from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pytest

@pytest.mark.Smoke
def Test_programminh():
    # driver=webdriver.Firefox()
    # driver.get("https://www.facebook.com")
    chromedriver = 'Downloads\chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.naukri.com")
    driver.maximize_window()
    ###### Screenshot####

    driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/untitled/venv/Screenshot.png")
    #TakeScreenshot.take_snip(driver, "First_snip")
    def take_snip(driver, name):
        driver.get_screenshot_as_file("C:/Users/bhara/PycharmProjects/untitled/venv/" + name + ".png")
    mainWin1=''
    driver.execute_script("window.scrollTo(0,700);")
    Allwindows1=driver.window_handles
    for win1 in Allwindows1:
        driver.switch_to.window(win1)
        if (driver.current_url=="https://www.naukri.com/"):
            original=win1
        else:
            driver.close()
    driver.switch_to.window(mainWin1)
    print(driver.current_url)

    a=''
    window=driver.window_handles
    for new_windows in window:
        driver.switch_to.window(new_windows)
        if (driver.current_url=='https://www.naukri.com/'):
            print("Main_window"+driver.current_url)
            a=new_windows
        else:
            print("secondary window"+driver.current_url)
            driver.close()

    driver.switch_to.window(a)
    print(driver.current_url)
    ##Window scroll down:
    driver.execute_script("window.scrollTo(0,1000);")

    driver.get("")
    driver.minimize_window()

    driver.find_element_by_xpath("").send_keys()
    driver.find_element_by_xpath("").click()

    drop=Select(driver.find_element_by_xpath(""))
    drop.select_by_value("")
    print(drop.first_selected_option.text)
    for x in drop.options:
        print(x)
    action=ActionChains(driver)
    action.move_to_element("").perform()
    action.key_down("").send_keys("").perform("")
    print(driver.find_element_by_xpath("").get_attribute("").text)
    time.sleep(1)
    driver.set_page_load_timeout(5)
    implicit=WebDriverWait(driver,5)
    implicit.until(ec.element_to_be_selected(By.XPATH("")))
    a=driver.current_url
    assert driver.current_url==a

    driver.execute_script('window.scrollTo(0,400);')


    def snipshot(driver,name):
        driver.get_screenshot_as_file(""+name)
    #Takescreenshot.snapshot(driver,'hello')

    all_window=driver.window_handles
    print(all_window)

    main_win=''
    for x in all_window:
        driver.switch_to.window(x)
        if driver.current_url=="www.airindia.com":
            main_win=x
        else:
            driver.close()

    driver.switch_to.frame()
    driver.switch_to.default_content()












