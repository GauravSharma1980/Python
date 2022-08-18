"""
Classes : Instance Objects and Instance Variables
"""

class Employee:
    company_name = "XYZ Company"
    def __init__(self, n, s):
        self.name = n
        self.salary =s

# Requirement : store 2 employee details name,salary,company_name
# and print both employee details


Employee1 = Employee('emp-1', 20000)
Employee2 = Employee('emp-2', 22000)

print("employee_1_name : ", Employee1.name)
print("employee_1_salary : ", Employee1.salary)
print("employee_1_company : ", Employee.company_name)

print("employee_2_name : ", Employee2.name)
print("employee_2_salary : ", Employee2.salary)
print("employee_2_company : ", Employee.company_name)

print("-"*40)
# --------------------------

# POINT-1
# --------------------------
# - There is a builtin class called 'object'
# - Inside 'object' class, we have many methods, in that 2 methods are
#   1) __new__ # Construct the Object
#   2) __init__ # Initialize the Object
# - All our classes are by default inherited from object class
#
# - whenever we create object like
# 1           Employee1 = Employee('emp-1', 20000)
#           internally it calls 2 methods
#            1) Employee1 = __new__() create and store
#            2) __init__(Employee1, 'emp-1', 20000) # self = Employee1 n=emp1 s=20000
#               self.name -> Employee1.name='emp-1'
#               self.salary -> Employee1.salary=20000
#
# 2           Employee2 = Employee('emp-2', 22000)
#           internally it calls 2 methods
#            1) Employee2 = __new__() create and store
#            2) __init__(Employee2, 'emp-2', 22000) # self = Employee2 n=emp2 s=22000
#               self.name -> Employee2.name='emp-2'
#               self.salary -> Employee2.salary=22000
# --------------------------

# POINT-2
# --------------------------
# - Totally we have 3 objects 1) Employee 2) Employee1 3) Employee2
# - CLASS OBJECTS : 1) Employee
# - CLASS VARIABLE : company_name
# - INSTANCE OBJECTS : 1) Employee1 2) Employee2
# - INSTANCE VARIABLES : name, salary
# --------------------------

# POINT-3
# --------------------------
# - whatever the data we are storing in CLASS OBJECT can be accessed
#   using INSTANCE OBJECTS
# - CLASS OBJECT is like common place for all INSTANCE OBJECTS
# - Data whichever is common for for INSTANCE OBJECTS, those data we can keep
# - in our class, compny_name was common for all INSTANCE OBJECTS, so we stored in
#   CLASS OBJECT
# --------------------------

print("Access company_name using CLASS OBJECT Employee : ", Employee.company_name)
print("Access company_name using INSTANCE OBJECT Employee1 : ", Employee1.company_name)
print("Access company_name using INSTANCE OBJECT Employee2 : ", Employee2.company_name)
