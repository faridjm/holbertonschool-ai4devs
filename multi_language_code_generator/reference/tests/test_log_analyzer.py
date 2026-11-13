import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class EmptyFileTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_empty_file(self):
        self.assert_summary("")
