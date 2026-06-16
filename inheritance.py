#  oru class la irukuratha inoru class access pana muducha athutha inheritance

"""class dad():
    def phone (self):
        print("dads phone")

class son():
    def laptop(self):
        print("sons laptop")

ram=son()
ram.laptop()"""

# single inheritance

"""class dad():
    def phone (self):
        print("dads phone")

class son(dad): # dad is link in two classes
    def laptop(self):
        print("sons laptop")

ram=son()
ram.phone()"""

#multiple inheritance

"""class dad():
    def phone (self):
        print("dads phone")

class mom():
    def sweet(self):
        print("moms sweet")

class son(dad,mom): # dad is link in two classes
    def laptop(self):
        print("sons laptop")

ram=son()
ram.phone()
ram.sweet()"""

#multi level inheritance
"""
class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("dads money")

class son(dad):
    def laptop(self):
        print("sons laptop")

ram = son()
ram.laptop()
ram.money()
ram.phone()

d1=dad()
d1.phone()"""

#hirarchy inheritance

"""class dad():
    def money(self):
        print("dad money")

class son1(dad):
    pass


class son2(dad):
    pass


class son3(dad):
    pass


s2=son2()
s2.money()"""

#hybrid inheritance

class dad():
    def money(self):
        print("dad money")

class land():
    def important(self):
        print("important land")

class son1(dad,land):
    pass


class son2(dad):
    pass


class son3(dad):
    pass 


s1=son1()
s1.money()
s1.important()




