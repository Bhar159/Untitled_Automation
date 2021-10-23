from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import*
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.current_window_handle)
print(driver.title)
driver.find_element_by_xpath("//ul[@class='makeFlex font12']/li//a[@class='active makeFlex hrtlCenter column']").click()
driver.find_element_by_xpath("//div[@class='makeFlex']//ul/li[2]").click()
driver.find_element_by_xpath("//span[contains(text(),'From')]").click()
driver.find_element_by_xpath("//div[@class='hsw_autocomplePopup autoSuggestPlugin']/div/input").send_keys("Chennai"+Keys.DOWN)
actionkeys1 = ActionChains(driver)
time.sleep(5)
actionkeys1.send_keys(Keys.ENTER).perform()

waiting=WebDriverWait(driver,10)
waiting.until(ec.title_contains(By.XPATH('')))

'''
a=0
while a<=1:
    actionkeys = ActionChains(driver)
    actionkeys.key_down(Keys.ARROW_DOWN).perform()
    a=a+1

driver.find_element_by_xpath("//div[@class='hsw_autocomplePopup autoSuggestPlugin']/div/input").send_keys(Keys.ENTER)


for x in range(4):
    if x==1 or x==2:
        actionkeys=ActionChains(driver)
        actionkeys.key_down(Keys.ARROW_DOWN).perform()
        if x==3:
            actionkeys1 = ActionChains(driver)
            time.sleep(5)
            actionkeys1.send_keys(Keys.ENTER).perform()
'''
driver.find_element_by_xpath("//span[contains(text(),'To')]").click()
driver.find_element_by_xpath("//div[@class='hsw_autocomplePopup autoSuggestPlugin']/div/input").click()
scroll=driver.find_element_by_xpath("//div[@id='react-autowhatever-1']/div/ul/li[6]")
driver.execute_script("arguments[0].scrollIntoView();",scroll)
actionkeys2=ActionChains(driver)
actionkeys2.click(scroll).perform()

driver.find_element_by_xpath("//span[contains(text(),'DEPARTURE')]").click()
driver.find_element_by_xpath("//div[@class='DayPicker-Months']/div[1]/div[3]/div[4]/div[5]").click()

for change in range(3):
    driver.find_element_by_xpath("//div[@class='DayPicker-wrapper']/div/span[2]").click()

driver.find_element_by_xpath("//div[@class='DayPicker-Months']/div[2]/div[3]/div[3]/div[2]").click()
driver.find_element_by_xpath("//a[contains(text(),'Search')]").click()
time.sleep(5)
#explicite wait
#driver.find_element_by_xpath("//div[@class='fli-intl-rhs pull-left start ']/div[1]/div/div/div/span[2]").click()
#wait=WebDriverWait(driver,10)
#element=wait.until(ec.element_to_be_clickable((By.XPATH,"//div[@class='fli-intl-rhs pull-left start ']/div[2]/div/div/div/span[3]")))
#element.click()
print(driver.current_window_handle)
print(driver.title)
driver.find_element_by_xpath("//header/div[@id='search-widget']/div[1]/div[3]/div[1]").click()

driver.find_element_by_xpath("//button[@id='search-button']").click()
print("Done")
print(driver.current_url)
print(driver.title)

driver.find_element_by_xpath("//button[contains(text(),'Book Now')]").click()
b=driver.find_element_by_xpath("//div[@class='multifareOuter']/div[2]")
c3=driver.find_element_by_xpath("//div[@class='multifareOuter']/div[2]/div[2]")
#driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",b)
driver.execute_script("arguments[0].scrollIntoView();",c3)
time.sleep(5)
#driver.find_element_by_xpath("//div[@class='multifareOuter']/div[3]/button").click()
#driver.save_screenshot("D:\Selenium\makemytrip.png")
time.sleep(5)
#action2=ActionChains(driver)
#action2.context_click(c3).perform()
#action2.context_click(driver.find_element_by_xpath("//p[contains(text(),'Thu 15 Apr')]")).perform()

print("Done DOne D0Ne")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//button[contains(text(),'Continue')]").click()
time.sleep(5)
print(driver.current_url)
print(driver.title)
print(driver.title)
driver.switch_to_window(driver.window_handles[1])
driver.execute_script("window.scrollTo(0,5000);")
print(driver.title)

#action4=ActionChains(driver)
#action4.context_click(driver.find_element_by_xpath("//p[contains(text(),'RETURN')]")).perform()
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_xpath("//button[contains(text(),'Continue')]").click()
driver.switch_to_window(driver.window_handles[2])
print(driver.title)
print("Mission Completed")
driver.switch_to_window(driver.window_handles[0])
for x in range(4):
    driver.back()

print(driver.title)

driver.forward()
driver.refresh()

print("Below items are performed","\n Refresh \t Back \t forward")







