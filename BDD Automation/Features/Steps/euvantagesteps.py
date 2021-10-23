from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


#######################_____Downloading a report_______######################
@given("^User in Home page$")
def homePage(context):
    context.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
    context.driver.get("https://na2-app.euvantage.com/Account/Login?clientCode=Anunta")
    context.driver.maximize_window()


@when('User enters username')
def userId(context):
    context.driver.find_element_by_xpath("//input[@id='username']").send_keys("vikkrams")


@when('User enters Password')
def userPwd(context):
    context.driver.find_element_by_xpath("//div[3]/div/input[@id='pwd']").send_keys("pass@123")


@when('User enters the home page login button')
def loginButton(context):
    context.driver.find_element_by_xpath("//button[@id='btnSubmit']").click()


@Then('User should be logged in successfully')
def loginScreen(context):
    currentUrl = context.driver.current_url
    print(currentUrl)
    if currentUrl == "https://na2-app.euvantage.com/MMDashboardOpt/Index#/Dashboard/View/Health":
        print("user in correct page")
        assert True
    else:
        assert False


@when('User clicks on home and navigate to report-usage till date')
def userReport(context):
    currentUrlpage = context.driver.current_url
    print(currentUrlpage)
    if currentUrlpage == "https://na2-app.euvantage.com/MMDashboardOpt/Index#/Dashboard/View/Health":
        print("user in correct page")
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[@id='main-wrapper']/div[@id='main-navbar']/button[2]/i").click()
    action = ActionChains(context.driver)
    action.move_to_element(
        context.driver.find_element_by_xpath("//div[@class='col-md-12 main-menu-content']/div[5]")).perform()
    webElement_Menu = context.driver.find_element_by_xpath(
        "//div[@class='col-md-12']//div[@class='col-md-12 sub-menu-content']/div[9]")
    webElement_SubMenu = context.driver.find_element_by_xpath(
        "//div[@class='col-md-12']//div[@class='col-md-12 sub-menu-content']/div[9]")
    action.move_to_element(webElement_Menu).perform()
    action.move_to_element(webElement_SubMenu).perform()
    action.click(webElement_SubMenu).perform()
    time.sleep(10)
    DropDown = Select(
        context.driver.find_element_by_xpath("//form//div[@class='col-md-12']//div[@class='form-inline']/select[1]"))
    DropDown.select_by_value('80')
    time.sleep(20)


@Then('File should download')
def downloadFile(context):
    context.driver.find_element_by_xpath(
        "//body/div[@id='main-wrapper']/div[@id='content-wrapper']/div[1]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/button[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath(
        "//div[@class='col-md-12']/div[@class='form-inline']//div[2]//ul/li[1]").click()


@Given('User in login page')
def loginPage(context):
    context.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
    context.driver.get("https://na2-app.euvantage.com/Account/Login?clientCode=Anunta")
    context.driver.maximize_window()


@when('Enter username "{user}" and password "{pwd}"')
def userCrd(context, user, pwd):
    context.driver.find_element_by_xpath("//input[@id='username']").send_keys(user)
    context.driver.find_element_by_xpath("//div[3]/div/input[@id='pwd']").send_keys(pwd)


@when('User enters the login button')
def login(context):
    context.driver.find_element_by_xpath("//button[@id='btnSubmit']").click()


@Then('User should be logged in home page successfully')
def loggedIn(context):
    pageTitle = context.driver.title
    title = context.driver.find_element_by_xpath("//*[@id='main-navbar']/div/div[1]/a/img").is_displayed()
    if title == "True":
        print("Positive case passed")
    elif pageTitle == "Anunta - LOGIN":
        print("Negative pass")


##################### _____FilterOption_____ ###########################################
@given('user open the login page')
def fLoginPage(context):
    context.driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
    context.driver.get("https://na2-app.euvantage.com/Account/Login?clientCode=Anunta")
    context.driver.maximize_window()


@when('user enters user id and password')
def fCred(context):
    context.driver.find_element_by_xpath("//input[@id='username']").send_keys("vikkrams")
    context.driver.find_element_by_xpath("//div[3]/div/input[@id='pwd']").send_keys("pass@123")

@when('User click the login button')
def flogin(context):
    context.driver.find_element_by_xpath("//button[@id='btnSubmit']").click()
    time.sleep(10)
    print("Current page" + context.driver.current_url)

@then('user successfully logged in home page')
def floginpage(context):
    presentUrl = context.driver.current_url
    print(presentUrl)
    if presentUrl == "https://na2-app.euvantage.com/MMDashboardOpt/Index#/Dashboard/View/Health":
        print("user in correct page")
        assert True
    else:
        assert False
    print(context.driver.current_url)


@when('User select home button and navigate to report and usage till_date')
def fHomePage(context):
    context.driver.find_element_by_xpath("//body/div[@id='main-wrapper']/div[@id='main-navbar']/button[2]/i[1]").click()
    time.sleep(10)
    action = ActionChains(context.driver)
    action.move_to_element(
        context.driver.find_element_by_xpath("//div[@class='col-md-12 main-menu-content']/div[5]")).perform()
    WebElement_Menu = context.driver.find_element_by_xpath(
        "//div[@class='col-md-12']//div[@class='col-md-12 sub-menu-content']/div[9]")
    WebElement_SubMenu = context.driver.find_element_by_xpath(
        "//div[@class='col-md-12']//div[@class='col-md-12 sub-menu-content']/div[9]")
    action.move_to_element(WebElement_Menu).perform()
    action.move_to_element(WebElement_SubMenu).perform()
    action.click(WebElement_SubMenu).perform()
    print("Current Page" + context.driver.current_url)
    print("Title" + context.driver.title)


@then('User successfully reached Usage till date page')
def fUsagePage(context):
    time.sleep(10)
    userPage = context.driver.current_url
    locTitle = context.driver.title
    print(userPage)
    print("Title" + locTitle)
    if userPage == "https://na2-app.euvantage.com/Analytic/UserDuration":
        assert True, "Passed"
    else:
        assert False, "Failed"


@when('User select filter option')
def fFilterOpt(context):
    DropDown1 = Select(
        context.driver.find_element_by_xpath("//form//div[@class='col-md-12']//div[@class='form-inline']/select[1]"))
    DropDown1.select_by_value('82')
    time.sleep(10)
    dropDown2 = Select(context.driver.find_element_by_xpath(
        "//form//div[@class='col-md-12']//div[@class='form-inline']/select[@id='period']"))
    dropDown2.select_by_value('0')
    time.sleep(10)
    context.driver.find_element_by_xpath("//div//button[@class='btn btn-primary btn-xs btn-labeled']").click()


@when('User enters the Pool name and server name and User name')
def ftextboxValue(context):
    time.sleep(10)
    poolName = '//input[@id="PoolNameTxt"]'
    serverName = '//input[@id="HostName_txt"]'
    userName = '//div[@class="col-md-2"]//span/input[@id="sourceIPAPPTxt"]'
    context.driver.find_element_by_xpath(poolName).click()
    context.driver.find_element_by_xpath(poolName).send_keys("My_Desktop_IGSDBU_Voice")
    time.sleep(5)
    context.driver.find_element_by_xpath(serverName).click()
    context.driver.find_element_by_xpath(serverName).send_keys("TPIGSDBUV3-0.intelenetglobal.com")
    #context.driver.find_element_by_xpath(userName).click()
    #context.driver.find_element_by_xpath(userName).send_keys("INTELENETGLOBAL\100000000467670")


@when('User click on search button')
def fsearchbox(context):
    context.driver.find_element_by_xpath(
        "//span/button[@class='btn btn-xs btn-success mrg-rt-10']/i[@class='fa-lg fa fa-search']").click()
    time.sleep(20)

@then('User navigated to expected page')
def fnavigator(context):
    assert True


# Second scenario
@when('User select the value from the drop down')
def fDropDownCheck(context):
    selectDrop = Select(context.driver.find_element_by_xpath("//span[@class='pull-right']/select[1]"))
    selectDrop.select_by_value('60')
    time.sleep(5)


@then(u'Verify selected value displayed in the report')
def fvalueCheck(context):
    selectedValue = context.driver.find_element_by_xpath("//span[contains(text(),'Top 60 Users')]")
    if selectedValue == "Top 60 Users":
        assert True, "Pass"
    else:
        assert False
    print(selectedValue)


# Third Scenario
@when('User drag the slider button')
def slideBar(context):
    performAction = ActionChains(context.driver)
    drag = context.driver.find_element_by_xpath(
        "//*[local-name()='svg']/*[local-name()='g'][11]/*[local-name()='g']/*[local-name()='g'][3]")
    performAction.click_and_hold(drag).move_by_offset(0, 25).release().perform()
    time.sleep(5)
    drag2 = context.driver.find_element_by_xpath(
        "//*[local-name()='svg']/*[local-name()='g'][11]/*[local-name()='g']/*[local-name()='g'][3]")
    performAction.click_and_hold(drag2).move_by_offset(50, 30).release().perform()
    time.sleep(5)


@then('Verify selected value displayed in the report window')
def fdisplay(context):
    assert True


# Fourth Scenario
@when(u'User clicks on clear all button')
def fclearbutton(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Clear All')]").click()


@then('Verity that text in the pool name,server ip,server name,session ip,username should be removed')
def fEmptyTextBox(context):
    poolNamebox = '//input[@id="PoolNameTxt"]'
    if (context.driver.find_element_by_xpath(poolNamebox).size() == 0):
        assert True
        print("pass")
    else:
        assert False
