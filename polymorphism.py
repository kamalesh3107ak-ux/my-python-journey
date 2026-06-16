#polymorphism
#poly = more , morphism = change the body 

"""
def add(a,b,c=0):
    print(a+b+c)
add(10,20,)
add(10,20,30)"""

"""class animal():
    def sound (self):
        print("animal make sound")

class dog(animal):
    def sound(self): #method overriding
        print("dog barks")

class bird(animal):
    def sound(self):
        print("bird sing")

b1=bird()
b1.sound()"""

"""class shape():
    def area(self):
        return 0
    
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)
        
r1=rectangle()
r1.area()"""

"""
class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

    def display(self):
        print(self.name,self.grade)

s1=student("kamalesh","A")
s1.display()"""


"""
class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
         super().start()
         print("car started")



s1=car()
s1.start()"""


class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        print("name:",self.name,"salary:",self.salary,"department:",self.department)

m1=manager("kamalesh","50000","cse")
m1.display()



