"""
In this section, we are discussing about,
1. Numbers : We already have option to store numbers like int, float.
                    But we dont know how to use it
                    - IMMUTABLE
"""

print("Numbers PART - 1")
print("-"*20)
# ------------------

# Everything is object
a = 10 # Internally it will create predefined class object 'int' with a value 10
b = 12.5 # Internally it will create predefined class object 'float' with a value 12.5
c = int(10) # same as c = 10
d = float(12.5) # same as d = 12.5
print(a, b, c, d)

print("#"*40, end="\n\n") # end="\n\n" : after printing everything at the end put 2 \n
################

print("About print function - Example - 1")
print("-"*20)
# ------------------
a = 100 # previouse object with value 10, will go for garbage collection
b = 200
c = 300
d = 400
print(a, b, c, d) # default separator is SPACE
print(a, b, c, d, sep="|")
print(a, b, c, d, sep="X")
print(a, b, c, d, sep=",")
print(a, b, c, d, sep="XYZ")
print("#"*40, end="\n\n")

print(a,b,c,d)

print(a, b, c, d) # end="\n" : After printing all the values, at the end put '\n'
print(a, b, c, d, end=".")  # end="." : After printing all the values, at the end put '.'
print(a, b, c, d, end="X")  # end="X" : After printing all the values, at the end put 'X'
print(a, b, c, d)
# Total  we can pass 4 parameters to print function
# 1) sep 2) end 3) file 4) flush
# file & flush we will discuss during file operations
print("#"*40, end="\n\n")
################

import sys

print("total ref",sys.getrefcount(300))

################################

print("Garbage Collection")
print("-"*20)
# ------------------
a = 100
print("Reference ID of a is : ", id(a))
print("value at a is : ", a)
print("-"*10)
b = a
print("Reference id of a after b = a is : ", id(a)) # Same
print("Reference id of b after b = a is : ", id(b)) # same
print("-"*10)
a = 200
print("Reference id of a after a = 200 is : ", id(a))
print("Reference id of b after a = 200 is : ", id(b))
print("-"*10)
#b = 300
print("Reference ID of b after b = 300 : ", id(b))
print("-"*10)
import sys
print("Total number of reference refering to b is : ", sys.getrefcount(b))
print("-"*10)
x = 100
y = 200
z = x + y
print("Value of z is : ", z)
print("ID of z is : ", id(z))
print("Total number of reference refering to b is : ", sys.getrefcount(b))
print("-"*10)
print("#"*40, end="\n\n")
################