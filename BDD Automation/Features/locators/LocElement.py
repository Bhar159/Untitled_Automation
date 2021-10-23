class Locators():

    def loginpage2(self,driver):
        self.driver = driver

        self.username_textbox_xpath="//input[@id='username']"
        self.password_textbox_xpath="//div[3]/div/input[@id='pwd']"
        self.login_button_xpath="//button[@id='btnSubmit']"
        self.invalid_message="//span[contains(text(),'Username or password provided is incorrect.')]"

    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()