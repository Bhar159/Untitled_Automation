
from behave import *
from selenium import webdriver
import time



@given('Useranme')
def step_impl1(self,driver):
    self.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
    driver=self.driver
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    login=LoginPage2(driver)

@when('password')
def step_impl2(self):
    login.enter_password("pass@123")


@then('User logged in')
def step_impl3(context):
    login.click_login()
'''
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        driver=self.driver
        driver.get("https://na2-app.euvantage.com/Account/Login?clientCode=Anunta")
        login=LoginPage(driver)
        login.enter_username("vikkrams")
        login.enter_password("pass@123")
        login.click_login()
        time.sleep(10)
        
        '''
