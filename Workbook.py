from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
driver.get("https://na2-app.euvantage.com/Account/Login?clientCode=Anunta")
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='username']").send_keys("vikkrams")
driver.find_element_by_xpath("//div[3]/div/input[@id='pwd']").send_keys("pass@123")
driver.find_element_by_xpath("//button[@id='btnSubmit']").click()
time.sleep(20)
print(driver.current_url)
driver.find_element_by_xpath("//body/div[@id='main-wrapper']/div[@id='main-navbar']/button[2]/i[1]").click()
time.sleep(10)
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//div[@class='col-md-12 main-menu-content']/div[5]")).perform()
WebElement_Menu = driver.find_element_by_xpath(
    "//div[@class='col-md-12']//div[@class='col-md-12 sub-menu-content']/div[9]")
WebElement_SubMenu = driver.find_element_by_xpath(
    "//div[@class='col-md-12']//div[@class='col-md-12 sub-menu-content']/div[9]")
action.move_to_element(WebElement_Menu).perform()
action.move_to_element(WebElement_SubMenu).perform()
action.click(WebElement_SubMenu).perform()
print("Current Page" + driver.current_url)
print("Title" + driver.title)
time.sleep(10)
userPage = driver.current_url
locTitle = driver.title
print(userPage)
print("Title" + locTitle)
if userPage == "https://na2-app.euvantage.com/Analytic/UserDuration":
    assert True, "Passed"
else:
    assert False, "Failed"
DropDown1 = Select(driver.find_element_by_xpath("//form//div[@class='col-md-12']//div[@class='form-inline']/select[1]"))
DropDown1.select_by_value('80')
time.sleep(10)
dropDown2 = Select(driver.find_element_by_xpath(
    "//form//div[@class='col-md-12']//div[@class='form-inline']/select[@id='period']"))
dropDown2.select_by_value('5')
time.sleep(10)
driver.find_element_by_xpath("//div//button[@class='btn btn-primary btn-xs btn-labeled']").click()
time.sleep(10)
poolName = '//input[@id="PoolNameTxt"]'
serverName = '//input[@id="HostName_txt"]'
userName = '//div[@class="col-md-2"]//span/input[@id="sourceIPAPPTxt"]'
driver.find_element_by_xpath(poolName).click()
driver.find_element_by_xpath(poolName).send_keys("My_Desktop_IGSDBU_Voice")
time.sleep(5)
driver.find_element_by_xpath(serverName).click()
driver.find_element_by_xpath(serverName).send_keys("TPIGSDBUV3-0.intelenetglobal.com")
driver.find_element_by_xpath(userName).click()
driver.find_element_by_xpath(userName).send_keys("INTELENETGLOBAL\100000000467670")
driver.implicitly_wait(driver,20)

