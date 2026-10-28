import importlib.util
import json
from pathlib import Path
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('watch_ci', ROOT / 'skills/pr-ci-watch/scripts/watch_ci.py')
watcher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(watcher)


def response(data, code=0):
    return subprocess.CompletedProcess([], code, json.dumps(data), '')


def open_head(sha='aaa'):
    return response({'headRefOid': sha, 'state': 'OPEN'})


@pytest.mark.parametrize('last,watch_code,expected', [
    (open_head(), 0, ('CI_PASSED', 0)),
    (open_head('bbb'), 0, ('HEAD_CHANGED', 3)),
    (open_head(), 1, ('CI_FAILED_OR_UNAVAILABLE', 1)),
    (open_head(), 8, ('CI_PENDING', 3)),
    (response({'headRefOid': 'aaa', 'state': 'MERGED'}), 0, ('MERGED_EXTERNALLY', 3)),
])
def test_watch_checks_head_after_watcher(monkeypatch, last, watch_code, expected):
    outputs = iter([open_head(), response([{'name': 'tests'}]), response([], watch_code), last,
                    response([{'name': 'tests', 'bucket': 'pass'}]), open_head()])
    calls = []

    def run(args, **kwargs):
        calls.append(args)
        assert 0 < kwargs['timeout'] <= 30
        assert kwargs['capture_output']
        return next(outputs)

    monkeypatch.setattr(watcher.subprocess, 'run', run)
    assert watcher.watch(12, 'owner/repo', 30) == expected
    assert '--watch' in calls[2]
    assert all(cmd[:2] == ['gh', 'pr'] for cmd in calls)


def test_no_checks_is_not_success(monkeypatch):
    outputs = iter([open_head(), response([])])
    monkeypatch.setattr(watcher.subprocess, 'run', lambda *a, **k: next(outputs))
    assert watcher.watch(12, 'owner/repo', 30) == ('NO_REQUIRED_CHECKS', 3)


@pytest.mark.parametrize('checks', [[], [{'name': 'tests', 'bucket': 'skipping'}],
                                   [{'name': 'tests', 'bucket': 'pending'}]])
def test_success_exit_without_passing_checks_is_inconclusive(monkeypatch, checks):
    outputs = iter([open_head(), response([{'name': 'tests'}]), response([]),
                    open_head(), response(checks)])
    monkeypatch.setattr(watcher.subprocess, 'run', lambda *a, **k: next(outputs))
    assert watcher.watch(12, 'owner/repo', 30) == ('CI_INCONCLUSIVE', 3)


def test_api_failure_is_not_empty_success(monkeypatch):
    outputs = iter([open_head(), subprocess.CompletedProcess([], 1, '', 'private API error')])
    monkeypatch.setattr(watcher.subprocess, 'run', lambda *a, **k: next(outputs))
    with pytest.raises(watcher.WatchError):
        watcher.watch(12, 'owner/repo', 30)


def test_cli_timeout_is_explicit_and_redacts_output(monkeypatch, capsys):
    monkeypatch.setattr(watcher.subprocess, 'run', lambda *a, **k: (_ for _ in ()).throw(subprocess.TimeoutExpired(a[0], 1, output='private log')))
    monkeypatch.setattr('sys.argv', ['watch_ci.py', '12', '--repo', 'owner/repo', '--timeout', '1'])
    assert watcher.main() == 3
    output = capsys.readouterr().out
    assert json.loads(output)['state'] == 'TIMEOUT'
    assert 'private log' not in output


def test_missing_gh_is_explicit(monkeypatch, capsys):
    monkeypatch.setattr(watcher.subprocess, 'run', lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError()))
    monkeypatch.setattr('sys.argv', ['watch_ci.py', '12', '--repo', 'owner/repo'])
    assert watcher.main() == 2
    assert json.loads(capsys.readouterr().out)['state'] == 'BLOCKED'


@pytest.mark.parametrize('argv', [
    ['0', '--repo', 'owner/repo'], ['12', '--repo', '--malformed'],
    ['12', '--repo', 'owner/repo', '--timeout', '1801'],
])
def test_invalid_cli_arguments(monkeypatch, argv):
    monkeypatch.setattr('sys.argv', ['watch_ci.py', *argv])
    with pytest.raises(SystemExit) as exc:
        watcher.main()
    assert exc.value.code == 2
