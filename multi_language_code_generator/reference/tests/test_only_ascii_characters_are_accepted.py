import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class OnlyAsciiCharactersAreAcceptedTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_only_ascii_characters_are_accepted(self):
        self.assert_summary(
            "cliënt\tGET\t/products\t200\n"
            "c1\tGET\t/café\t200\n"
            "c1\tGET\t/products\t２０0\n"
            "\u00a0\n",
            malformed=4,
        )
