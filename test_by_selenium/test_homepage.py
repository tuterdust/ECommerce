import time
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("localhost:8000")
        
    def test_Login(self):
        driver = self.driver
        print(driver.title)

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("PROFILE"))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("CART"))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("SIGN IN"))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("SIGN UP"))

        time.sleep(8)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

