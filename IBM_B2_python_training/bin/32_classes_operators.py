"""
There will be a name given for each operator, those name startswith
 __ and endswith __.  for example
+ -> __add__

Now, if we want to support for + then we need to add __ method inside our class
"""

print("ERROR : adding 2 employee objects")
print("-"*20)
# ------------------------

class Employee:
    def __init__(self, n):
        self.name = n


e1 = Employee('emp-1')
e2 = Employee('emp-2')
# result = e1 + e2 # ERROR
# print("result : ", result)

'''
Traceback (most recent call last):
  File "C:\IBM_B2_python_training\bin\32_classes_operators.py", line 16, in <module>
    result = e1 + e2
TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
'''
print("-"*40, end="\n\n")
# ------------------------

print("ERROR : adding 2 employee objects")
print("-"*20)
# ------------------------

class Employee:
    def __init__(self, n):
        self.name = n
    def __add__(self, other): # # __add__(e1, e2) -> self=e1, other=e2
        return self.name + other.name
    def __len__(self):
        return len(self.name) # self.name='emp-1'
    def __str__(self):
        return self.name

e1 = Employee('emp-1')
e2 = Employee('emp-2')
result = e1 + e2 # Internally it e1.__add__(e2)
print("result : ", result)

print("e1 is : ", e1)
print("Length of e1 : ", len(e1))


print("-"*40, end="\n\n")
# ------------------------
