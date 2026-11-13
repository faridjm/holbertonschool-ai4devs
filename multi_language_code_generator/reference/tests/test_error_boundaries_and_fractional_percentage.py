import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class ErrorBoundariesAndFractionalPercentageTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_error_boundaries_and_fractional_percentage(self):
        self.assert_summary(
            "c1\tGET\t/\t399\nc2\tGET\t/\t400\nc3\tGET\t/\t599\n",
            requests=3,
            clients=3,
            errors=2,
            error_rate=66.67,
            endpoints=(("GET", "/", 3, 2),),
        )
