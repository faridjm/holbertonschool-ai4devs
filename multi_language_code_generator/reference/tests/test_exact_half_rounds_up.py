import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class ExactHalfRoundsUpTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_exact_half_rounds_up(self):
        self.assert_summary(
            "c1\tGET\t/items\t200\n" * 31 + "c1\tGET\t/items\t500",
            requests=32,
            clients=1,
            errors=1,
            error_rate=3.13,
            endpoints=(("GET", "/items", 32, 1),),
        )
