from pathlib import Path
import shutil

import pytest
from abvx_agent_skills import cli

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def package(tmp_path, monkeypatch):
    source = tmp_path / 'package'
    for name in ('minimal-diff-builder', 'diagnose'):
        shutil.copytree(ROOT / 'skills' / name, source / name)
    monkeypatch.setattr(cli, 'packaged_skills_root', lambda: source)
    return source


def test_conflict_is_detected_before_any_skill_is_installed(package, tmp_path):
    destination = tmp_path / 'installed'
    local = destination / 'diagnose'
    local.mkdir(parents=True)
    (local / 'SKILL.md').write_text('Local customized instructions')
    assert cli.main(['install', 'minimal-diff-builder', 'diagnose', '-d', str(destination)]) == 2
    assert not (destination / 'minimal-diff-builder').exists()
    assert (local / 'SKILL.md').read_text() == 'Local customized instructions'


def test_preview_has_no_filesystem_side_effects(package, tmp_path, capsys):
    destination = tmp_path / 'not-created'
    assert cli.main(['install', 'diagnose', '-d', str(destination), '--dry-run']) == 0
    assert not destination.exists()
    assert 'install' in capsys.readouterr().out


def test_explicit_selection_is_required(package, tmp_path):
    destination = tmp_path / 'installed'
    assert cli.main(['install', '-d', str(destination)]) == 2
    assert not destination.exists()


def test_managed_update_preserves_customizations_and_force_keeps_backup(package, tmp_path):
    import json
    destination = tmp_path / 'installed'
    args = ['install', 'diagnose', '-d', str(destination)]
    assert cli.main(args) == 0
    target = destination / 'diagnose/SKILL.md'
    original = target.read_text()
    target.write_text(original + '\nLocal rule\n')
    assert cli.main(args) == 2
    assert 'Local rule' in target.read_text()
    assert cli.main(args + ['--force']) == 0
    state = destination.parent / ('.' + destination.name + '.abvx-skills')
    manifest = json.loads((state / 'manifest.json').read_text())
    backup = state / 'transactions' / manifest['last_transaction'] / 'backup/diagnose/SKILL.md'
    assert 'Local rule' in backup.read_text()
    assert target.read_text() == original
    assert cli.main(['rollback', '-d', str(destination)]) == 0
    assert 'Local rule' in target.read_text()
    assert cli.main(['doctor', '-d', str(destination)]) == 1


def test_upgrade_is_allowed_only_for_unchanged_managed_payload(package, tmp_path, capsys):
    import json
    destination = tmp_path / 'installed'
    args = ['install', 'diagnose', '-d', str(destination)]
    assert cli.main(args) == 0
    (package / 'diagnose/SKILL.md').write_text((package / 'diagnose/SKILL.md').read_text() + '\nNew release instruction\n')
    capsys.readouterr()
    assert cli.main(['doctor', '-d', str(destination)]) == 0
    assert json.loads(capsys.readouterr().out)['skills'][0]['update_available']
    assert cli.main(args) == 0
    assert 'New release instruction' in (destination / 'diagnose/SKILL.md').read_text()
    assert cli.main(['rollback', '-d', str(destination)]) == 0
    assert 'New release instruction' not in (destination / 'diagnose/SKILL.md').read_text()


def test_commit_failure_restores_all_skills_and_manifest(package, tmp_path, monkeypatch):
    from abvx_agent_skills import installer
    destination = tmp_path / 'installed'
    args = ['install', 'minimal-diff-builder', 'diagnose', '-d', str(destination)]
    assert cli.main(args) == 0
    old = (destination.parent / ('.' + destination.name + '.abvx-skills') / 'manifest.json').read_bytes()
    originals = {n: (destination / n / 'SKILL.md').read_bytes() for n in ('minimal-diff-builder', 'diagnose')}
    for n in originals:
        (package / n / 'SKILL.md').write_text((package / n / 'SKILL.md').read_text() + '\nNew behavior\n')
    rename = installer.os.replace
    failed = False
    def fail_second(source, target):
        nonlocal failed
        if not failed and Path(source).parent.name == 'stage' and Path(target).name == 'diagnose':
            failed = True
            raise OSError('Simulated rename failure')
        return rename(source, target)
    monkeypatch.setattr(installer.os, 'replace', fail_second)
    assert cli.main(args) == 2
    assert (destination.parent / ('.' + destination.name + '.abvx-skills') / 'manifest.json').read_bytes() == old
    for n, content in originals.items():
        assert (destination / n / 'SKILL.md').read_bytes() == content


def test_rollback_refuses_post_install_edits_unless_retained(package, tmp_path):
    destination = tmp_path / 'installed'
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 0
    (destination / 'diagnose/SKILL.md').write_text('new local work')
    assert cli.main(['rollback', '-d', str(destination)]) == 2
    assert (destination / 'diagnose/SKILL.md').read_text() == 'new local work'
    assert cli.main(['rollback', '-d', str(destination), '--force']) == 0
    assert not (destination / 'diagnose').exists()
    assert any(p.read_text() == 'new local work' for p in (destination.parent / ('.' + destination.name + '.abvx-skills') / 'transactions').glob('*/replaced/diagnose/SKILL.md'))


def test_unknown_and_traversal_names_do_not_modify_destination(package, tmp_path):
    destination = tmp_path / 'installed'
    for names in [['diagnose', 'not-a-skill'], ['../diagnose']]:
        assert cli.main(['install', *names, '-d', str(destination)]) == 2
        assert not destination.exists()


def test_source_symlinks_and_target_symlinks_are_rejected(package, tmp_path):
    destination = tmp_path / 'installed'
    (package / 'diagnose/extra').symlink_to(tmp_path / 'elsewhere')
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 2
    assert not destination.exists()
    (package / 'diagnose/extra').unlink()
    destination.mkdir()
    (destination / 'diagnose').symlink_to(package / 'diagnose', target_is_directory=True)
    assert cli.main(['install', 'diagnose', '-d', str(destination), '--force']) == 2


def test_all_profiles_install_only_their_small_selection(tmp_path, monkeypatch):
    import json
    from abvx_agent_skills import installer
    monkeypatch.setattr(cli, 'packaged_skills_root', lambda: ROOT / 'skills')
    for name, skills in installer.PROFILES.items():
        destination = tmp_path / name
        assert cli.main(['install', '--profile', name, '-d', str(destination)]) == 0
        manifest = json.loads((destination.parent / ('.' + destination.name + '.abvx-skills') / 'manifest.json').read_text())
        assert set(manifest['skills']) == set(skills)
        assert manifest['profiles'] == [name]
        assert cli.main(['doctor', '-d', str(destination)]) == 0


def test_process_interruption_is_recoverable_without_losing_later_local_edits(package, tmp_path):
    import json
    import os
    import subprocess
    import sys
    destination = tmp_path / 'installed'
    names = ['minimal-diff-builder', 'diagnose']
    assert cli.main(['install', *names, '-d', str(destination)]) == 0
    old = (destination.parent / ('.' + destination.name + '.abvx-skills') / 'manifest.json').read_bytes()
    for name in names:
        (package / name / 'SKILL.md').write_text((package / name / 'SKILL.md').read_text() + '\nUpgrade content\n')
    code = '''import os, sys
from pathlib import Path
from abvx_agent_skills import installer
original = os.replace
def interrupt(source, target):
    original(source, target)
    if Path(source).parent.name == 'stage':
        os._exit(77)
installer.os.replace = interrupt
installer.install(Path(sys.argv[1]), Path(sys.argv[2]), ['minimal-diff-builder','diagnose'])
'''
    result = subprocess.run([sys.executable, '-c', code, str(package), str(destination)], env=dict(os.environ, PYTHONPATH=str(ROOT / 'src')), timeout=20)
    assert result.returncode == 77
    assert cli.main(['doctor', '-d', str(destination)]) == 1
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 2
    first = destination / names[0] / 'SKILL.md'
    first.write_text(first.read_text() + '\nLocal work after interrupted update\n')
    assert cli.main(['recover', '-d', str(destination)]) == 0
    assert (destination.parent / ('.' + destination.name + '.abvx-skills') / 'manifest.json').read_bytes() == old
    for name in names:
        assert 'Upgrade content' not in (destination / name / 'SKILL.md').read_text()
    assert any('Local work after interrupted update' in p.read_text() for p in (destination.parent / ('.' + destination.name + '.abvx-skills') / 'transactions').glob('*/replaced/*/SKILL.md'))
    assert cli.main(['recover', '-d', str(destination)]) == 0


def test_manifest_write_failure_restores_new_install(package, tmp_path, monkeypatch):
    from abvx_agent_skills import installer
    destination = tmp_path / 'installed'
    write = installer._write
    def fail_manifest(path, data):
        if path.name == 'manifest.json':
            raise OSError('No space to save manifest')
        return write(path, data)
    monkeypatch.setattr(installer, '_write', fail_manifest)
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 2
    assert not (destination / 'diagnose').exists()
    assert not (destination.parent / ('.' + destination.name + '.abvx-skills') / 'manifest.json').exists()


def test_runtime_bytecode_does_not_count_as_local_customization(package, tmp_path, capsys):
    destination = tmp_path / 'installed'
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 0
    cache = destination / 'diagnose/__pycache__'
    cache.mkdir()
    (cache / 'runtime.pyc').write_bytes(b'cache')
    capsys.readouterr()
    assert cli.main(['doctor', '-d', str(destination)]) == 0


def test_identical_unmanaged_install_is_adopted_and_rollback_keeps_it(package, tmp_path):
    destination = tmp_path / 'installed'
    shutil.copytree(package / 'diagnose', destination / 'diagnose')
    before = (destination / 'diagnose/SKILL.md').read_bytes()
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 0
    assert cli.main(['rollback', '-d', str(destination)]) == 0
    assert (destination / 'diagnose/SKILL.md').read_bytes() == before


def test_state_backups_are_outside_skill_discovery_and_validation_root(package, tmp_path):
    from abvx_agent_skills.validator import validate_skills_root
    destination = tmp_path / 'installed'
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 0
    assert {p.name for p in destination.iterdir()} == {'diagnose'}
    assert not validate_skills_root(destination)


def test_symlink_in_installer_state_is_rejected_without_writes(package, tmp_path):
    destination = tmp_path / 'installed'
    state = destination.parent / ('.' + destination.name + '.abvx-skills')
    elsewhere = tmp_path / 'elsewhere'
    elsewhere.mkdir()
    state.symlink_to(elsewhere, target_is_directory=True)
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 2
    assert not destination.exists()
    assert not list(elsewhere.iterdir())


def test_doctor_is_read_only_when_nothing_is_installed(package, tmp_path):
    destination = tmp_path / 'installed'
    assert cli.main(['doctor', '-d', str(destination)]) == 0
    assert not destination.exists()
    assert not (tmp_path / '.installed.abvx-skills').exists()


def test_preview_lists_changed_and_removed_files(package, tmp_path, capsys):
    import json
    destination = tmp_path / 'installed'
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 0
    (destination / 'diagnose/local.txt').write_text('keep my data')
    capsys.readouterr()
    assert cli.main(['install', 'diagnose', '-d', str(destination), '--dry-run', '--force']) == 0
    preview = json.loads(capsys.readouterr().out)['preview'][0]
    assert preview['removed'] == ['local.txt']
    assert (destination / 'diagnose/local.txt').read_text() == 'keep my data'


def test_active_installer_lock_prevents_concurrent_mutation(package, tmp_path):
    from abvx_agent_skills import installer
    destination = tmp_path / 'installed'
    with installer.locked(destination):
        assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 2
        assert cli.main(['doctor', '-d', str(destination)]) == 2
    assert not (destination / 'diagnose').exists()


def test_new_history_is_private_on_posix(package, tmp_path):
    import os
    if os.name == 'nt':
        pytest.skip('Windows ACL verification is outside the current support evidence')
    destination = tmp_path / 'installed'
    assert cli.main(['install', 'diagnose', '-d', str(destination)]) == 0
    state = tmp_path / '.installed.abvx-skills'
    assert state.stat().st_mode & 0o777 == 0o700
    assert (state / 'manifest.json').stat().st_mode & 0o777 == 0o600


def test_repeated_restore_preserves_recreated_new_skill(package, tmp_path, monkeypatch):
    import json
    from abvx_agent_skills import installer
    destination = tmp_path / 'installed'
    installer.install(package, destination, ['diagnose'])
    state = installer._state(destination)
    manifest = installer.read_manifest(destination)
    folder = state / 'transactions' / manifest['last_transaction']
    journal = installer._journal(folder)
    journal['status'] = 'applying'
    installer._write(folder / 'journal.json', journal)
    original_write = installer._write
    def fail_journal(path, value):
        if Path(path).name == 'journal.json':
            raise OSError('Interrupted recovery')
        original_write(path, value)
    monkeypatch.setattr(installer, '_write', fail_journal)
    with pytest.raises(OSError):
        installer.recover(destination)
    assert (folder / 'replaced/diagnose/SKILL.md').exists()
    (destination / 'diagnose').mkdir()
    (destination / 'diagnose/SKILL.md').write_text('Recreated local content')
    monkeypatch.setattr(installer, '_write', original_write)
    assert installer.recover(destination) == [folder.name]
    assert not (destination / 'diagnose').exists()
    archived = list((folder / 'replaced').glob('diagnose*/SKILL.md'))
    assert len(archived) == 2
    assert 'Recreated local content' in [p.read_text() for p in archived]
    assert installer.recover(destination) == []


@pytest.mark.parametrize('kind', ['file', 'symlink', 'dangling', 'nested-symlink'])
def test_doctor_reports_unsafe_managed_paths_and_continues(package, tmp_path, kind):
    from abvx_agent_skills import installer
    destination = tmp_path / 'installed'
    installer.install(package, destination, ['diagnose', 'minimal-diff-builder'])
    target = destination / 'diagnose'
    if kind == 'nested-symlink':
        (target / 'extra').symlink_to(package)
    else:
        shutil.rmtree(target)
        if kind == 'file':
            target.write_text('Corrupt directory')
        else:
            target.symlink_to(package if kind == 'symlink' else tmp_path / 'absent')
    report = installer.doctor(package, destination)
    assert {s['name']: s['status'] for s in report['skills']} == {'diagnose': 'unsafe', 'minimal-diff-builder': 'ok'}
