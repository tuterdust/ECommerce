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

        
        signuplink = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("SIGN UP"))

        signuplink.click()

        strEmail = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_email"))
        strEmail.send_keys("someone@gmail.com");
        strPass = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_password"))
        strPass.send_keys("12345678");
        strPassConfirm = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_confirm_password"))
        strPassConfirm.send_keys("12345678");
        strName = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_firstname"))
        strName.send_keys("Some");
        strLastName = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_lastname"))
        strLastName.send_keys("One");
        strAddress = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_address"))
        strAddress.send_keys("SomePlace");

        btnsubmit = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/center/form/div[2]/div[2]/input"))
        btnsubmit.click()

        signinlink = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("SIGN IN"))
        signinlink.click()

        inEmail = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_email"))
        inEmail.send_keys("someone@gmail.com");
        inPass = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("id_password"))
        inPass.send_keys("12345678");

        btnsignin = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/center/div/div[2]/form/input[2]"))
        btnsignin.click()

        signoutlink = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("SIGN OUT"))
        signoutlink.click()

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/center/h1/b"))
                
        time.sleep(8)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

