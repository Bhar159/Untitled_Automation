def bank(current_balance, withdrawn_amount):
    bank_balance=current_balance-withdrawn_amount
    return bank_balance
balance = bank(5100,200)

name = input("Enter your name: ")
acc_number = input("Enter your acc_number: ")
branch = input("Enter your branch: ")

if (acc_number == '1512'):
        print("Wait for a sec", name.upper())
        print("Your account balance $", balance)

        if(balance <= 6000):
            print("Your balance is too low",name.upper())
else:
        if(acc_number != '1512'):
            print("Unknown user")
            print("Check your password & Acc_number")

"""  new programm  """

a = 'bharani tharan'
b = list(a)


for x in range(0, len(a), 2):
    b[x] = b[x].upper()
    print(b)
    x = ''.join(b)
print(x)

def sample():
    num1=input("enter your num1: ")
    num2=input("enter your num2: ")
    total=int(num1)+int(num2)
    return total

def orange():
    price=sample()
    if price==3:
        print("good")
    else:
        print("try")

orange()

def removevowels(input):
    vowels='aeiou'
    f1=[]
    for i in input:
        if i not in vowels:
            f1.append(i)
    return ''.join(f1)



input='bharani Murali'
a=removevowels(input)
print(a)

x=6
num=0

for a in range(x):
    for b in range(a):
        i=num*1
        num+=3
        print(i,end='')
    print('')

dx=datetime(2011,2,12,9,32,22,22)
print(dx)
print(dx.date())
sx=dx.replace(minute=55,second=12)
print(sx)
fx=dx.strftime('%y|%d|%m %h:%m')
print(fx)


import base64

a='bharani Murali'.encode('utf-8')
y=base64.b64encode(a)
c=base64.b64decode(y)

print(y)
print(c)

''' Wrapping'''
import textwrap
def wrap(string, max_width):
    apple=textwrap.TextWrapper(width=max_width)
    text=apple.wrap(text=string)
    return text

line="hello man how are you"
x=wrap(line,40)
print(x)





