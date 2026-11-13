import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class DuplicatesAndCaseSensitiveClientsAndPathsTests(LogAnalyzerTestCase, unittest.TestCase):
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
