#exception handling - error handling
# 3 type of errors 
# compile time error 

"""print("kamalesh")
print("maha")
print("best friends")
printt("1331")  #error 
"""

#logical error 

"""a=10
b=20
print(a+a)""" #logical error

# run time error
"""
a = int(input())
b = int(input())
print(a+b)"""

"""
try:
    a = int(input())
    b = int(input())
    print(a+b)
except Exception:
    print("something")"""

"""

try:
    a = int(input())
    b = int(input())
    print(a+b)
except Exception as e :
    print("something",e)"""


"""try:
    a = (input())
    b = (input())
    print(a/b)
except Exception as e :
    print("something",e)"""

#type error
"""
try:
    a = int(input())
    b = int (input())
    c = input ()
    print(a/c)
except ValueError as e :
    print("valueerror",e)
except TypeError as e:
    print("typeerror",e)"""

#name error
"""try:
    a = int(input())
    b = int (input())
    c = input ()
    print(d)
except ValueError as e :
    print("valueerror",e)
except TypeError as e:
    print("typeerror",e)
except Exception:
    print("something wrong")"""


#finally
try:
    a = int(input())
    b = int (input())
except ValueError as e :
    print("valueerror",e)
except Exception:
    print("something wrong")
finally:
    print("done")
