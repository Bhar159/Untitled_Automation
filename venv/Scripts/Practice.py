import openpyxl
from selenium import webdriver
import time


path="C:\\Users\\bhara\\PycharmProjects\\untitled\\BDD Automation\\TestData\\New.xlsx"
workbook=openpyxl.load_workbook(path)
print(workbook)
sheet=workbook.get_sheet_by_name('Corona list')
data1=sheet['B3'].value
print(data1)
print(sheet.cell(7,4).value)
print(workbook['Corona list']['B8'].value)
sheet['B22'].value='Pune'

rowCount=sheet.max_row
colunmCount=sheet.max_column
print(rowCount)
print(colunmCount)
print(workbook.sheetnames)
print(workbook.active.title)

usersheet=workbook.active
usersheet['A7'].value="Canada"
usersheet['A6'].value="Jiji"
print(usersheet.cell(column=1,row=7).value)
print(usersheet.cell(column=1,row=6).value)
workbook.save(path)

# for x in range(1,rowCount+1):
#     for y in range(1,colunmCount+1):
#         print(sheet.cell(row=x,column=y).value)


