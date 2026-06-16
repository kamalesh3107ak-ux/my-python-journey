# instance variable 
# class variable

"""class phone():
    def __init__(self,brand,price,charegertype):
        self.brand=brand #instance variable
        self.price=price
        self.chargertype=charegertype
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype",self.chargertype)   

samsung=phone("samsung","10000","b type") 
samsung.display()

redmi=phone("redmi","10000","b type") 
redmi.display()"""

class phone():
    chargertype="c-type" #class variable
    def __init__(self,brand,price):
        self.brand=brand 
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype",self.chargertype)   

phone.chargertype="b-type" #class variable
samsung=phone("samsung","10000",) 
samsung.display()

redmi=phone("redmi","10000",) 
redmi.display()

#common na change pannanum na use class variable
#ovveru object ku change agure visiyatha instance variable use panuga
