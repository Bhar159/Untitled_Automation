from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from collections import Counter
import re
import random as r
import string

def rNmaes():
    Nonvowels =['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't','v', 'w', 'x', 'y', 'z']

    vowels=['a','e','i','o','u']
    randomNumber=r.randint(2,4)
    print(randomNumber)
    name=""
    for x in range(randomNumber):
        randomNonVowels=r.choice(Nonvowels)
        randomVowels=r.choice(vowels)
        name=name+randomVowels+randomNonVowels
    return name

a=rNmaes()
print(a)






# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--incognito')
# driver=webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver',chrome_options=chrome_options)
# driver.get('https://www.airasia.co.in/home')
# msg=driver.find_elements_by_tag_name("a")
# print(msg)
# print("Completed")

# opt=Options()
# opt.add_argument("--headless")
# driver=webdriver.Chrome(executable_path='D:\Selenium\chromedriver_win32/chromedriver',chrome_options=opt)
# driver.get('https://www.airasia.co.in/home')
# msg=driver.find_elements_by_tag_name("a")
# print(msg)
# print("Completed")


#
# def email(size=4,chars=string.ascii_lowercase+string.digits+string.ascii_uppercase):
#     return ''.join(r.choice(chars) for x in range(size))
#
# a=email()
# print(a+"@gmail.com")


# def randomEmail(size=4,char=string.ascii_lowercase+string.digits):
#     return ''.join(r.choice(char) for x in range(size))
#
# a=randomEmail()
# print(a+"@gmail.com")


# def Alpha(name):
#     word="bhar"
#     f=[]
#     c=''
#     for x in word:
#         if x  in name:
#             f.append(x)
#     for x in name:
#         if x not in word:
#             c=''.join(x)
#     print(f)
#     print(c)
# Alpha("bharani")







