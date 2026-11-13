import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class MixedTrafficAndRepeatedClientsTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_mixed_traffic_and_repeated_clients(self):
        self.assert_summary(
            "c1\tGET\t/products\t200\n"
            "c1\tGET\t/products\t404\n"
            "c2\tPOST\t/orders\t201\n"
            "c3\tGET\t/products\t503\n"
            "c2\tGET\t/orders\t302\n",
            requests=5,
            clients=3,
            errors=2,
            error_rate=40,
            endpoints=(
                ("GET", "/products", 3, 2),
                ("GET", "/orders", 1, 0),
                ("POST", "/orders", 1, 0),
            ),
        )
