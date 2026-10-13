"""Staged skill installation with preflight, durable undo journals and manifests.

Renames are atomic per directory; the set is recoverable as a transaction, not
simultaneously visible to external readers. Never erase replaced user payloads.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import uuid

from . import __version__
from .validator import validate_skill

PROFILES = {
    'context': ['token-efficient-execution', 'shell-output-compaction', 'lean-context-layout', 'compaction-survival'],
    'debug': ['diagnose', 'bug-evidence-protocol', 'test-driven-execution'],
    'delivery': ['delivery-preflight-gate', 'delivery-baseline-audit', 'public-release-verification'],
}
STATE = '.abvx-skills'


class InstallError(ValueError):
    pass


def _name(name):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        raise InstallError(f'Invalid skill name: {name}')
    return name


def payload(path):
    if path.is_symlink() or not path.is_dir():
        raise InstallError(f'Expected a real skill directory: {path}')
    result = {}
    for item in sorted(path.rglob('*')):
        relative = item.relative_to(path)
        if '__pycache__' in relative.parts or item.suffix == '.pyc' or item.name == '.DS_Store':
            continue
        if item.is_symlink():
            raise InstallError(f'Symlink in skill payload: {item}')
        if item.is_file():
            result[relative.as_posix()] = {'sha256': hashlib.sha256(item.read_bytes()).hexdigest(), 'executable': bool(item.stat().st_mode & 0o111)}
        elif not item.is_dir():
            raise InstallError(f'Unsupported file type: {item}')
    return result


def digest(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def _state(destination):
    if destination.exists() and not destination.is_dir():
        raise InstallError('Destination must be a directory')
    # Keep archived SKILL.md files outside the agent discovery root.
    state = destination.parent / ('.' + destination.name + STATE)
    if state.is_symlink() or (state.exists() and not state.is_dir()):
        raise InstallError('Installer state must be a real directory')
    for name in ('manifest.json', 'lock', 'transactions'):
        if (state / name).is_symlink():
            raise InstallError(f'Unsafe installer state path: {name}')
    return state


def read_manifest(destination):
    path = _state(destination) / 'manifest.json'
    if not path.exists():
        return {'schema_version': 1, 'skills': {}, 'profiles': [], 'last_transaction': None}
    data = json.loads(path.read_text())
    if data.get('schema_version') != 1 or not isinstance(data.get('skills'), dict):
        raise InstallError('Unsupported or invalid manifest')
    for name, record in data['skills'].items():
        _name(name)
        if not isinstance(record, dict) or not isinstance(record.get('files'), dict):
            raise InstallError(f'Invalid manifest record: {name}')
    tx = data.get('last_transaction')
    if tx is not None and not re.fullmatch(r'[a-f0-9]{32}', tx):
        raise InstallError('Invalid manifest transaction')
    return data


def _write(path, value):
    temporary = path.with_name(path.name + '.tmp')
    if path.is_symlink() or temporary.is_symlink():
        raise InstallError('Unsafe state file')
    with temporary.open('w') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


@contextmanager
def locked(destination, create=True):
    state = _state(destination)
    if create:
        destination.mkdir(parents=True, exist_ok=True)
        state.mkdir(parents=True, exist_ok=True)
    if create and destination.stat().st_dev != state.stat().st_dev:
        raise InstallError('Use a skill subdirectory on the same filesystem as its sibling state')
    flags = (os.O_CREAT if create else 0) | os.O_RDWR | getattr(os, 'O_NOFOLLOW', 0)
    fd = os.open(state / 'lock', flags, 0o600)
    try:
        if os.name == 'nt':
            import msvcrt
            if os.fstat(fd).st_size == 0:
                os.write(fd, b'0')
            os.lseek(fd, 0, 0)
            msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield state
    finally:
        os.close(fd)


def _journal(folder):
    if not re.fullmatch(r'[a-f0-9]{32}', folder.name) or folder.is_symlink() or not folder.is_dir():
        raise InstallError('Unsafe transaction directory')
    for name in ('journal.json', 'stage', 'backup', 'replaced'):
        if (folder / name).is_symlink():
            raise InstallError('Symlink in transaction state')
    data = json.loads((folder / 'journal.json').read_text())
    if data.get('status') not in ('prepared', 'applying', 'committed', 'rolled_back') or not isinstance(data.get('operations'), list) or not isinstance(data.get('had_manifest'), bool):
        raise InstallError('Invalid transaction journal')
    names = []
    for operation in data['operations']:
        names.append(_name(operation['name']))
        if operation.get('before') is not None and not isinstance(operation['before'], dict):
            raise InstallError('Invalid prior payload record')
    if len(set(names)) != len(names) or not isinstance(data.get('previous_manifest'), dict) or data['previous_manifest'].get('schema_version') != 1:
        raise InstallError('Invalid undo manifest')
    return data


def _pending(state):
    transactions = state / 'transactions'
    if not transactions.exists():
        return []
    result = []
    for folder in transactions.iterdir():
        if folder.is_symlink():
            raise InstallError('Unsafe transaction directory')
        path = folder / 'journal.json'
        if path.exists() and _journal(folder)['status'] == 'applying':
            result.append(folder)
    return result


def plan(source, destination, names, force=False):
    manifest = read_manifest(destination)
    if _pending(_state(destination)):
        raise InstallError('Interrupted transaction; run abvx-skills recover first')
    result = []
    for name in dict.fromkeys(names):
        _name(name)
        folder = source / name
        incoming = payload(folder)
        failures = []
        validate_skill(folder, failures)
        if failures:
            raise InstallError('\n'.join(failures))
        target = destination / name
        existing = payload(target) if target.exists() or target.is_symlink() else None
        record = manifest['skills'].get(name)
        if existing is None:
            action = 'install'
        elif existing == incoming:
            action = 'unchanged' if record else 'adopt'
        elif not force and (not record or existing != record['files']):
            action = 'conflict'
        else:
            action = 'update'
        result.append({'name': name, 'action': action, 'before': existing, 'files': incoming,
                       'local_changes': bool(existing is not None and (not record or existing != record['files'])),
                       'added': sorted(set(incoming) - set(existing or {})),
                       'removed': sorted(set(existing or {}) - set(incoming)),
                       'changed': sorted(p for p in set(incoming) & set(existing or {}) if incoming[p] != existing[p])})
    return result


def _restore(destination, folder, journal):
    for op in reversed(journal['operations']):
        name = _name(op['name'])
        target, backup, staged = destination / name, folder / 'backup' / name, folder / 'stage' / name
        if backup.exists():
            if target.exists() or target.is_symlink():
                saved = folder / 'replaced' / name
                saved.parent.mkdir(exist_ok=True)
                if saved.exists():
                    saved = saved.with_name(name + '-' + uuid.uuid4().hex)
                os.replace(target, saved)
            os.replace(backup, target)
        elif op['before'] is None and not staged.exists() and (target.exists() or target.is_symlink()):
            saved = folder / 'replaced' / name
            saved.parent.mkdir(exist_ok=True)
            os.replace(target, saved)
    manifest = _state(destination) / 'manifest.json'
    if journal['had_manifest']:
        _write(manifest, journal['previous_manifest'])
    elif manifest.exists():
        manifest.unlink()
    journal['status'] = 'rolled_back'
    _write(folder / 'journal.json', journal)


def install(source, destination, names, force=False, profile=None):
    # Entire selection is checked before even creating destination/state.
    first = plan(source, destination, names, force)
    if any(op['action'] == 'conflict' for op in first):
        raise InstallError('Local/unmanaged skill conflict; preview changes or use --force (backups retained)')
    with locked(destination) as state:
        selection = plan(source, destination, names, force)
        if any(op['action'] == 'conflict' for op in selection):
            raise InstallError('Selection changed during preflight')
        old = read_manifest(destination)
        tx = uuid.uuid4().hex
        folder = state / 'transactions' / tx
        (folder / 'stage').mkdir(parents=True)
        (folder / 'backup').mkdir()
        operations = [op for op in selection if op['action'] in ('install', 'update')]
        journal = {'status': 'prepared', 'operations': operations, 'previous_manifest': old,
                   'had_manifest': (state / 'manifest.json').exists()}
        _write(folder / 'journal.json', journal)
        for op in operations:
            shutil.copytree(source / op['name'], folder / 'stage' / op['name'], ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
            if payload(folder / 'stage' / op['name']) != op['files']:
                raise InstallError('Package changed while staging')
        for op in selection:
            target = destination / op['name']
            actual = payload(target) if target.exists() or target.is_symlink() else None
            if actual != op['before']:
                raise InstallError('Local files changed while staging; nothing applied')
        journal['status'] = 'applying'
        _write(folder / 'journal.json', journal)
        try:
            for op in operations:
                target = destination / op['name']
                current = payload(target) if target.exists() or target.is_symlink() else None
                if current != op['before']:
                    raise InstallError('Local files changed during commit; rolling back')
                if op['before'] is not None:
                    os.replace(target, folder / 'backup' / op['name'])
                os.replace(folder / 'stage' / op['name'], target)
            new = json.loads(json.dumps(old))
            for op in selection:
                card = (source / op['name'] / 'SKILL_CARD.md').read_text()
                version = re.search(r'## Version\s+([^\s]+)', card)
                new['skills'][op['name']] = {'skill_version': version.group(1) if version else None,
                    'package_version': __version__, 'source': 'abvx-agent-skills package',
                    'upstream': 'https://github.com/markoblogo/abvx-agent-skills',
                    'sha256': digest(op['files']), 'files': op['files']}
            if profile:
                new['profiles'] = sorted(set(new.get('profiles', [])) | {profile})
            new['last_transaction'] = tx
            new['updated_at'] = datetime.now(timezone.utc).isoformat()
            _write(state / 'manifest.json', new)
            journal['status'] = 'committed'
            _write(folder / 'journal.json', journal)
        except BaseException:
            # Ordinary failures restore the complete set; a killed process uses recover.
            journal['status'] = 'applying'
            _write(folder / 'journal.json', journal)
            _restore(destination, folder, journal)
            raise
    return tx


def rollback(destination, force=False):
    with locked(destination) as state:
        if _pending(state):
            raise InstallError('Run recover before rollback')
        manifest = read_manifest(destination)
        tx = manifest.get('last_transaction')
        if not tx:
            raise InstallError('No managed transaction to roll back')
        folder = state / 'transactions' / tx
        if folder.is_symlink() or (folder / 'journal.json').is_symlink():
            raise InstallError('Unsafe rollback journal')
        journal = _journal(folder)
        if journal['status'] != 'committed':
            raise InstallError('Transaction is not committed')
        for name, record in manifest['skills'].items():
            target = destination / _name(name)
            if not force and (not target.exists() or payload(target) != record['files']):
                raise InstallError('Local changes after installation; use --force to retain them in history and roll back')
        _restore(destination, folder, journal)
        return tx


def recover(destination):
    with locked(destination) as state:
        pending = _pending(state)
        for folder in pending:
            _restore(destination, folder, _journal(folder))
        return [p.name for p in pending]


def _doctor(source, destination):
    manifest = read_manifest(destination)
    result = []
    for name, record in sorted(manifest['skills'].items()):
        target = destination / name
        if not target.exists():
            status = 'missing'
        elif payload(target) != record['files']:
            status = 'modified'
        else:
            status = 'ok'
        packaged = source / name
        update = packaged.is_dir() and payload(packaged) != record['files']
        result.append({'name': name, 'status': status, 'update_available': update,
                       'installed_package_version': record.get('package_version')})
    unmanaged = sorted(p.name for p in destination.iterdir() if p.is_dir() and (p / 'SKILL.md').is_file() and p.name not in manifest['skills']) if destination.exists() else []
    return {'skills': result, 'unmanaged': unmanaged, 'profiles': manifest.get('profiles', []),
            'pending_transactions': [p.name for p in _pending(_state(destination))],
            'package_version': __version__, 'manifest_path': str(_state(destination) / 'manifest.json')}


def doctor(source, destination):
    if (_state(destination) / 'lock').exists():
        with locked(destination, create=False):
            return _doctor(source, destination)
    return _doctor(source, destination)
