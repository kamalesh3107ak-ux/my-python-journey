#syntex
#while condition:
    # statements

"""i=0
while(i==0):
    print(i)
    i=i+1"""

#1.
"""i=1
while(i<6):
    print(i)
    i=i+1"""

#2 (10,20,30,...200)

"""i=10
while(i<=10):
    print(i,end=",")
    i=i+10"""

#reverse order

"""i=10
while(i>0):
    print(i,end=",")
    i=i-1"""

#factorial number

"""i=3
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)"""


num = int(input("Enter Number: "))
sum = 0
while (num>0):
    digit = num%10
    sum=sum+digit
    num=num/10  

print(sum)