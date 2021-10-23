from behave import *
from selenium import webdriver
import time
import Seleniumbehave.Pagemodel.loginpage.py

#C:\Users\bhara\PycharmProjects\untitled\Seleniumbehave



@given('Username')
def step_impl1(self):
    self.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
    driver = self.driver
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    login =LocElement(self.driver)
    login.enter_username("vikkrams")


@when('password')
def step_impl2(self):
    login2=LocElement(self.driver)
    login2.enter_password("pass@123")


@then('User logged in')
def step_impl3(context):
    login3=LocElement(self.driver)
    login3.click_login()


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
