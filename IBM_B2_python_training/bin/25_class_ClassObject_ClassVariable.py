"""
Class : Class Object and Class Variable
"""

print("Without using class")
print("#"*20)
############################

# Requirement : store 2 employee details name,salary,company_name
# and print both employee details

company_name = "XYZ Company"

employee_1_name = "emp-1"
employee_1_salary = 20000

employee_2_name = "emp-2"
employee_2_salary = 22000

print("employee_1_name : ", employee_1_name)
print("employee_1_salary : ", employee_1_salary)
print("employee_1_company : ", company_name)

print("employee_2_name : ", employee_2_name)
print("employee_2_salary : ", employee_2_salary)
print("employee_2_company : ", company_name)

print("-"*40)
# --------------------------

print("Using class")
print("#"*20)
############################

# Requirement : store 2 employee details name,salary,company_name
# and print both employee details


class Company:
    name = "XYZ Company"


class Employee1:
    name = "emp-1"
    salary = 20000


class Employee2:
    name = "emp-2"
    salary = 22000

# Automatically for each class it will create object with the class name
# so totally 3 objects are created 1) Company 2) Employee1 3) Employee2
# CLASS VARIABLES : name, salary
# CLASS OBJECTS : 1) Company 2) Employee1 3) Employee2


print("employee_1_name : ", Employee1.name)
print("employee_1_salary : ", Employee1.salary)
print("employee_1_company : ", Company.name)

print("employee_2_name : ", Employee2.name)
print("employee_2_salary : ", Employee2.salary)
print("employee_2_company : ", Company.name)

print("-"*40)
# --------------------------
