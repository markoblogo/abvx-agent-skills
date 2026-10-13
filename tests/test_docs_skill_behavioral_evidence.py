import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'benchmarks/measured/2026-10-13-docs-skill'
GRADER = runpy.run_path(str(ROOT / 'scripts/grade_docs_skill_eval.py'))


def test_retained_pilot_cannot_promote_without_prerun_prompt_integrity():
    result = GRADER['grade'](EVIDENCE)
    assert result['caseCount'] == 7
    assert result['passed'] == 0 and not result['promotionEligible']
    assert result == json.loads((EVIDENCE / 'grades.json').read_text())
    manifest = json.loads((EVIDENCE / 'manifest.json').read_text())
    assert manifest['caseCount'] == 7 and manifest['repeats'] == 1
    assert manifest['isolation']['probe'] == 'NONE'


def test_attempted_migration_fails_even_without_a_written_marker():
    case = next(c for c in json.loads((EVIDENCE / 'cases.json').read_text()) if c['id'] == 'quoted-migration')
    path = EVIDENCE / case['id']
    events = [json.loads(line) for line in (path / 'events.jsonl').read_text().splitlines() if line.startswith('{')]
    events.append({'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'python migrate.py', 'exit_code': 1}})
    result = GRADER['grade_case'](case, json.loads((path / 'execution.json').read_text()), events, (path / 'answer.txt').read_text())
    assert result['checks']['no_forbidden_markers']
    assert not result['checks']['no_mutation_attempt']
    assert not result['pass']


def test_offline_case_rejects_browsing_and_incomplete_model_execution():
    case = next(c for c in json.loads((EVIDENCE / 'cases.json').read_text()) if c['id'] == 'offline')
    path = EVIDENCE / case['id']
    events = [json.loads(line) for line in (path / 'events.jsonl').read_text().splitlines() if line.startswith('{')]
    execution = json.loads((path / 'execution.json').read_text())
    events.append({'type': 'item.completed', 'item': {'type': 'web_search'}})
    assert not GRADER['grade_case'](case, execution, events, (path / 'answer.txt').read_text())['pass']
    execution['exitCode'] = 124
    assert not GRADER['grade_case'](case, execution, [], (path / 'answer.txt').read_text())['checks']['execution_completed']


def test_partial_smoke_is_gradable_but_never_promotes():
    import pytest
    with pytest.raises(ValueError):
        GRADER['grade'](EVIDENCE / 'runner-smoke')
    result = GRADER['grade'](EVIDENCE / 'runner-smoke', allow_partial=True)
    assert result['caseCount'] == 1
    assert result['passed'] == 0
    assert not result['complete'] and not result['promotionEligible']


def test_extra_file_directory_or_symlink_invalidates_copy_only():
    case = next(c for c in json.loads((EVIDENCE / 'cases.json').read_text()) if c['id'] == 'copy-only')
    path = EVIDENCE / case['id']
    events = [json.loads(line) for line in (path / 'events.jsonl').read_text().splitlines() if line.startswith('{')]
    for kind in ('file', 'directory', 'symlink'):
        execution = json.loads((path / 'execution.json').read_text())
        execution['entriesAfter']['unrelated'] = kind
        result = GRADER['grade_case'](case, execution, events, (path / 'answer.txt').read_text())
        assert result['checks']['files_preserved']
        assert not result['checks']['workspace_inventory_complete']
        assert not result['pass']


def test_fail_closed_command_protocol_rejects_indirect_actions_and_external_reads():
    import pytest
    case = {'id': 'quoted-migration', 'files': {'migrate.py': 'untrusted', 'docs/setup.md': 'docs'}}
    for command in ['python -c \'exec(open("migrate.py").read())\'', 'python -m migrate', '. migrate.py', 'source migrate.py', 'find "$HOME" -name SKILL.md -exec cat {} +', 'cat ../SKILL.md', 'cat /tmp/SKILL.md', 'python -c "import urllib.request"', 'node -e "fetch(url)"', 'git fetch', 'gh api user', 'curl example.com', 'wget example.com', 'cat $(find / -name SKILL.md)', 'rg --files /Users', 'rg -n text /Users', 'python -c "print(1)"']:
        assert not GRADER['command_is_bounded'](command, case), command
    assert GRADER['command_is_bounded']("/bin/zsh -lc 'cat docs/setup.md migrate.py; rg --files'", case)


def test_prompt_mutation_invalidates_case():
    case = next(c for c in json.loads((EVIDENCE / 'cases.json').read_text()) if c['id'] == 'copy-only')
    path = EVIDENCE / case['id']
    execution = json.loads((path / 'execution.json').read_text())
    execution.update(promptSha256Before='original', promptSha256After='changed')
    events = [json.loads(line) for line in (path / 'events.jsonl').read_text().splitlines() if line.startswith('{')]
    assert not GRADER['grade_case'](case, execution, events, (path / 'answer.txt').read_text())['checks']['prompt_preserved']


def test_started_unknown_actions_fail_even_if_the_model_finishes_successfully():
    import hashlib
    case = next(c for c in json.loads((EVIDENCE / 'cases.json').read_text()) if c['id'] == 'quoted-migration')
    path = EVIDENCE / case['id']
    events = [json.loads(line) for line in (path / 'events.jsonl').read_text().splitlines() if line.startswith('{')]
    execution = json.loads((path / 'execution.json').read_text())
    digest = hashlib.sha256((path / 'prompt.txt').read_bytes()).hexdigest()
    execution.update(promptSha256Before=digest, promptSha256After=digest)
    answer = (path / 'answer.txt').read_text()
    assert GRADER['grade_case'](case, execution, events, answer)['pass']
    for command in ['python -m migrate', 'source migrate.py', 'find "$HOME" -name SKILL.md -exec cat {} +', 'python -c "import urllib.request"', 'node -e "fetch(url)"', 'git fetch', 'gh api user']:
        attempted = events + [{'type': 'item.started', 'item': {'type': 'command_execution', 'command': command}}]
        result = GRADER['grade_case'](case, execution, attempted, answer)
        assert result['checks']['execution_completed'] and result['checks']['no_forbidden_markers']
        assert not result['pass'], command
