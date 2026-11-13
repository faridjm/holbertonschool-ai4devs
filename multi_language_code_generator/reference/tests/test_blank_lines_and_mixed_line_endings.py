import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class BlankLinesAndMixedLineEndingsTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_blank_lines_and_mixed_line_endings(self):
        self.assert_summary("\r\n \t \n\t\r\n  ")
