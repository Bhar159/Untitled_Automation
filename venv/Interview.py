
from collections import*
import random as r
from collections import Counter
import re

#------------------------------
# reverse a number
# name="Hello"
# lsit_name=list(name)
# length=len(lsit_name)
# for x in range(length-1,-1,-1):
#     print(lsit_name[x],end="")
#-----------------------------------

# a=[1,2,3]
# print(a)
# s=''
#
# for x in a:
#     s=s.join(x)
#
# print(s)

a='Bharani'
print(a[0:4])


list_comp=[2*x for x in range(10)]
print(list_comp)











''''
class tesla():
    def __init__(self,car,model):
        self.car=car
        self.model=model
        self.price=1000
        self.customer_yes=True
        self.customer_no=False

        customer= input("Hello sir. Welcome to Carfact \n please enter your name: ")
        print("Hello Mr/Ms \t", customer)

        support_team=input("Would you like to check the model/price ? \t Yes/No: ")

        if support_team == 'Yes' or support_team=='Y' or support_team=='y':
            self.customer_yes
            print("Wait fo few sec, will direct to new page")
        else:
            print("OK, Thank you for your interest")
            self.customer_no

    def model():
        list_options = {1: 'Telsaxsc', 2: 'Tesxl', 3: "teslabmX"}
        print(list_options)
        customer_choice=input("choose the below option: /n If you come out of the page enter No")
        if customer_choice=='no' or customer_choice=='No':
            False
        elif customer_choice=='1':
            print("you have selected 1",list_options[1])
        elif customer_choice=='2':
            print("you have sffelected 2",list_options[2])
        elif customer_choice=='3':
            print("you have selected 2",list_options[3])
        else:
            print("please select the option..!!")






tesla(car='tesla',model='125xs')
tesla.model()





#phone number
Phone_number="Call me on +91-950-0586-974"
search=re.search("\+\d{2}-\d{3}-\d{4}-\d{3}",Phone_number)
print(search)

#date
date="today date 06-02-2021"
result1=re.findall("\d{2}-\d{2}-\d{4}",date)
print(result1)



text="hello sir? hello sir? are you there hello?"
result=re.findall("hello",text)
print(result)

for x in rInterview.pyesult:
    print(x)


#email ID
text="Can you please share your Email ID ? Bharanimurali159@gmail.com"
ans=re.search(r'[a-zA-Z0-9]+@[a-z]+\.(com|edu|in)',text)
print(ans)






 # Counter
name="Bharani"
count=Counter(name)

print(count['B'])
print(count)

for x in 'hara':
    print(x,count[x])
---------------Tuple
a=(1,2,3,'bharani')

#print(a[2])
------Random
a=[1,2,3,4,5]
b=r.choice(a)
print(b)

print(r.random())
print(r.randint(-99,-33))
print(r.sample(a,3))

r="Welcoome too narcooos tat cccc"
b=Counter(r)
print(b)

print(b['t'])

for x in 'teo':
    print(x,b[x])
'''














