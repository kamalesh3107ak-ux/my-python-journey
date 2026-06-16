"""#instance method
class laptop():
    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

hp=laptop()
hp.setprice(60000)
hp.getprice()"""


class laptop():
    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

    @classmethod
    def changechargertype(cls):
        cls.chargertype="b-type"
        print("charger type changed to b")

    @staticmethod
    def info():
        print("this is laptop class")

hp=laptop()
hp.setprice(60000)
hp.getprice()

laptop.changechargertype()

hp.info()
