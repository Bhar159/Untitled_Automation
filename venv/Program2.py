
class person:
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
        print("Name list below:")
        self.mark=500
        print(self.mark)
        self.name3=-89

    def student(self):
        print(self.name1,self.name2)
        self.bonus=5698
        a=2
        b=4
        c=a+b
        print(c+self.mark)

class marking(person):
    def __init__(self,name1,name2,hello):
        super().__init__(name1,name2)
        self.hello=hello
        self.bye=8569
        print(self.name3)
        print(self.hello)
        print(self.bye)

    def passmark(self):
        name='Bharani'
        Grade='A+'
        print(name,"/",Grade+"/",self.mark,self.bonus)

a=marking("kj",'Farukshake',"fine")
a.student()
a.passmark()
