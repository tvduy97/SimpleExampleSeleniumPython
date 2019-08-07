import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../..'))

import unittest
from tests.cases.google_test_case import GoogleTestCase


class TestSuite1(unittest.TestCase):
    def test_main(self):
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(GoogleTestCase),

        ])
        unittest.TextTestRunner()


if __name__ == "__main__":
    unittest.main(verbosity=2)
