from selenium import webdriver
import time
import os
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
path = os.getcwd().replace("tests", "").replace("\\", "/") + "drivers/chromedriver.exe"

@pytest.mark.usefixtures("test_launch_browser")
class TestLogin:

    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

        # driver.find_element_by_name("username").send_keys("admin")
        # driver.find_element_by_name("pwd").send_keys("manager")
        # driver.find_element_by_id("loginButton").click()

    def test_logout(self):
        driver = self.driver
        time.sleep(5)
        hp = HomePage(driver)
        hp.click_on_logout()
        # driver.find_element_by_id("logoutLink").click()
