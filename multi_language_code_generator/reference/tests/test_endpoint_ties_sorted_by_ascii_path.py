import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class EndpointTiesSortedByAsciiPathTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_endpoint_ties_sorted_by_ascii_path(self):
        self.assert_summary(
            "c1\tGET\t/z\t100\nc1\tGET\t/a\t200\nc1\tGET\t/A\t200",
            requests=3,
            clients=1,
            endpoints=(("GET", "/A", 1, 0), ("GET", "/a", 1, 0), ("GET", "/z", 1, 0)),
        )
