import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../../..'))

import unittest
from tests.cases.case1.facebook_test_case import FacebookTestCase


class FacebookTestSuite(unittest.TestCase):
    def test_main(self):
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FacebookTestCase),

        ])
        unittest.TextTestRunner()


if __name__ == "__main__":
    unittest.main(verbosity=2)
