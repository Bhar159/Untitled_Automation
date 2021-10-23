class dog():

    def __init__(self, name, breed):
        self.name = input("what is your name? ")
        self.breed = input("what is your bread? ")

    def names(self):
        print(self.name.title()+" my dog name")

    def breeds(self):
        print(self.breed.title() + ' breed')


doggies = dog(name='',breed='')

doggies.names()
doggies.breeds()
print("my dog name is: " + doggies.name.title() + ".")
print("my dog breed is: " + doggies.breed.title() + ".")

class dem():

    def __init__(self, acc_id, name, amount):
        self.acc_id = input("Enter your id: ")
        self.name = input("enter you name: ")
        self.amount = 1000

    def hdfc(self, debit_amount, total_balance):
        remaining_balance = total_balance - debit_amount
        print("Welcome to our bank" + self.name.title())
        print("Please find confirm you acc_number: " + self.acc_id)
        print("Please find your balance:", remaining_balance)

        self.amount += remaining_balance
        print(self.amount)


my_bank = dem(acc_id='', name='', amount='')
my_bank.hdfc(1500, 1500)
print(my_bank.hdfc(50, 250))









