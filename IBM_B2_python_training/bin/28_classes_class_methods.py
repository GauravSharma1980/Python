"""
Class Methods
"""

'''
Requirement: Add method to store company_ceo_name
'''

'''
- On which object (INSTANCE/CLASS OBJECT), we need to store company_ceo_name ?
- Since it is common for all INSTANCES, we can keep this in CLASS OBJECT
'''

'''
By default, all methods are instance methods which takes 'self' as first param,eter
NOW,
we need a method whhich takes CLASS OBJECT as first arg.

- We can make use of @classmethod decorator. This is will take care of sending
    CLASS OBJECT as 1st parameter
'''


class Employee:
    company_name = "XYZ Company"

    def add_name(self, n):
        self.name = n

    def view_name(self):
        return self.name

    def add_salary(self, s):
        self.salary = s

    def view_salary(self):
        return self.salary

    @classmethod
    def add_company_ceo(cls, n):
        cls.ceo_name = n

    @classmethod
    def view_company_ceo(cls): # cls=Employee
        return cls.ceo_name

# Requirement : store 2 employee details name,salary,company_name
# and print both employee details


Employee1 = Employee()
Employee2 = Employee()

Employee1.add_name('emp-1') # add_name(Employee1, 'emp-1') # self=Employee1
Employee1.add_salary(20000)

Employee2.add_name('emp-2')
Employee2.add_salary(22000)

print("employee_1_name : ", Employee1.view_name())
print("employee_1_salary : ", Employee1.view_salary())
print("employee_1_company : ", Employee.company_name)

print("employee_2_name : ", Employee2.view_name())
print("employee_2_salary : ", Employee2.view_salary())
print("employee_2_company : ", Employee.company_name)

Employee.add_company_ceo('CEO-1') # add_company_ceo(Employee, 'CEO-1')
Employee1.add_company_ceo('CEO-2')  # add_company_ceo(Employee, 'CEO-1')
Employee2.add_company_ceo('CEO-3') #  # add_company_ceo(Employee, 'CEO-1')
# We can call using any INSTANCE OBJECT,

print("Ceo Name : ", Employee.view_company_ceo()) # CEO-3
print("Ceo Name : ", Employee1.view_company_ceo())# CEO-3
print("Ceo Name : ", Employee2.view_company_ceo())# CEO-3

print("-"*40)
# --------------------------
