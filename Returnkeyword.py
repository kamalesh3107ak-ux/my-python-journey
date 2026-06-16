"""def painter():
    return "i am painter"
print(painter())"""

"""def valueofa():
    return 10
a=valueofa()
print(a)"""

#username&password

"""s_username="kamalesh"
s_password="123"
uname=(input("enter value for username:"))
password=(input("ener value for password:"))

def validate():
    if(s_username==uname and s_password==password):
        print("correct")
    else:
        print("wrong")
validate()"""


"""s_username="kamalesh"
s_password="123"
uname=(input("enter value for username:"))
password=(input("ener value for password:"))

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
     
a=validate()
print(a)"""

#(a+b)*c

def add(n1,n2):
    return(n1+n2)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

added=add(a,b)

output=added*c
print(output)