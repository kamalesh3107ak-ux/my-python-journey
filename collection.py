# python collections
"""list
tuble
set
dictionary"""

#list []

"""a=[10,20,30,40,50]
print(type(a))"""

#append add pana extra list la enna data type venalu add panikalam

"""a=[1,2,3,4,5]
print(a)
a.append(78)
print(a)
a.append("kamalesh")
print(a)"""

#need current position using a[]

"""a=[1,2,3,4,5,6,7,8,9,]
print(a[5])"""

# insert new number using insert

"""a=[1,2,3,4,5,6]
a.insert(0,11)
print(a)"""

#modify the number in position

"""a=[1,2,3,4,5,6]
a[1]=12
print(a)"""

#remove the number using pop

"""a=[1,2,3,4,5,6]
a.pop(5)
a.pop(1)
print(a)"""

#merge two list using extend

"""a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)"""

#tuble - not modify only casting ()

"""a=(1,2,3,4)
print(a)"""

"""a=(1,2,3,4,5)
a=list(a)
print(a)"""


#set - do not allowed dublicate , dublicate values romoved , only add,romove,pop elements {}
#set - unordered

"""a={1,2,3,4,1}
print(a)"""

#add

"""a={1,2,3,4,}
a.add(5)
print(a)"""

#remove

"""a={1,2,3,4,5}
a.remove(4)
print(a)"""

#pop

"""a={1,2,3,4,5,6}
a.pop()
print(a)"""

#dictionary - kry:value pair (get),(keys),(values),(add),(uppdate),(pop)

"""a={
    "name":"kamalesh"
}
print(a)"""

"""a={
    "name":"kamalesh"
}
print(a["name"])"""


"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul"
}
print(a)"""



"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
print(a["name"])
print(a["age"])
print(a["location"])
print(a["best friends"])"""

# only keys 

"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
print(a.keys())"""

#only values


"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
print(a.values())"""

#modify

"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
a["age"]=23
print(a)"""

#add

"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
a["colour"]="red"
print(a)"""

#update

"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
a.update({"age":23})
print(a)"""


#pop

"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
a.pop("age")
print(a)"""

"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
del a["age"]
print(a)"""

#clear complete dictionary

"""a={
    "name":"kamalesh",
    "age":21,
    "location":"dindigul",
    "best friends":["kamalesh","maha"]
}
a.clear()
print(a)"""

#largest and minimum
"""numbers = [10, 20, 30, 40, 50]

large =max(numbers)
min=min(numbers)
print("largest element :",large)
print("minimum element:",min)"""

#reversed numbers
"""numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.reverse()
print("reverse numbers:",numbers)"""

# sum of  5 numbers using list
"""numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
print("Sum of 5 numbers:", total)"""
 
#multiple the numbers

"""import math
numbers=[10,20,30,40,50]

multiple=math.prod(numbers)
print("multiple the numbers:",multiple)"""

#average
"""numbers = [10,20,30,40,50]
print("Average:", sum(numbers)/5)"""


# Sorting and reversing a list
"""marks = [56, 89, 45, 92, 67]
marks.sort()
print("Sorted:", marks)
marks.reverse()
print("Reversed:", marks)
"""

#matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][0])  
