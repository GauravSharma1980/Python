"""
apart from example 17 & 18,
other possible combinations of arguments
"""

print("Both Positional & keyword args")
print("#"*20)
##############################

# a,b are positional
# c, d are keyword
def add(a, b, *, c, d):
    return a + b + c + d

result = add(10, 20, d=40, c=30)
print("result : ", result)

print("-"*40, end="\n\n")
#-----------------------------

print("Both Positional & keyword args")
print("#"*20)
##############################

# a,b are positional
# *c is variable positional

# d, e are keyword
def add(a, b, *c, d, e):
    return a + b + sum(c) + d + e

result = add(10, 20, 30, 40, 50, 60, d=40, e=30)
print("result : ", result)

print("-"*40, end="\n\n")
#-----------------------------

print("zero or more Positional & keyword args")
print("#"*20)
##############################

# a,b are positional
# *c is variable positional

# d, e are keyword
def add(*c, d, e):
    return sum(c) + d + e

result = add(10, 20, 30, 40, 50, 60, d=40, e=30)
print("result : ", result)

print("-"*40, end="\n\n")
#-----------------------------

print("zero or more Positional")
print("#"*20)
##############################


# *c is variable positional

def add(*c):
    return sum(c)

result = add(10, 20, 30, 40, 50, 60)
print("result : ", result)

print("-"*40, end="\n\n")
#-----------------------------


print("zero or more keyword args")
print("#"*20)
##############################


# **c is variable keyword

def add(**c):
    return sum(c.values())

result = add(a=10, b=20, c=30, d=40, e=50, f=60)
print("result : ", result)

print("-"*40, end="\n\n")
#-----------------------------

print("zero or more positional args and zero or more keyword args")
print("#"*20)
##############################

# * a is zero or more positional
# **b # * a is zero or more keyword args

def add(*a,**b):
    return sum(a)+sum(b.values())

result = add(10, 20, 30, 40, 50, 60, a=10, b=20, c=30, d=40, e=50, f=60)
print("result : ", result)

print("-"*40, end="\n\n")
#-----------------------------
