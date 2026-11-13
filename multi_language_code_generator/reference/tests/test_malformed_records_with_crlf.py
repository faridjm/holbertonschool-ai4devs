import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class MalformedRecordsWithCrlfTests(LogAnalyzerTestCase, unittest.TestCase):
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
