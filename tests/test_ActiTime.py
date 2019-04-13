import os
import pytest
import time
from pages.loginpage import LoginPage
from pages.userpage import UserPage
from pages.edit_userpage import EditUserPage
path = os.getcwd().replace("tests", "").replace("\\", "/") + "drivers/chromedriver.exe"

@pytest.mark.usefixtures("test_launch_browser")
class TestActiTime:

    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

#    def test_userAction(self):
#        driver = self.driver
#        kp = UserPage(driver)
#        kp.click_user()
#        kp.enter_first_name()
#        kp.enter_user_name()
#        kp.enter_last_name()
#        kp.enter_pwd()
#        kp.enter_email()
#        kp.enter_reenter_pwd()
#        time.sleep(10)
#        kp.click_on_create_user()

    def test_edit_user(self):
        driver = self.driver
        mp = EditUserPage(driver)
        mp.click_users_menu()
        mp.search_user()
        time.sleep(20)
        mp.click_opened_user()
        mp.change_first_name()
        time.sleep(20)
        mp.click_on_SaveChanges

