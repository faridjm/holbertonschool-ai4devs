# Pull Request: Add Task Filtering by Status and Due Date

## Summary

Add a Python CLI and a reusable filtering function that return tasks matching a status, an inclusive due-date range, or both.

## Changes

- Read a UTF-8 JSON array of tasks and write matching records to standard output as JSON.
- Support `todo`, `in_progress`, and `done` with the `--status` option. Support either date boundary independently through `--due-from` and `--due-to`.
- Keep input order. Include undated tasks in status-only searches and exclude them when a date boundary is supplied.
- Report invalid dates, reversed ranges, and malformed input on standard error with exit code 2.
- Add 10 automated tests covering the filtering rules and the CLI.

## Context

A task list can mix finished work, upcoming deadlines, and undated items. Filtering helps users find the work they need to review. This standalone feature provides a small diff for the AI code review exercise. There is no linked issue.

## Usage

Save a JSON array such as the following to `tasks.json`:

```json
[
  { "title": "Write tests", "status": "todo", "due_date": "2026-11-13" },
  { "title": "Review the PR", "status": "in_progress", "due_date": "2026-11-14" }
]
```

From the repository root, run:

```bash
python3 ai_code_review_simulator/task_filter.py tasks.json --status todo --due-to 2026-11-13
```

## Verification

```bash
python3 -m unittest discover -s ai_code_review_simulator -v
(cd multi_language_code_generator && python3 -m unittest discover -s reference/tests -v)
```
