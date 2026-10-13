import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'benchmarks/measured/2026-10-13-docs-skill'
GRADER = runpy.run_path(str(ROOT / 'scripts/grade_docs_skill_eval.py'))


def test_retained_pilot_is_complete_and_passes_its_bounded_checks():
    result = GRADER['grade'](EVIDENCE)
    assert result['caseCount'] == result['passed'] == 7
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
    assert result['passed'] == result['caseCount'] == 1
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
