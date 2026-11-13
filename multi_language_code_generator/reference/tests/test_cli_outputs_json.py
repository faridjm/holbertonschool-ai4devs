import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


class CliOutputsJsonTests(unittest.TestCase):
    def test_cli_outputs_json(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "sample access.log"
            path.write_bytes(b"c1\tPOST\t/orders\t500\r\n")
            script = Path(__file__).resolve().parents[1] / "log_analyzer.py"
            result = subprocess.run(
                [sys.executable, str(script), str(path)],
                check=True,
                capture_output=True,
                text=True,
            )

        self.assertEqual(
            json.loads(result.stdout),
            {
                "totalRequests": 1,
                "uniqueClients": 1,
                "errorRequests": 1,
                "errorRatePercent": 100,
                "malformedLines": 0,
                "endpoints": [
                    {"method": "POST", "path": "/orders", "requestCount": 1, "errorCount": 1},
                ],
            },
        )
        self.assertEqual(result.stderr, "")
