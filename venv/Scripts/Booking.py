import requests
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


tag = driver.find_elements(By.TAG_NAME,"a")

print(len(tag))
empty_list=[]

for x in tag:
    empty_list.append(x.get_attribute('href'))

for link in empty_list:
    r=requests.get(link)
    #print(r.status_code)
    if r.status_code >=400:
        print(link)
        print(r.status_code)

tags=driver.find_elements(By.TAG_NAME,'a')
print(len(tag))
empty_list2=[]

for c in tags:
    empty_list2.append(c.get_attribute('href'))

for links in empty_list2:
    r1=requests.get(links)
    if r1.status_code >=400:
        print()




'''

print(enter)
for x in range(1,enter+1):
    for y in range(1,x+1):
        print(y,end='')
    print(" ")
'''
