"""for i in "kamalesh":
    print (i)"""

# i = variable (change any value)

#range

"""for i in range (1,5):
    print(i)"""

# 2*matrix
"""for i in range (1,11):
    print(i,"*2=",i*2)"""

#3*matrix
"""for i in range (1,11):
    print(i,"*3=",i*3)"""

#examples of for loop

"""a = int(input())
b = int(input())
for i in range(a+1,b):#particular range 
    print(i)"""

#even number
"""
for i in range(1,11):
    if(i%2==0):
        print(i)"""

#odd number
"""for i in range(1,11):
    if(i%2!=0):
        print(i)"""

#count

"""count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
        print(count)

count=0
for i in range(1,5):
    if(i%2==0):
        count=count+1
        print(count)"""

#even and add count

"""e_count=0
o_count=0
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
        print(e_count)
        print(o_count)"""

"""count=0
for i in range(1,100):
    if(i%3==0 and i%5==0):
        count=count+1
        print(count)"""

#sum of natural numbers

"""sum=0
for i in range (1,6):
    sum=sum+i
print(sum)"""

#sum and average  (for loop using list)

"""a=[]
a.append(10)
a.append(20)
a.append(30)
a.append(40)
b=int(input())
a.append(b)
print(a)"""

"""for i in range (10):
    print(i)"""

"""a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(a)"""

"""a=[]
print("enter 10 numbers:")
for i in range(5):
    num=int(input("enter num" + str(i+1)))
    a.append(num)
print(a)"""

"""sum=0
for i in a:
    sum=sum+i
print(sum)"""

#class mentor examples

"""for i in range (1,11):
        print(i,"*2=",i*2,)"""

"""sum=0
n=int(input("enter the natural numbers of terms"))
print("the first",n,"natural numbers are:")
for i in range (1,n+1):
    print(i,end="")
    sum+=i
    print("\nthe sum of natural numbers:",sum)"""

"""n=int(input("number of terms"))
for i in range(1,n+1):
  print("number is:",i,"and cube of the",i,"is:",i*i*i)"""

#triangle 
"""n=5
for i in range(1,n+1):
    for j in range (n-1):
        print(" ",end="")
    for k in range (i):
        print("*",end="")
    print()"""
    
#reverse order    

"""n=5
for i in range(n,0,-1):
    for j in range (n-1):
        print(" ",end="")
    for k in range (i):
        print("* ",end="")
    print()

n=5
for i in range(1,n+1):
    for j in range (n-1):
        print(" ",end="")
    for k in range (i):
         print("*",end="")
    print() """


"""n=5
for i in range(1,n+1):
  print("*"*i)"""

#reverse order

"""n=5
for i in range(n,0,-1):
  print("*"*i)"""


"""n=5
for i in range(1,n+1):
  print("*"*i)"""

#pramid
"""n=5
for i in range(1,n+1):
 print(" " * (n-i),end="")
 print("* " *i)"""

#pramid reverse
"""n=5
for i in range(n,0,-1):
 print(" " * (n-i),end="")
 print("* " *i)"""

 #dimend

"""n=5
for i in range(1,n+1):
 print(" " * (n-i),end="")
 print("* " *i)
 n=5
for i in range(n,0,-1):
 print(" " * (n-i),end="")
 print("* " *i)"""


# alphepet L
"""for i in range(0,8):
  print("*")
n=8
for i in range(1,n+1):
 print("* ",end="")"""

#  Alphabet A-Z
"""for i in range(65, 91):
    print(chr(i), end=" ")"""


# 25. Pattern 1, 12, 123
"""for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
"""

#pramid
"""n = 5
for i in range(1, n+1):
    pattern = "* " * i
    print(pattern.center(n*2))"""


"""for i in range(1,11):
    print(i)"""


#sum of digit in number
"""a = 522
sum = 0

for i in str(a):
    sum = sum + int(i)

print(sum)"""

#Fibonacci series

"""a = 0
b = 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c"""

#amstrong number 

"""num = int(input("number"))
a = num     

sum = 0

for i in range(3):  
    digit = num % 10
    sum += digit ** 3
    num //= 10

print("Armstrong" if sum == a else "Not Armstrong")"""


#reverse the string 
"""s = input("Enter string: ")
print(s[::-1])"""


#palindrom
"""a = input("Enter a string: ")
if (a.lower() == a.lower()[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")"""

#factorial number

"""n = 5
a = 1
for i in range(1,n+1):
    a = a* i

print(a)"""


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print( a,b)

