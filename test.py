'''
import textwrap

import matplotlib.pyplot as plt


a=[1,3,5]
b=[6,8,10]
c=[4,7,9]
plt.plot(a,b,linewidth=10)
plt.plot(a,c,linewidth=12)
plt.title("percentage",fontsize=3)
plt.xlabel("total",fontsize=5)
plt.ylabel("no of pepeole(millions)")
plt.legend(["people","revenue"])
plt.show()

'''
from datetime import *


class Bank():
    def __init__(self):
        print("Welcome to HDFC Corprate bank __/\__")
        self.Acc_number = input("Enter the Account Number:")
        self.Password = input("Enter the Password:")
        if self.Acc_number == '12345' and self.Password == '12345':
            print("Please wait for a moment")
            self.isCredTrue = True
        else:
            print("Sorry please check the Accountnumber and password")
            self.isCredTrue = False

    def getIsCredTrue(self):
        return self.isCredTrue

    def nextstep(self, total_amount):
        Withdraw_amount = input("Enter the Amount you like to withdraw:")
        date = datetime.today()
        balance_amount = total_amount - int(Withdraw_amount)
        print("Remaining balance: \n\t", balance_amount)
        print(date)
        user = input("\n\t Would you like to take loan: Y/N  ")
        if user == 'Y' or user == 'y':
            print("wait for a moment..!!")
            self.loan = True
        else:
            print("Thank you..!!")
            self.loan = False

    def loans(self):
        return self.loan

    def choose(self):
        list = {1: "House loan", 2: "personal loan", 3: "Car loan"}
        print("Please choose the below options:")
        for x, y in list.items():
            print(x, y)
        user = input("Enter the options:")
        if user == '1':
            print("you have choosed ", list[1])
            print("Our branch manger will contact you..!!")
        elif user == '2':
            print(list[2])
            print("you have choosed ", list[2])
            print("Our branch manger will contact you shortly..!!")
        elif user == '3':
            print(list[3])
            print("you have choosed ", list[3])
            print("Our branch manger will contact you..!!")


a = Bank()
if a.getIsCredTrue():
    a.nextstep(26000)
    if a.loans():
        a.choose()
        print(a)
