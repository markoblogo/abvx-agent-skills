import json
from pathlib import Path

from abvx_agent_skills.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_has_complete_metadata_and_categories():
    catalog = build_catalog(ROOT / 'skills', ROOT / 'README.md')
    assert catalog['skill_count'] == len(catalog['skills'])
    for item in catalog['skills']:
        assert item['status'], item['name']
        assert item['origin'], item['name']
        assert item['category'] != 'Uncategorized', item['name']


def test_docs_skill_scenarios_cover_activation_negative_and_authority():
    scenarios = json.loads((ROOT / 'benchmarks/fixture-cases/read-the-damn-docs.json').read_text())
    assert scenarios['skill'] == 'read-the-damn-docs'
    # Promotion is backed by the retained model pilot, not authored prompts alone.
    assert scenarios['eval_tier'] == 'fixture_checked'
    assert (ROOT / 'benchmarks/measured/2026-10-13-docs-skill/grades.json').is_file()
    ids = []
    for category in ('activation', 'negative', 'authority'):
        assert scenarios[category]
        for case in scenarios[category]:
            assert case['request'] and case['expected']
            ids.append(case['id'])
    assert len(ids) == len(set(ids))
    skill = next(item for item in build_catalog(ROOT / 'skills', ROOT / 'README.md')['skills'] if item['name'] == scenarios['skill'])
    assert skill['eval_tier'] == scenarios['eval_tier']


def test_readme_tables_have_headers_and_consistent_cell_counts():
    lines = (ROOT / 'README.md').read_text().splitlines()
    width = None
    for index, line in enumerate(lines):
        if line.startswith('|'):
            cells = line.strip().strip('|').split('|')
            if width is None:
                assert index + 1 < len(lines) and lines[index + 1].startswith('|---'), f'Orphan table row: {line}'
                width = len(cells)
            assert len(cells) == width, line
        else:
            width = None
