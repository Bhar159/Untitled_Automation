######Working as expected#################
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

path='Downloads\chromedriver_win32/chromedriver'
driver=webdriver.Chrome(path)
driver.get("https://www.facebook.com/")

driver.find_element_by_id('email').send_keys("bharani")
driver.find_element_by_id('pass').send_keys("bharani")
#actionchain(keyboard/mouse)
'''
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
act.send_keys(Keys.TAB).perform()
driver.find_element_by_xpath('//input[@id="pass"]').send_keys('bharanii@123')

act=ActionChains(driver)
act.click(driver.find_element_by_id('u_0_b')).perform()
act1=ActionChains(driver)
'''
#how to get text of url/attribute value/page source/title
#act1.move_to_element(driver.find_element_by_xpath('//a[contains(text(),"Forgotten account?")]')).perform()
print("Tile is "+driver.title)
print("Url is "+driver.current_url)
#print("___________________________________________________")
print("fetching text"+ driver.find_element_by_xpath('//span[contains(text(),"Create an account")]').text)
print("fetech attribute value: " +driver.find_element_by_css_selector('input[id="u_0_o"]').get_attribute("class"))
