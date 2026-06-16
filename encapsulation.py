class company():
    def __init__(self):
       self.__companyname="google" #private variable(__)
     
    def companyname(self):
        print(self.__companyname)# public variable 

c1=company()
c1.companyname()
print(c1.__companyname)

