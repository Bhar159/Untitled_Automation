from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import sys
from locators import LocElement


#######################   Health_Check  ######################



@Given("user in the login page")
def HhomePage(context):
    context.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
    context.driver.get("https://na2-app.euvantage.com/Account/Login?clientCode=Anunta")
    context.driver.maximize_window()
    print("System path 234555:  ", sys.path)

@When("user enters user id/password cred")
def HCred(context):
    context.driver.find_element_by_xpath("//input[@id='username']").send_keys("vikkrams")
    #a=context.driver.find_element_by_xpath("//input[@id='username']")
    #context.driver.executeScript("document.getElementById('username').value='vikkrams';")
    context.driver.find_element_by_xpath("//div[3]/div/input[@id='pwd']").send_keys("pass@123")

@When("User click the login icon")
def HCredLogin(context):
    context.driver.find_element_by_xpath("//button[@id='btnSubmit']").click()
    time.sleep(10)
    print(context.driver.current_url)

@When("user successfully logged in home page")
def Page_Info(context):
    Current_Url1=context.driver.current_url
    print(Current_Url1)

''' #################### parameter report(First_check) #################### '''

@when('Navigate to report and click on parameter icon')
def Para_Icon(context):
    context.driver.find_element_by_xpath("//div[@id='main-navbar']/button[2]").click()
    time.sleep(5)
    actionP=ActionChains(context.driver)
    actionP.move_to_element(context.driver.find_element_by_xpath('//div[@class="col-md-12 main-menu-content"]/div[5]')).perform()
    Move_Xpath=(context.driver.find_element_by_xpath("//div[@class='col-md-12 sub-menu-content']/div[1]"))
    actionP.move_to_element(Move_Xpath).perform()
    actionP.click(Move_Xpath).perform()
    time.sleep(5)

@then('enter client details and click on search')
def Client_details(context):
        select1 = Select(
            context.driver.find_element_by_xpath("//div[@class='col-md-2']/div[@class='form-group']/select[@id='client']"))
        select1.select_by_visible_text("County of San Mateo")
        time.sleep(5)
        context.driver.find_element_by_xpath("//input[@id='deviceIP']").send_keys("172.16.204.112"+Keys.ARROW_DOWN+Keys.ENTER)
        #time.sleep(1)
        #context.driver.find_element_by_xpath("//input[@id='deviceIP']").send_keys(Keys.ARROW_DOWN+Keys.ENTER)
        time.sleep(5)
        select2 = Select(context.driver.find_element_by_xpath("//select[@id='period']"))
        select2.select_by_visible_text("Last Week")
        time.sleep(5)
        select3 = Select(context.driver.find_element_by_xpath("//select[@id='parameter']"))
        select3.select_by_value('10')


@then('Report should generate successfully')
def parameter_report(context):
    context.driver.find_element_by_xpath(
        "//body/div[@id='main-wrapper']/div[@id='content-wrapper']/div[1]/div[3]/div[1]/div[2]/form[1]/div[2]/div[4]/div[1]/button[1]").click()
    time.sleep(5)
    context.driver.save_screenshot("D:\Selenium\screenshot1.png")


'''-----------#Device_dashboard(Second_check)-------------------'''

@when('User navigates to health/Alert Dashboard')
def DHomepage(context):
    context.driver.find_element_by_xpath("//div[@id='main-navbar']/button[2]").click()
    time.sleep(5)
    daction=ActionChains(context.driver)
    daction.move_to_element(context.driver.find_element_by_xpath("//div[@class='col-md-12 main-menu-content']//div[2]/div/i")).perform()
    daction1=context.driver.find_element_by_xpath("//div[@class='col-md-12 sub-menu-content']/div[2]")
    daction.move_to_element(daction1).perform()
    daction.click(daction1).perform()

@when('select the client/model name and device ip')
def DClient(context):
    context.driver.refresh()
    time.sleep(15)
    select2 = Select(context.driver.find_element_by_xpath("//div[@class='form-group']/select"))
    select2.select_by_visible_text("County of San Mateo")
    time.sleep(15)
    context.driver.find_element_by_xpath("//a[contains(text(),'Windows 10 Pro')]").click()



@then('User should able to see the report status')
def Dreport(context):
    url2=context.driver.current_url
    print(url2)
    time.sleep(5)
    context.driver.find_element_by_xpath("//a[contains(text(),'172.16.205.99')]").click()
    time.sleep(15)
    context.driver.save_screenshot("D:\Selenium\screenshot2.png")

'''-----------------------Session_Count(Third_check)-------------------------'''
@when('User navigates to Home-->Monitoring dashboard')
def SHome(context):
    context.driver.find_element_by_xpath("//div[@id='main-navbar']/button[2]").click()
    time.sleep(5)
    saction = ActionChains(context.driver)
    saction.move_to_element(
        context.driver.find_element_by_xpath("//div[@class='col-md-12 main-menu-content']//div[2]/div/i")).perform()
    saction.move_to_element(context.driver.find_element_by_xpath("//h6[contains(text(),'Monitoring Dashboard')]")).perform()
    saction.click(
        context.driver.find_element_by_xpath("//h6[contains(text(),'Monitoring Dashboard')]")).perform()


@Then('User should able to see the report status1')
def Sreport(context):
    url3=context.driver.current_url
    print(url3)
    time.sleep(15)
    select3=Select(context.driver.find_element_by_xpath("//body/div[@id='main-wrapper']/div[@id='content-wrapper']/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
    select3.select_by_visible_text('County of San Mateo')
    time.sleep(15)
    context.driver.save_screenshot("D:\Selenium\screenshot3.png")

'''-------------------Topology(Forth_check)------------------------------'''
@when('User Navigates to HOME-->Configuration-->User Session')
def Thome(context):
    context.driver.find_element_by_xpath("//div[@id='main-navbar']/button[2]").click()
    time.sleep(5)
    Taction=ActionChains(context.driver)
    Taction.move_to_element(context.driver.find_element_by_xpath("//h6[contains(text(),'CONFIGURATION')]")).perform()
    #Taction.move_to_element(context.driver.find_element_by_xpath("//div[@class='col-md-12 sub-menu-content']//div[21]")).perform()
    Taction.click(
        context.driver.find_element_by_xpath("//div[@class='col-md-12 sub-menu-content']//div[21]")).perform()

@when('enter the IP address and select the session ip')
def TIp_details(context):
    url4=context.driver.current_url
    print(url4)
    time.sleep(10)
    select4 = Select(context.driver.find_element_by_xpath(
        "//body/div[@id='main-wrapper']/div[@id='content-wrapper']/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/select[1]"))
    select4.select_by_visible_text('County of San Mateo')
    time.sleep(10)
    context.driver.find_element_by_xpath("//tbody/tr[1]/td[3]/a[1]").click()
    time.sleep(25)
    context.driver.find_element_by_xpath(
        "//body/div[@id='main-wrapper']/div[@id='content-wrapper']/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/img[1]").click()

@Then('User should able to see the status report2')
def TIp_details(context):
    url5=context.driver.current_url
    print(url5)
    time.sleep(25)
    context.driver.save_screenshot("D:\Selenium\screenshot4.png")


'''------------Fifth_Check---------------------------'''

@when('user Navigates to home-->Diagnosis dashboard')
def FHome(context):
    context.driver.find_element_by_xpath("//div[@id='main-navbar']/button[2]").click()
    time.sleep(5)
    action5=ActionChains(context.driver)
    action5.move_to_element(context.driver.find_element_by_xpath("//div[@class='col-md-12 main-menu-content']//div[2]/div/i")).perform()
    action5.click(context.driver.find_element_by_xpath("//div[@class='col-md-12 sub-menu-content']//div[4]")).perform()
    time.sleep(15)
    context.driver.save_screenshot('D:\Selenium\screenshot5.png')
    time.sleep(5)
    context.driver.execute_script("window.scrollTo(0,500);")
    context.driver.save_screenshot('D:\Selenium\screenshot5.1.png')
    time.sleep(5)
    context.driver.execute_script("window.scrollTo(0,1000);")
    context.driver.save_screenshot('D:\Selenium\screenshot5.2.png')

@when('User should able to see the report status3')
def FReport(context):
    assert True
    print("Check the screenshots")





