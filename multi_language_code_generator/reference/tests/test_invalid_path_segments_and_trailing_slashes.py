import unittest

from log_analyzer_test_support import LogAnalyzerTestCase


class InvalidPathSegmentsAndTrailingSlashesTests(LogAnalyzerTestCase, unittest.TestCase):
    def test_invalid_path_segments_and_trailing_slashes(self):
        self.assert_summary(
            "c1\tHEAD\t/api_v1/my-file.json\t204\n"
            "c1\tHEAD\t/api_v1//items\t204\n"
            "c1\tHEAD\t/api_v1/\t204\n"
            "c1\tHEAD\t/api_v1#items\t204\n",
            requests=1,
            clients=1,
            malformed=3,
            endpoints=(("HEAD", "/api_v1/my-file.json", 1, 0),),
        )
