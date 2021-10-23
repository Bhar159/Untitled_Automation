import pytest
from selenium import webdriver
import allure

'''
# @pytest.mark.skipif(a>100, reason="skip this")
@pytest.mark.regression
def test_cases1_data():
    paths = 'Downloads\chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(paths)
    driver.get("https://book.airindia.in/itd/itd/lang/en/travel/schedules")
    print("first page:" + driver.current_url)


@pytest.mark.Smoke
def test_cases2_copy():
    paths = 'Downloads\chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(paths)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()


@pytest.mark.Smoke
def test_cases2_data():
    paths = 'Downloads\chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(paths)
    driver.get("https://twitter.com/")
    driver.maximize_window()
    

@pytest.fixture(scope='module')
def fixture():
    global driver
    paths = 'Downloads\chromedriver_win32/chromedriver'
    driver = webdriver.Chrome(paths)
    driver.maximize_window()
    yield
    driver.close()
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.Smoke
def test_cases1_data(fixture):
    driver.get("https://book.airindia.in/itd/itd/lang/en/travel/schedules")
    print("first page:" + driver.current_url)
    a=driver.current_url
    assert driver.current_url=='same'
    allure.attach(driver.get_screenshot_as_png(),name="sample_allure")
@allure.severity(allure.severity_level.MINOR)
def test_cases2_copy(fixture):
    driver.get("https://www.facebook.com/")
    b=driver.title
    assert driver.title==b

@pytest.mark.Smoke
def test_cases2_data(fixture):
    driver.get("https://twitter.com/")
    driver.find_element_by_xpath('//input[@id="pass"]').send_keys()
    
'''



a='bharani'

b=len(a)

r=[]

while b > 0:
    r +=a[b -1]
    b=b-1
print(r)



