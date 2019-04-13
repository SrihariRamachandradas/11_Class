class EditUserPage:

    def __init__(self, driver):
        self.driver = driver
        self.click_on_userslink = '//*[@id="topnav"]/tbody/tr[1]/td[9]/a/div[1]'
        self.search_for_user = 'userNameInput'
        self.click_on_opened_user = '//span[@class="userNameSpan"]'
        self.FN_text_bx_id = 'userDataLightBox_firstNameField'
        self.click_on_SaveChanges = '//span[@class="buttonTitle"]'

    def click_users_menu(self):
        self.driver.find_element_by_xpath(self.click_on_userslink).click()

    def search_user(self):
        self.driver.find_element_by_id(self.search_for_user).send_keys("System")

    def click_opened_user(self):
        self.driver.find_element_by_xpath(self.click_on_opened_user).click()

    def change_first_name(self):
        self.driver.find_element_by_id(self.FN_text_bx_id).clear()
        self.driver.find_element_by_id(self.FN_text_bx_id).send_keys("TestK")

    def click_savechanges(self):
        self.driver.find_element_by_xpath(self.click_on_SaveChanges).click()


