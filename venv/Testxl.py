import openpyxl
from selenium import webdriver
import time

path="D:\\New.xlsx"
workbook=openpyxl.load_workbook(path)
name=workbook.sheetnames
print(path)
print(name)
sheet=workbook.get_sheet_by_name("User")

password=sheet.cell
rows=sheet.max_row
column=sheet.max_column
print("Rows",rows)


driver = webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver')
driver.get("https://www.facebook.com/")

for x in range(1,rows+1):
    username = sheet.cell(row=x, column=1).value
    password=sheet.cell(row=x,column=2).value
    driver.find_element_by_xpath("//input[@id='email']").clear()
    driver.find_element_by_xpath("//input[@id='email']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='pass']").send_keys(password)
    driver.find_element_by_xpath("//button[@name='login']").click()
    time.sleep(5)
    text=driver.find_element_by_xpath("//div[contains(text(),'தவறான நற்சான்றுகள்')]").text
    if text=="//div[contains(text(),'தவறான நற்சான்றுகள்')]":
        print("Correct its working")
        driver.refresh()
        time.sleep(5)
    else:
        print("Failed")
        driver.refresh()
        time.sleep(5)


