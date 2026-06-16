"""mark = int(input())
if(mark>35):
    print("pass")
else:
    print("fail")"""

"""income = int(input("income:"))
if(income>7000):
    print("scholourship are available")
else:
    print("not available")"""

#divisible by number

"""a = 15
print(a/2)"""

# remainder (using mod %)

"""print(11%2)
print(10%3)
print(15%3)
print(16%3)"""

"""a = int(input())
if(a%3==0 & a%5==0):
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")"""

# even or odd number

"""num = int(input())
if(num%2==0):
    print("even")
else:
    print("odd")"""

"""score = int(input("score:"))
if (score<35):
    print("poor student")
if(score>35 and score<70):
    print("average student")
if(score>70):
    print("best student")"""

#elif

"""score = int(input("score:"))
if (score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
if(score>70):
    print("best student")"""

"""score = int(input("score:"))
if (score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
elif(score>70 and score<100):
    print("best student")
else:
    print("invalid score")"""

"""a = int(input("a:"))
b = int(input("b:"))
op =(input("add/sub/mul/div:"))
if(op=="add"):
     print(a+b)
elif(op=="sub"):
     print(a-b)
elif(op=="mul"):
     print(a*b)
elif(op=="div"):
     print(a/b)
else:
     print("invalid")"""

"""score = int(input())
if(score>=70):
    name=(input("enter your name:"))
    age=(input("enter your age:"))
    location=(input("enter your location:"))
    print("eligible")
else:
    print("not eligible")"""

#nested if 

"""salary =int (input("salary:"))
age =int (input("age:"))
if(salary>=20000 or age<=25):
    loan =int(input("loan:"))
    if(loan<=50000):
        print("eligible for loan")
    else:
        print("max amount")
else:
    print("not eligible")"""

"""a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f= (a+b+c+d+e)/5
if(f<35):
    print("additional class po")
else:
    print("you are good to go")"""



#06:10:2025
# 1. Positive or Negative

"""a = int(input("Enter a number: "))
if a > 0:
    print("Positive")
else:
    print("Negative")"""
    

# 2. Even or Odd
"""
a = int(input("Enter number: "))
if (a % 2 == 0):
    print("Even")
else:
    print("Odd")
"""

# 3. Divisible by 5
"""
b = int(input("Enter number: "))
if (b % 5 == 0):
    print("Divisible by 5")
else:
    print("Not divisible by 5")"""

"""
# 4. Greatest of two numbers

a = int(input("A: "))
b = int(input("B: "))
if ( a > b):
    print("A is greater")
else:
    print("B is greater")

"""

# 5. Multiple of 3 and 7

"""
a = int(input("Enter number: "))
if (a % 3 == 0 and a % 7 == 0):
    print("Multiple of 3 and 7")
else:
    print("Not multiple of 3 and 7")"""


# 6. Zero, Positive or Negative

"""k = int(input("Enter number: "))
if (k > 0):
    print("Positive")
elif (k == 0):
    print("Zero")
else:
    print("Negative")"""

# 7. Eligible to vote

"""age = int(input("Enter age: "))
if (age >= 18):
    print("Eligible to vote")
else:
    print("Not eligible")"""

# 8. Number within range
"""
n = int(input("Enter number: "))
if 1 <= n <= 100:
    print("In range")
else:
    print("Out of range")"""

# 9. Divisible by 2 and 3

"""n = int(input("Enter number: "))
if (n % 2 == 0 and n % 3 == 0):
    print("Divisible by 2 and 3")
else:
    print("Not divisible")"""


# 10. Leap year

"""year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not leap year")"""

# 11. Compare two strings

"""a = input("String 1: ")
b = input("String 2: ")
if a == b:
    print("Same")
else:
    print("Different")"""


# 12. Vowel or Consonant

"""ch = input("Enter letter: ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")"""


# 13. Single, Double, or Triple digit
"""n = int(input("Enter number: "))
if n < 10:
    print("Single digit")
elif n < 100:
    print("Double digit")
else:
    print("Triple digit or more")"""




# 14. Number ends with 5
"""n = int(input("Enter number: "))
if (n % 10 == 5):
    print("Ends with 5")
else:
    print("Does not end with 5")"""



# 15. Smallest of three numbers
"""a,b,c = map(int,input("Enter 3 numbers: ").split())
if a<b and a<c:
    print("A is smallest")
elif b<c:
    print("B is smallest")
else:
    print("C is smallest")"""

"""a,b =  (input("enter two numbers ").split())
if a == b:
    print("Same")
else:
    print("Different")"""
