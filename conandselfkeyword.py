"""class laptop:
    def __init__(self): #constructer
        print("demo")
    def display(self):
        print("display")

hp=laptop() #object"""


"""class laptop:
    def __init__(self): #constructer
        self.price=""
        self.ram=""
    def display(self):
        print("ram",self.ram)
        print("price",self.price)

hp=laptop()
dell=laptop() #object

hp.price=50000
hp.ram="i7"
dell.price=60000
dell.ram="i5"

hp.display()
dell.display()"""


"""class laptop:  #empty class 
    pass """

"""class student:
    def __init__(self):
        self.name="kamalesh"
        self.regno = "921622104021"
    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)

s1=student()
print(s1.name)
print(s1.regno)
s1.display()"""

"""class student:
    def __init__(self):
        self.name="kamalesh"
        self.regno = "921622104021"
    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)

s1=student()
s2=student()

s1.name="kamalesh"
s1.regno="921622104021"
s2.name="maha"
s2.regno="921622104025"
s1.display()
s2.display()"""


"""class fruit:
    def __init__(self):
        self.colour="black"

apple=fruit()
print(apple.colour)"""

"""class fruit:
    def __init__(self,col):
        self.colour=col

apple=fruit("red")
print(apple.colour)"""

"""class teacher:
    def __init__(self,name,regno):
        self.name =name
        self.regno=regno
    def display (self):
        print("name",self.name)
        print("regno",self.regno)

t1=teacher("aparna","1")
t2=teacher("femila","2")
t1.display()
t2.display()"""

"""class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)

obj1=calculator(10,2)
obj1.add()"""
"""
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def sub(self):
        print("sub",self.num1-self.num2)

obj1=calculator(10,2)
obj1.sub()"""

"""
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def div(self):
        print("div",self.num1/self.num2)

obj1=calculator(10,2)
obj1.div()"""


class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def mul(self):
        print("mul",self.num1*self.num2)

obj1=calculator(10,2)
obj1.mul()