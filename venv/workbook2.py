import unittest
from selenium import webdriver
import HtmlTestRunner
import time


class FaceBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
        cls.driver.maximize_window()

    def test_LoginPage(self):
        self.driver.get("https://www.facebook.com/")

    def test_Logindetails(self):
        self.driver.find_element_by_xpath("//input[@id='email']").clear()
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("bharanirocks15@gmail.com")
        self.driver.find_element_by_xpath("//input[@id='pass']").clear()
        self.driver.find_element_by_xpath("//input[@id='pass']").send_keys("Welcome@123")
        time.sleep(5)

    def test_Submit(self):
        self.driver.find_element_by_xpath("//button[@name='login']").click()

    @classmethod
    def tearDownclass(self):
        a=self.driver.title()
        print(a)
        if a==self.driver.title:
            assert True

if __name__== "__main__":
    HtmlTestRunner.main()
    #unittest.main()

        #(testRunner=HtmlTestRunner.HtmlTestRunner(output='..\\report'))

