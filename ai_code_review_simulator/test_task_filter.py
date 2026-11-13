import json
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from task_filter import Task, filter_tasks


class FilterTasksTests(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            Task("Write tests", "todo", date(2026, 11, 13)),
            Task("Review the PR", "in_progress", date(2026, 11, 14)),
            Task("Publish notes", "todo", date(2026, 11, 15)),
            Task("Refine the backlog", "todo"),
            Task("Plan the sprint", "done", date(2026, 11, 12)),
        ]

    def test_without_filters_preserves_order_and_undated_tasks(self):
        self.assertEqual(filter_tasks(iter(self.tasks)), self.tasks)

    def test_status_only_includes_matching_undated_tasks(self):
        self.assertEqual(
            filter_tasks(self.tasks, status="todo"),
            [self.tasks[0], self.tasks[2], self.tasks[3]],
        )

    def test_date_bounds_are_inclusive_and_exclude_undated_tasks(self):
        self.assertEqual(
            filter_tasks(self.tasks, due_from=date(2026, 11, 13), due_to=date(2026, 11, 15)),
            self.tasks[:3],
        )

    def test_status_and_dates_must_both_match(self):
        self.assertEqual(
            filter_tasks(self.tasks, status="todo", due_to=date(2026, 11, 14)),
            [self.tasks[0]],
        )

    def test_no_matches_returns_empty_list(self):
        self.assertEqual(filter_tasks(self.tasks, due_from=date(2026, 11, 16)), [])

    def test_reversed_date_range_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "due-from must be on or before due-to"):
            filter_tasks(self.tasks, due_from=date(2026, 11, 15), due_to=date(2026, 11, 13))

    def test_unknown_status_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "status must be one of"):
            filter_tasks(self.tasks, status="pending")


class CommandLineTests(unittest.TestCase):
    def run_cli(self, raw_json, *arguments):
        script = Path(__file__).with_name("task_filter.py").resolve()
        with TemporaryDirectory() as directory:
            input_path = Path(directory) / "tasks.json"
            input_path.write_text(raw_json, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(script), str(input_path), *arguments],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_outputs_only_matching_json_records(self):
        tasks = [
            {"title": "Write tests", "status": "todo", "due_date": "2026-11-13"},
            {"title": "Plan the sprint", "status": "done", "due_date": "2026-11-13"},
        ]
        result = self.run_cli(json.dumps(tasks), "--status", "todo")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), tasks[:1])
        self.assertEqual(result.stderr, "")

    def test_bad_record_reports_row_number_and_no_partial_output(self):
        result = self.run_cli(
            '[{"title":"Write tests","status":"todo"},'
            '{"title":"Review the PR","status":"todo","due_date":"2026-02-30"}]'
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("task 2: due_date must be a valid calendar date", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_date_flags_require_exact_iso_format(self):
        result = self.run_cli("[]", "--due-to", "20261113")
        self.assertEqual(result.returncode, 2)
        self.assertIn("--due-to must use YYYY-MM-DD format", result.stderr)


if __name__ == "__main__":
    unittest.main()
