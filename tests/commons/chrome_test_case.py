import unittest
from selenium import webdriver
import constants as cts


class ChromeTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--Tests-type")
        options.add_argument('--disable-features=NetworkService')
        self.browser = webdriver.Chrome(executable_path=cts.CHROME_DRIVER_PATH, chrome_options=options)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.close()
