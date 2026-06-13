from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from abvx_agent_skills.catalog_okf import export_okf_catalog


ROOT = Path(__file__).resolve().parents[1]


class ExportOkfTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmpdir.name) / "repo"
        shutil.copytree(ROOT / "skills", self.repo / "skills")
        self.output_dir = self.repo / "catalog" / "okf"

    def tearDown(self) -> None:
        self._tmpdir.cleanup()

    def test_export_writes_root_index_and_skill_concepts(self) -> None:
        results = export_okf_catalog(
            self.repo,
            self.output_dir,
            dry_run=False,
            print_diff=False,
        )
        self.assertTrue(any(row.changed for row in results))
        self.assertTrue((self.output_dir / "index.md").is_file())
        self.assertTrue((self.output_dir / "skills" / "rtk-assisted-shell.md").is_file())
        self.assertTrue(
            (
                self.output_dir
                / "groups"
                / "token-economy-context-control"
                / "index.md"
            ).is_file()
        )

        root_index = (self.output_dir / "index.md").read_text(encoding="utf-8")
        self.assertIn("ABVX Skills Catalog", root_index)
        self.assertIn(
            "groups/token-economy-context-control/index.md", root_index
        )

        skill_doc = (
            self.output_dir / "skills" / "rtk-assisted-shell.md"
        ).read_text(encoding="utf-8")
        self.assertIn('type: "Skill Catalog Entry"', skill_doc)
        self.assertIn('canonical: "skills/rtk-assisted-shell"', skill_doc)
        self.assertIn("# Trigger", skill_doc)

    def test_export_check_mode_stabilizes_after_first_write(self) -> None:
        export_okf_catalog(
            self.repo,
            self.output_dir,
            dry_run=False,
            print_diff=False,
        )
        results = export_okf_catalog(
            self.repo,
            self.output_dir,
            dry_run=True,
            print_diff=False,
        )
        self.assertTrue(results)
        self.assertTrue(all(row.action == "skipped" for row in results))
        self.assertTrue(all(not row.changed for row in results))

    def test_partial_export_omits_absent_group_links(self) -> None:
        partial_repo = Path(self._tmpdir.name) / "partial-repo"
        (partial_repo / "skills").mkdir(parents=True)
        shutil.copytree(
            ROOT / "skills" / "rtk-assisted-shell",
            partial_repo / "skills" / "rtk-assisted-shell",
        )
        partial_output = partial_repo / "catalog" / "okf"

        export_okf_catalog(
            partial_repo,
            partial_output,
            dry_run=False,
            print_diff=False,
        )

        root_index = (partial_output / "index.md").read_text(encoding="utf-8")
        self.assertIn(
            "groups/token-economy-context-control/index.md",
            root_index,
        )
        self.assertNotIn(
            "groups/coding-debugging-architecture/index.md",
            root_index,
        )
        self.assertFalse(
            (
                partial_output
                / "groups"
                / "coding-debugging-architecture"
                / "index.md"
            ).exists()
        )


if __name__ == "__main__":
    unittest.main()
