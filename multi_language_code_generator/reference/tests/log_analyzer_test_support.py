from pathlib import Path
from tempfile import TemporaryDirectory

from reference.log_analyzer import analyze_file


class LogAnalyzerTestCase:
    def assert_summary(
        self,
        log: str,
        *,
        requests: int = 0,
        clients: int = 0,
        errors: int = 0,
        error_rate: int | float = 0,
        malformed: int = 0,
        endpoints: tuple[tuple[str, str, int, int], ...] = (),
    ) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "access.log"
            path.write_bytes(log.encode("utf-8"))
            summary = analyze_file(path)

        self.assertEqual(
            summary,
            {
                "totalRequests": requests,
                "uniqueClients": clients,
                "errorRequests": errors,
                "errorRatePercent": error_rate,
                "malformedLines": malformed,
                "endpoints": [
                    {
                        "method": method,
                        "path": path,
                        "requestCount": request_count,
                        "errorCount": error_count,
                    }
                    for method, path, request_count, error_count in endpoints
                ],
            },
        )
