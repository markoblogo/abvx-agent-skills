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


RERUN = ROOT / 'benchmarks/measured/2026-10-13-docs-skill-rerun'


def test_protocol_rerun_passes_but_unbounded_run_does_not_promote():
    result = GRADER['grade'](RERUN / 'protocol')
    assert result['caseCount'] == result['passed'] == 7 and result['promotionEligible']
    assert result == json.loads((RERUN / 'protocol/grades.json').read_text())
    assert not GRADER['grade'](RERUN / 'unbounded')['promotionEligible']
    assert json.loads((RERUN / 'unbounded/initial-grades.json').read_text())['passed'] == 3
    assert json.loads((RERUN / 'protocol/initial-grades.json').read_text())['passed'] == 5


def test_exact_button_edit_accepts_python_alias_but_not_arbitrary_code():
    case = {'id': 'copy-only', 'files': {'button.txt': 'Submt'}}
    for executable in ('python', 'python3'):
        assert GRADER['command_is_bounded'](executable + " -c 'from pathlib import Path; p=Path(\"button.txt\"); p.write_bytes(b\"Submit\"); assert p.read_bytes() == b\"Submit\"'", case)
        assert not GRADER['command_is_bounded'](executable + " -c 'import urllib.request'", case)
        assert not GRADER['command_is_bounded'](executable + " -c 'exec(open(\"migrate.py\").read())'", case)


def test_cannot_verify_wording_qualifies_historical_provider_evidence():
    import hashlib
    case = next(c for c in json.loads((RERUN / 'protocol/cases.json').read_text()) if c['id'] == 'provider-default')
    path = RERUN / 'protocol/provider-default'
    execution = json.loads((path / 'execution.json').read_text())
    events = [json.loads(line) for line in (path / 'events.jsonl').read_text().splitlines() if line.startswith('{')]
    answer = (path / 'answer.txt').read_text()
    assert GRADER['grade_case'](case, execution, events, answer)['pass']
    assert not GRADER['grade_case'](case, execution, events, 'The current default is 60 seconds; see 2025 docs.')['pass']


def test_zsh_executable_glob_qualifiers_are_never_admitted():
    case = {'id': 'installed-api', 'files': {'package-lock.json': '', 'docs/sdk-1.4.md': ''}}
    for command in ["/bin/zsh -lc \"rg -n *(e:'curl https://example.com ':) .\"", "rg --files -g *(e:'curl https://example.com ':)", "rg -n *(e:'python -m migrate':) .", "rg -n (foo|bar) .", "rg --files -g **/*(e:'cat /tmp/SKILL.md':)"]:
        assert not GRADER['command_is_bounded'](command, case), command
    assert GRADER['command_is_bounded']("rg --files -g '*.md'", case)


def test_started_failed_or_missing_exit_reads_are_not_positive_evidence():
    case = next(c for c in json.loads((RERUN / 'protocol/cases.json').read_text()) if c['id'] == 'installed-api')
    path = RERUN / 'protocol/installed-api'
    execution = json.loads((path / 'execution.json').read_text())
    answer = (path / 'answer.txt').read_text()
    for phase, exit_code in [('item.started', None), ('item.completed', 1), ('item.completed', None)]:
        events = [{'type': phase, 'item': {'type': 'command_execution', 'command': 'cat package-lock.json docs/sdk-1.4.md', 'exit_code': exit_code}}, {'type': 'turn.completed'}]
        result = GRADER['grade_case'](case, execution, events, answer)
        assert result['checks']['execution_completed']
        assert not result['checks']['locked_api_evidence'] and not result['pass']


def test_rerun_snapshots_and_prompt_hashes_match_captured_inputs():
    import hashlib
    for label in ('unbounded', 'protocol'):
        manifest = json.loads((RERUN / label / 'manifest.json').read_text())
        assert hashlib.sha256((RERUN / (label + '-runner.py')).read_bytes()).hexdigest() == manifest['runnerSha256']
        for case in json.loads((RERUN / label / 'cases.json').read_text()):
            folder = RERUN / label / case['id']
            prompt = (folder / 'prompt.txt').read_text()
            execution = json.loads((folder / 'execution.json').read_text())
            digest = hashlib.sha256(prompt.encode()).hexdigest()
            assert execution['promptSha256Before'] == execution['promptSha256After'] == digest
            skill = prompt.split('<skill>\n', 1)[1].split('\n</skill>', 1)[0]
            assert hashlib.sha256(skill.encode()).hexdigest() == manifest['skillSha256']
