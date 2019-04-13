from utils.constants import *

class UserPage:

    def __init__(self, driver):
        self.driver = driver
        self.click_on_userslink = '//*[@id="topnav"]/tbody/tr[1]/td[9]/a/div[1]'
        self.click_on_users = ('//span[text()="User"]')
        self.FN_text_bx_id = 'userDataLightBox_firstNameField'
        self.UN_text_bx_id = 'userDataLightBox_usernameField'
        self.LN_text_bx_id = 'userDataLightBox_lastNameField'
        self.pwd1_text_bx_id = 'userDataLightBox_passwordField'
        self.email_text_bx_id = 'userDataLightBox_emailField'
        self.pwd2_text_bx_id = 'userDataLightBox_passwordCopyField'
        self.create_user_btn_xpath = ('//span[text()="Create User"]')

    def click_users_menu(self):
        self.driver.find_element_by_xpath(self.click_on_userslink).click()

    def click_user(self):
        self.driver.find_element_by_xpath(self.click_on_users).click()

    def enter_first_name(self):
        self.driver.find_element_by_id(self.FN_text_bx_id).send_keys(FIRST_NAME)

    def enter_user_name(self):
        self.driver.find_element_by_id(self.UN_text_bx_id).send_keys(USNAME)

    def enter_last_name(self):
        self.driver.find_element_by_id(self.LN_text_bx_id).send_keys(LAST_NAME)

    def enter_pwd(self):
        self.driver.find_element_by_id(self.pwd1_text_bx_id).send_keys(PWD1)

    def enter_email(self):
        self.driver.find_element_by_id(self.email_text_bx_id).send_keys(EMAIL)

    def enter_reenter_pwd(self):
        self.driver.find_element_by_id(self.pwd2_text_bx_id).send_keys(REENTERPWD1)

    def click_on_create_user(self):
        self.driver.find_element_by_xpath(self.create_user_btn_xpath).click()

