import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class AllRecordsMalformedTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_all_records_malformed(self):
        self.assert_summary(
            "c1\tGET\t/status\t099\n\tGET\t/status\t200\nc3\tGET\tstatus\t200\n",
            malformed=3,
        )
