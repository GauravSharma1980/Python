"""
# -----------------------------
# How to solve 2 cases
# -----------------------------
# Case - 1 : How to access variables outside the function
# Case - 2 : How to pass values to variables inside the function
# -----------------------------

"""

'''
In this section, we are discussing about
# Case - 1 : How to access variables outside the function
'''

import re


print("Function with 1 return")
print("#"*20)
##############################


def employee1():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    return name


received_value = employee1()
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------


print("Function with more than 1 return values - Tuple")
print("#"*20)
##############################


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    return name, company


received_value = employee()
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    return [name,company]


received_value = employee()
print("received_value as list: ", received_value)

print("-"*40, end="\n\n")
#-----------------------------


print("Function with more than 1 return values - DICT")
print("#"*20)
##############################


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    return {"name": name, "company":company}
# it can return any object we give it to return

received_value = employee()
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------

print("Function with without returning any values - None")
print("#"*20)
##############################


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    # 2 things about the return
    # 1. return the value which we provide
    # 2. end the function execution
    return # None
    

received_value = employee()
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------

print("Function with NO return statement - None")
print("#"*20)
##############################


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)


received_value = employee()
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------

print("Function with NO return statement - None")
print("#"*20)
##############################


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    return
    print("after return")


received_value = employee()
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------


print("Function with expression in return")
print("#"*20)
##############################


def employee():
    name = "emp-1"
    company = "XYZ Company"
    print("name : ", name)
    print("company : ", company)
    return (10+20)/(10-20) # return the result

received_value = employee()
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------