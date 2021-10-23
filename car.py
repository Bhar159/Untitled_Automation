class car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100
        print("Hello")

    def car_model(self):
        print("Available car model: " + self.model + " " + self.make + " " + str(self.year))

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it(test drive).")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print(self.odometer_reading)

class Electriccar(car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def batterylife(self, working_percent):
        print("Battery working_percent: ", working_percent, "%")

class battery(Electriccar):
    def __init__(self,make, model, year,battery_size):
        Electriccar.__init__(self,make, model, year)
        self.battery_size = battery_size

    def car_battery(self):
        print("This car has self_battery percent: " + str(self.battery_size))

    def get_range(self):

        range=" "
        if self.battery_size == 70:
            range = 120
        elif self.battery_size == 20:
            range = 154
        message = "This car has range: " + str(range)
        message += "\nAnd this is new feature"
        print(message)







my_new_car = car('audi', 'a4', 2016)
my_new_car.car_model()
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_tesla = Electriccar('tesla', 'sx', '2019')
my_tesla.car_model()
my_tesla.increment_odometer(700)
my_tesla.batterylife(98)
my_bat=battery('TBD','TBD',"TDB",70)
my_bat.car_battery()
my_bat.get_range()
















