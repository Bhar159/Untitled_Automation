from pywinauto import*
import time
from selenium import webdriver

'''
app=application.Application()
app.start("Notepad.exe")
time.sleep(5)
app.Notepad.edit.TypeKeys("Hello  Welcome")
app.Notepad.MenuSelect("File -> Exit")
app.click("Don't Save")
app.SaveAs.edit.SetText("Sample.txt")
app.SaveAs.Save.Click()
'''
driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        'app': 'C:\\Notepad.exe'
    })
