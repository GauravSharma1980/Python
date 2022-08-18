"""
Functions : If we want to rewrite same code MORE THAN ONE time then
instead of rewriting, we can keep that code in a block and reuse same
block whenever we want to execute that code
"""

print("Without using function")
print("#"*20)
##############################

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

print("-"*40, end="\n\n")
#-----------------------------

print("With using function")
print("#"*20)
##############################

def my_func():
    a = 10
    b = 20
    c = a + b
    print("c : ", c)
print("d",10)


my_func()
my_func()
my_func()
my_func()

print("Just another function")
print("#"*20)
##############################

def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    #employee()

employee()
employee()
employee()
employee()

name="Gaurav"
print(name)

print("-"*40, end="\n\n")
#-----------------------------


#-----------------------------
# Case-1
#-----------------------------
# We can't directly access any variables outside the function
# print("name value inside employee function = ", name)
#-----------------------------

#-----------------------------
# Case-2
#-----------------------------
# Assign some other name to variable 'name' present inside the function
# name = "emp-2" # It will create global variable, It will not change
#       variable 'name' inside the function
#-----------------------------

#-----------------------------
# How to solve 2 cases
#-----------------------------
# Case - 1 : How to access variables outside the function
# Case - 2 : How to pass values to variables inside the function
#-----------------------------

