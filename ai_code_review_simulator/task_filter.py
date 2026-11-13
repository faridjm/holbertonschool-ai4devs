"""Filter a JSON array of tasks by status and inclusive due-date bounds."""

import argparse
import json
import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from pathlib import Path


STATUSES = ("todo", "in_progress", "done")
ISO_DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


def parse_date(value: object, field: str) -> date:
    if not isinstance(value, str) or ISO_DATE.fullmatch(value) is None:
        raise ValueError(f"{field} must use YYYY-MM-DD format")
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{field} must be a valid calendar date") from error


@dataclass(frozen=True)
class Task:
    title: str
    status: str
    due_date: date | None = None

    @classmethod
    def from_record(cls, record: object) -> "Task":
        if not isinstance(record, dict):
            raise ValueError("expected an object")

        title = record.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")

        status = record.get("status")
        if status not in STATUSES:
            raise ValueError(f"status must be one of: {', '.join(STATUSES)}")

        raw_due_date = record.get("due_date")
        due_date = None if raw_due_date is None else parse_date(raw_due_date, "due_date")
        return cls(title=title, status=status, due_date=due_date)

    def to_record(self) -> dict[str, str | None]:
        return {
            "title": self.title,
            "status": self.status,
            "due_date": self.due_date.isoformat() if self.due_date is not None else None,
        }


def filter_tasks(
    tasks: Iterable[Task],
    *,
    status: str | None = None,
    due_from: date | None = None,
    due_to: date | None = None,
) -> list[Task]:
    """Return matching tasks in input order. Date bounds include their endpoints."""
    if status is not None and status not in STATUSES:
        raise ValueError(f"status must be one of: {', '.join(STATUSES)}")
    if due_from is not None and due_to is not None and due_from > due_to:
        raise ValueError("due-from must be on or before due-to")

    matches = []
    has_date_filter = due_from is not None or due_to is not None
    for task in tasks:
        if status is not None and task.status != status:
            continue
        if task.due_date is None:
            if has_date_filter:
                continue
        else:
            if due_from is not None and task.due_date < due_from:
                continue
            if due_to is not None and task.due_date > due_to:
                continue
        matches.append(task)
    return matches


def load_tasks(path: Path) -> list[Task]:
    records = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("task file must contain a JSON array")

    tasks = []
    for row_number, record in enumerate(records, start=1):
        try:
            tasks.append(Task.from_record(record))
        except ValueError as error:
            raise ValueError(f"task {row_number}: {error}") from error
    return tasks


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON file containing an array of tasks")
    parser.add_argument("--status", choices=STATUSES)
    parser.add_argument("--due-from", metavar="YYYY-MM-DD", help="inclusive earliest date")
    parser.add_argument("--due-to", metavar="YYYY-MM-DD", help="inclusive latest date")
    args = parser.parse_args(argv)

    try:
        due_from = parse_date(args.due_from, "--due-from") if args.due_from is not None else None
        due_to = parse_date(args.due_to, "--due-to") if args.due_to is not None else None
        tasks = load_tasks(args.input)
        matches = filter_tasks(tasks, status=args.status, due_from=due_from, due_to=due_to)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(json.dumps([task.to_record() for task in matches], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
