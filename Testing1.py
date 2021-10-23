from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import pytest
import allure
#https://twitter.com/LOGIN
@pytest.mark.Smoke1
def Testing():
        paths='Downloads\chromedriver_win32/chromedriver'
        driver=webdriver.Chrome(paths)
        driver.get("http://www.airindia.in/")
        time.sleep(2)
        mouse=ActionChains(driver)
        mouse.move_to_element(driver.find_element_by_id("aMnu1")).perform()
        driver.find_element_by_xpath('//a[contains(text(),"Flight Schedules")]').click()
        driver.set_page_load_timeout(10)
        #driver.get("https://book.airindia.in/itd/itd/lang/en/travel/schedules")
        #print("first page:"+driver.current_url)
        driver.maximize_window()

        #wait=WebDriverWait(driver,100)
        #wait.until(ec.element_to_be_selected(By.XPATH("")))
        window=driver.window_handles
        for win in window:
            driver.switch_to.window(win)
            if (driver.current_url=='https://book.airindia.in/itd/itd/lang/en/travel/schedules'):
                    time.sleep(2)
                    #wait.until(ec.element_to_be_selected(By.XPATH('//label[contains(text(),"Weekly schedule")]')))
                    driver.find_element_by_xpath('//label[contains(text(),"Weekly schedule")]').click()
                    select=Select(driver.find_element_by_xpath('//select[@id="searchDepartLocation"]'))
                    select.select_by_visible_text("Hyderabad (HYD)")
                    select=Select(driver.find_element_by_id("searchArriveLocation"))
                    select.select_by_value("Airport.MAA")
                    driver.find_element_by_id("tripTypeReturnRadio").click()
                    select1=Select(driver.find_element_by_xpath('//select[@id="wdfday0"]'))
                    select1.select_by_index(14)
                    select1=Select(driver.find_element_by_id("wdfmonthyear0"))
                    select1.select_by_value("2020-08")
                    print(select1.first_selected_option.text)

                    driver.find_element_by_id("tripTypeOneWayRadio").click()
                    driver.find_element_by_xpath("//div[2]/input[@type='submit']").click()
                    print("Latest:\n\tCureent Url Page "+driver.current_url)
                    time.sleep(5)
                    print(driver.find_element_by_xpath('//span[@class="breadcrumb_element breadcrumb_item selectd_breadcrumb"]').text)


Testing()



