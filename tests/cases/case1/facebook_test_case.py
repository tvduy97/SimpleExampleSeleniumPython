import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../../..'))

import unittest
from tests.commons.chrome_test_case import ChromeTestCase
import constants as cts


class FacebookTestCase(ChromeTestCase):
    def setUp(self):
        ChromeTestCase.setUp(self)
        self.url = cts.URL

    def testLoginFailed(self):
        self.loginAction('example123456@example.com', 'example123456')
        error_message = self.browser.find_element_by_xpath('//*[@id="globalContainer"]/div[3]/div/div/div').text
        self.assertEqual(error_message, error_message)

    def loginAction(self, email, password):
        self.browser.get(self.url)
        self.assertIn('Facebook', self.browser.title)
        email_input = self.browser.find_element_by_id('email')
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.browser.find_element_by_id('pass')
        password_input.clear()
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_id('u_0_2')
        login_button.click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
