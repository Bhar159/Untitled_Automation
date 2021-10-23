from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.keys import Keys


#######################   Health_Check  ######################
from selenium.webdriver.support.wait import WebDriverWait
#Travel place
driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
driver.get("https://www.booking.com/")
#driver.get("https://www.booking.com/hotel/mx/san-marino-suites.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AtD18YUGwAIB0gIkOTE3MmYyYzktMWVlNy00MDk5LWFiNjItMjNlYzdhYTdlNTM32AIF4AIB&sid=bc1b875d65b70ca0b2181434764ac29e&age=12&age=12&all_sr_blocks=7806717_272984587_0_2_0%2C7806719_272984587_0_2_0&checkin=2021-07-08&checkout=2021-07-15&dest_id=-1658079&dest_type=city&dist=0&group_adults=3&group_children=2&hapos=8&highlighted_blocks=7806717_272984587_0_2_0%2C7806719_272984587_0_2_0&hpos=8&no_rooms=2&req_adults=3&req_age=12&req_age=12&req_children=2&room1=A%2C12&room2=A%2CA%2C12&sb_price_type=total&sr_order=upsort_bh&srepoch=1622965017&srpvid=c37b358cb0c50027&type=total&ucfs=1&activeTab=main")
driver.maximize_window()

'''
search_option = driver.find_element(By.XPATH,"//input[@placeholder='Where are you going?']")
search_option.clear()
search_option.click()
search_option.send_keys("Mexi")
time.sleep(2)
search_option.send_keys(Keys.ARROW_DOWN+Keys.ENTER)
time.sleep(5)

driver.find_element_by_xpath("//div[@class='xp__dates-inner']").click()
time.sleep(5)
a=0
while a>3:
    driver.find_element(By.XPATH,"//div[@class='xp__dates xp__group']/div[2]/div/div/div[2]").click()
    a=+1
time.sleep(5)

driver.find_element_by_xpath("//div[@class='xp-calendar']/div/div/div[3]/div[2]/table/tbody/tr[2]/td[5]").click()
#driver.find_element(By.XPATH,"//div[@class='xp-calendar']/div/div/div[1]").click()
driver.find_element_by_xpath("//div[@class='xp-calendar']/div/div/div[3]/div[2]/table/tbody/tr[3]/td[5]").click()
time.sleep(5)

#Guest
driver.find_element_by_xpath("//span[@class='xp__guests__count']").click()
#Adult
driver.find_element_by_xpath("//div[@id='xp__guests__inputs-container']/div/div/div[1]/div/div[2]/button[2]").click()
#child

time.sleep(2)
doubleclick=driver.find_element_by_xpath("//div[@id='xp__guests__inputs-container']/div/div/div[2]/div/div[2]/button[2]")
a=ActionChains(driver)
a.double_click(doubleclick).perform()
#Rooms
driver.find_element_by_xpath("//div[@id='xp__guests__inputs-container']/div/div/div[3]/div/div[2]/button[2]").click()
time.sleep(5)

search_option = driver.find_element(By.XPATH,"//input[@placeholder='Where are you going?']")
search_option.clear()
search_option.click()
search_option.send_keys("Mexi")
time.sleep(2)
search_option.send_keys(Keys.ARROW_DOWN+Keys.ENTER)
time.sleep(5)
#search
driver.find_element_by_xpath("//div[@class='xp__button']").click()
time.sleep(5)
#second page:
title_webpage=driver.title
Current_url=driver.current_url
print(Current_url)
print(title_webpage)
#driver.execute_script('window.scrollTo(0,1000);')
#filter box
driver.find_element(By.XPATH,"//div[@id='filter_price']/div[2]").click()
check_displayed=driver.find_element(By.XPATH,"//div[@id='filter_price']/div[2]").is_enabled()
if check_displayed==False:
    assert False
hold_start=driver.find_element(By.XPATH,"//div[@class='noUi-base']/div[2]/div")
hold_end=driver.find_element(By.XPATH,"//div[@class='noUi-base']/div[3]/div")
price_range=ActionChains(driver)
price_range.drag_and_drop_by_offset(hold_start,0,5).release().perform()
time.sleep(5)
price_range.drag_and_drop_by_offset(hold_end,9,7).release().perform()
time.sleep(10)


print(check_displayed)
#Adult select_box
select_dropdown=Select(driver.find_element(By.XPATH,"//div[@class='sb-searchbox__row u-clearfix']//select[@id='group_adults']"))
time.sleep(2)
select_dropdown.select_by_index(10)
time.sleep(5)
#Properties_category
driver.find_element(By.XPATH,"//a[contains(text(),'Entire homes & apartments')]").click()
time.sleep(5)
scroll_find=driver.find_element(By.XPATH,"//span[contains(text(),'Exe Suites San Marino')]")
#driver.execute_script("arguments[0].scrollIntoView();",frame)
driver.execute_script("arguments[0].scrollIntoView();",scroll_find)
scroll_find.click()
assert True
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
windows=driver.window_handles
for win in windows:
    print(win)
    
'''
#picture
driver.find_element(By.XPATH,"//div[@id='blockdisplay1']/div/div/div/div[6]/div/div[3]").click()
time.sleep(5)
#driver.execute_script('window.scrollTo(0,5000);')
frame=driver.find_element(By.XPATH,"//div[@class='bh-photo-modal-thumbs-grid js-bh-photo-modal-layout js-no-close']")
driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', frame)
frame2=driver.find_element(By.XPATH,"//div[@class='gallery-side-reviews-wrapper__body']/ul[2]/li[11]")
driver.execute_script("arguments[0].scrollIntoView();",frame2)
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='bh-photo-modal-thumbs-grid js-bh-photo-modal-layout js-no-close']/div/div/div[6]").click()
time.sleep(5)
#picture move

for x in range(15):
    driver.find_element(By.XPATH,"//div[@class='js-bh-photo-modal-layout']/a[2]/span").click()
driver.find_element(By.XPATH,"//button[@class='bui-button bui-button--light bh-photo-modal-close bh-no-user-select']/span[2]").click()



#driver.find_element(By.XPATH,"//div[@class='bh-photo-modal-thumbs-grid js-bh-photo-modal-layout js-no-close']/div/div/div[5]").click()
#close
#driver.find_element(By.XPATH,"//div[@class='bh-photo-modal-toolbar js-no-close']/button[1]/span[@class='bui-button__icon']").click()





