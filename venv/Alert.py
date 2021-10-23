from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
driver.get("http://www.maths.surrey.ac.uk/explore/nigelspages/frame2.htm")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame(driver.find_element_by_xpath("//frameset[1]/frame[2]"))
driver.find_element_by_name("name").send_keys("Bharani")
driver.execute_script("window.scrollTo(0,1000);")
driver.save_screenshot("C:/Users/bhara/PycharmProjects/untitled/venv/Scripts/Snapshot1.png")
time.sleep(5)
driver.switch_to.parent_frame()
print(driver.title)
driver.switch_to.frame(driver.find_element_by_xpath("//frameset[1]/frame[1]"))
print("Crossed")
#driver.find_element_by_xpath("//a[contains(text(),'Background')]").click()
time.sleep(5)
#driver.execute_script("window.scrollTo(0,1000);")
frame=driver.find_element_by_xpath("//a[contains(text(),'Quizzes')]")
driver.execute_script("arguments[0].scrollIntoView();",frame)
driver.save_screenshot("C:/Users/bhara/PycharmProjects/untitled/venv/Scripts/Snapshot2.png")
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element_by_xpath("//frameset[1]/frame[3]"))
driver.execute_script("window.scrollTo(0,5000);")
driver.save_screenshot("C:/Users/bhara/PycharmProjects/untitled/venv/Scripts/Snapshot3.png")





'''
#Alerts
option=webdriver.ChromeOptions()
option.add_argument("-incognito")
driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver',chrome_options=option)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element_by_xpath("//button[contains(text(),'Click for JS Alert')]").click()
alert=driver.switch_to.alert
alert_text=alert.text
alert.accept()
print(alert_text)

driver.find_element_by_xpath("//button[contains(text(),'Click for JS Confirm')]").click()
prompt_alert=driver.switch_to.alert
alert_text1=prompt_alert.text
prompt_alert.dismiss()
print(alert_text1)

driver.find_element_by_xpath("//button[contains(text(),'Click for JS Prompt')]").click()
prompt_alert=driver.switch_to.alert
alert_text2=prompt_alert.text
prompt_alert.send_keys("Hello alert")
prompt_alert.accept()
print(alert_text2)
---------------------------------------------------------------------------
#Chrome options
options=webdriver.ChromeOptions()
options.add_argument("-incognito")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver',chrome_options=options)
driver.get("https://www.fabhotels.com/contact-us")
driver.maximize_window()
'''

