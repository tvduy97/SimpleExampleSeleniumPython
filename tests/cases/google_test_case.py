import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../..'))

import unittest
from selenium.webdriver.common.keys import Keys
from tests.commons.chrome_test_case import ChromeTestCase


class GoogleTestCaseSimple(ChromeTestCase):
    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def testSearchSomeThing(self):
        self.browser.get('https://www.google.com')
        self.assertIn('Google', self.browser.title)
        element = self.browser.find_element_by_name('q')
        element.send_keys('seleniumhq' + Keys.RETURN)
        self.assertIn('seleniumhq', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
