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
#driver.get("https://anuntaqa.mydesktopnow.com")
driver.get("https://anuntaqa.mydesktopnow.com")
driver.maximize_window()
driver.implicitly_wait(10)
body_text=driver.find_element_by_tag_name('body').text
print(body_text)
driver.find_element_by_xpath("//div[@class='p-4 ng-star-inserted']/form/div[1]/div/input").send_keys("QA")
driver.find_element_by_xpath("//div[@class='p-4 ng-star-inserted']/form/div[2]/div/input").send_keys("pass@123")
driver.find_element_by_xpath("//button/span[contains(text(),'Login')]").click()
time.sleep(5)
tab_AddVm_Xpath="//div[@class='col-12']/div/div/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]/div"
ad_click_avRegion_xpath="//div[@class='col-sm-10']/mat-select/div"
ad_dropdown_avRegion_xpath="//body/div[3]/div[2]/div[1]/div[1]/div[1]"
regions_list_number="//body/div[3]/div[2]/div[1]/div[1]/div[1]/mat-option[1]"
driver.find_element_by_xpath("//span[contains(text(),'VM Images')]").click()
driver.find_element_by_xpath(tab_AddVm_Xpath).click()
time.sleep(5)
driver.find_element_by_xpath(ad_click_avRegion_xpath).click()
region_list=driver.find_element_by_xpath(ad_dropdown_avRegion_xpath).text
print(region_list)
-------@@@@@
regions= {1:'East US',2:'West US 2',3:'Central US',4:'Brazil South',5:'South Africa North',6:'North Europe',7:'Germany West Central',
         8:'France Central',9:'Korea Central',10:'Japan East',11:'UAE North',12:'Australia East',13:'Central India',14:'Southeast Asia'}
print(regions.get(2))
listing=list(regions.items())
print(listing)

driver.find_element_by_xpath("").is_displayed()


if 1 in regions:
    print("hello")

for x in range(2,4):
    print ("Loop started")
    if x in regions:
        driver.find_element_by_xpath("//body/div[3]/div[2]/div[1]/div[1]/div[1]/mat-option["+str(x)+"]").click()
    elif regions==regions.keys(x):
        driver.find_element_by_xpath("//body/div[3]/div[2]/div[1]/div[1]/div[1]/mat-option["+str(3)+"]").click()
    # elif regions==regions.keys(x):
    #     driver.find_element_by_xpath("//body/div[3]/div[2]/div[1]/div[1]/div[1]/mat-option["+str(4)+"]").click()




driver.find_element_by_xpath("//div[@class='mat-tab-body-wrapper']/mat-tab-body/div/div/div/div/div/div[1]/div/span").click()
before_sort=len(driver.find_elements_by_xpath("//div[@class='overflow-auto']/div"))
beforeSorting=[]
for  x in range(1,before_sort+1):
    before=driver.find_element_by_xpath("//div[@class='overflow-auto']/div["+str(x)+"]").text
    beforeSorting.append(x)
    print(before,end='')
print()
time.sleep(5)
print("-----------------------Before Sort Done-------------------")
select_sort=Select(driver.find_element_by_xpath("//select[@id='inputGroupSelect01']"))
select_sort.select_by_value("asc")
time.sleep(5)
after_sort=len(driver.find_elements_by_xpath("//div[@class='overflow-auto']/div"))
aftersorting=[]
for y in range(1,after_sort+1):
    after=driver.find_element_by_xpath("//div[@class='overflow-auto']/div["+str(y)+"]").text
    aftersorting.append(y)
    print(after,end='')
print()

assertEqual(before,after,"Sorting is not working")

driver.find_element_by_xpath("").is_displayed()

'''












