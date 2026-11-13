                ("POST", "/orders", 1, 0),
            ),
        )

    def test_malformed_records_with_crlf(self):
        self.assert_summary(
            "\r\n \t \r\n"
            "c1\tGET\t/health\t200\r\n"
            "missing-fields\r\n"
            "c2\tget\t/health\t200\r\n"
            "c3\tGET\t/health?full=1\t200\r\n"
            "c4\tGET\t/health\t600\r\n"
            "c5\tGET\t/health\t 200\r\n"
            "c6\tGET\t/health\t200\textra",
            requests=1,
            clients=1,
            malformed=6,
            endpoints=(("GET", "/health", 1, 0),),
        )

    def test_duplicates_and_case_sensitive_clients_and_paths(self):
        self.assert_summary(
            "u1\tPOST\t/items\t200\n"
            "U1\tGET\t/items\t200\n"
            "u1\tGET\t/Items\t200\n"
            "u1\tGET\t/items\t200\n"
            "u1\tGET\t/items\t200\n",
            requests=5,
            clients=2,
            endpoints=(
                ("GET", "/items", 3, 0),
                ("GET", "/Items", 1, 0),
                ("POST", "/items", 1, 0),
            ),
        )

    def test_error_boundaries_and_fractional_percentage(self):
        self.assert_summary(
            "c1\tGET\t/\t399\nc2\tGET\t/\t400\nc3\tGET\t/\t599\n",
            requests=3,
            clients=3,
            errors=2,
            error_rate=66.67,
            endpoints=(("GET", "/", 3, 2),),
        )

    def test_all_records_malformed(self):
        self.assert_summary(
            "c1\tGET\t/status\t099\n\tGET\t/status\t200\nc3\tGET\tstatus\t200\n",
            malformed=3,
        )

    def test_endpoint_ties_sorted_by_ascii_path(self):
        self.assert_summary(
            "c1\tGET\t/z\t100\nc1\tGET\t/a\t200\nc1\tGET\t/A\t200",
            requests=3,
            clients=1,
            endpoints=(("GET", "/A", 1, 0), ("GET", "/a", 1, 0), ("GET", "/z", 1, 0)),
        )

    def test_blank_lines_and_mixed_line_endings(self):
        self.assert_summary("\r\n \t \n\t\r\n  ")

    def test_only_ascii_characters_are_accepted(self):
        self.assert_summary(
            "cliënt\tGET\t/products\t200\n"
            "c1\tGET\t/café\t200\n"
            "c1\tGET\t/products\t２０0\n"
            "\u00a0\n",
            malformed=4,
        )

    def test_invalid_path_segments_and_trailing_slashes(self):
        self.assert_summary(
            "c1\tHEAD\t/api_v1/my-file.json\t204\n"
            "c1\tHEAD\t/api_v1//items\t204\n"
            "c1\tHEAD\t/api_v1/\t204\n"
            "c1\tHEAD\t/api_v1#items\t204\n",
            requests=1,
            clients=1,
            malformed=3,
            endpoints=(("HEAD", "/api_v1/my-file.json", 1, 0),),
        )

    def test_exact_half_rounds_up(self):
        self.assert_summary(
            "c1\tGET\t/items\t200\n" * 31 + "c1\tGET\t/items\t500",
            requests=32,
            clients=1,
            errors=1,
            error_rate=3.13,
            endpoints=(("GET", "/items", 32, 1),),
        )

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


if __name__ == "__main__":
    unittest.main()
