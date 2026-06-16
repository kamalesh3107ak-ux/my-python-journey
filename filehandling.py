#read
"""f=open("fruits.txt")
print(f.read())"""

#write
"""f=open("fruits.txt","w")
f.write("banana\n")
f.write("mango")
f.close()
f=open("fruits.txt","r+")
print(f.read())"""

"""
#append
f=open("fruits.txt","a")
f.write("apple\n")
f.write("orange")
f.close()
f=open("fruits.txt","r+")
print(f.read())
"""

#readline
f=open("fruits.txt","a")
f.write("apple\n")
f.write("orange")
f.close()
f=open("fruits.txt","r+")
print(f.readline())
