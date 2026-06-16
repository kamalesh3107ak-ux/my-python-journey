#funtion - use def 

"""def painter():
    print("painting")
painter()"""

#add 

"""def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()"""

#sub

"""def sub():
    a=int(input())
    b=int(input())
    print(a-b)
sub()"""

#mul

"""def mul():
    a=int(input())
    b=int(input())
    print(a*b)
mul()"""

#div

"""def div():
    a=int(input())
    b=int(input())
    print(a/b)
div()"""

#onether concept (parameter funtion\ argument)

"""def painter(msg):
    print("message:",msg)
painter("paint my house")"""

#even or odd

"""
a=10
def findevenorodd(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")

findevenorodd(a)"""


"""a=int(input())
def findevenorodd(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")

findevenorodd(a)"""

#print range (user input for range)

def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
a=int(input("enter a :"))
b=int(input("enter b :"))
printrange(a,b)