import argparse
import json
import re
from collections import Counter
from collections.abc import Iterable
from pathlib import Path

CLIENT_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]+")
METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}
PATH_PATTERN = re.compile(r"/(?:[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*)?")
STATUS_PATTERN = re.compile(r"[1-5][0-9]{2}")


def _parse_record(record: str) -> tuple[str, str, str, int] | None:
    fields = record.split("\t")
    if len(fields) != 4:
        return None

    client_id, method, path, status = fields
    if (
        not CLIENT_ID_PATTERN.fullmatch(client_id)
        or method not in METHODS
        or not PATH_PATTERN.fullmatch(path)
        or not STATUS_PATTERN.fullmatch(status)
    ):
        return None

    return client_id, method, path, int(status)


def _error_rate_percent(errors: int, total: int) -> int | float:
    if total == 0:
        return 0

    # Work in hundredths of a percent to round ties exactly.
    hundredths, remainder = divmod(errors * 10_000, total)
    if remainder * 2 >= total:
        hundredths += 1
    return hundredths / 100


def analyze(lines: Iterable[str]) -> dict[str, object]:
    """Summarize access-log lines, including any LF or CRLF terminators."""
    clients: set[str] = set()
    requests_by_endpoint: Counter[tuple[str, str]] = Counter()
    errors_by_endpoint: Counter[tuple[str, str]] = Counter()
    total_requests = 0
    error_requests = 0
    malformed_lines = 0

    for line in lines:
        record = line.removesuffix("\r\n") if line.endswith("\r\n") else line.removesuffix("\n")
        if not record.strip(" \t"):
            continue

        parsed = _parse_record(record)
        if parsed is None:
            malformed_lines += 1
            continue

        client_id, method, path, status = parsed
        endpoint = (method, path)
        clients.add(client_id)
        total_requests += 1
        requests_by_endpoint[endpoint] += 1
        if status >= 400:
            error_requests += 1
            errors_by_endpoint[endpoint] += 1

    ordered_endpoints = sorted(
        requests_by_endpoint,
        key=lambda endpoint: (-requests_by_endpoint[endpoint], endpoint),
    )
    endpoints = [
        {
            "method": method,
            "path": path,
            "requestCount": requests_by_endpoint[method, path],
            "errorCount": errors_by_endpoint[method, path],
        }
        for method, path in ordered_endpoints
    ]
    return {
        "totalRequests": total_requests,
        "uniqueClients": len(clients),
        "errorRequests": error_requests,
        "errorRatePercent": _error_rate_percent(error_requests, total_requests),
        "malformedLines": malformed_lines,
        "endpoints": endpoints,
    }


def analyze_file(path: str | Path) -> dict[str, object]:
    """Read a UTF-8 log one line at a time and return its summary."""
    with open(path, encoding="utf-8", newline="\n") as log_file:
        return analyze(log_file)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a UTF-8 API access log.")
    parser.add_argument("log_file", type=Path, help="path to the tab-separated log file")
    args = parser.parse_args()

    try:
        summary = analyze_file(args.log_file)
    except (OSError, UnicodeError) as error:
        parser.exit(1, f"{parser.prog}: {error}\n")

    print(json.dumps(summary))


if __name__ == "__main__":
    main()
