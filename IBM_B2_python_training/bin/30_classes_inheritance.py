"""
Single / Multi Level IMnheritance

class A:
    pass

class B(A):
    pass

class C(B):
    pass

n levels
"""

'''
Requirement: Extend existing class and add methods related to tax
1) add_tax 2) view_tax 3) Modify view_salary to return sal-tax
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

    @staticmethod
    def compute_avg_salary(sal1, sal2):
        return (sal1+sal2)/2


class NewEmployeeClass(Employee):
    def add_tax(self, t):
        self.tax = t
    def view_tax(self):
        return self.tax
    # POLYMORPHISM : We can reuse same name as super class
    def view_salary(self): # This will OVERRIDE super class method
        return self.salary - self.tax


# Requirement : store 2 employee details name,salary,company_name
# and print both employee details


Employee1 = NewEmployeeClass()
Employee2 = NewEmployeeClass()

Employee1.add_name('emp-1') # add_name(Employee1, 'emp-1') # self=Employee1
Employee1.add_salary(20000)
Employee1.add_tax(2000)

Employee2.add_name('emp-2')
Employee2.add_salary(22000)
Employee2.add_tax(2200)

print("employee_1_name : ", Employee1.view_name())
print("employee_1_salary : ", Employee1.view_salary())
print("employee_1_tax : ", Employee1.view_tax())
print("employee_1_company : ", NewEmployeeClass.company_name)

print("employee_2_name : ", Employee2.view_name())
print("employee_2_salary : ", Employee2.view_salary())
print("employee_2_tax : ", Employee2.view_tax())
print("employee_2_company : ", NewEmployeeClass.company_name)

NewEmployeeClass.add_company_ceo('CEO-1') # add_company_ceo(Employee, 'CEO-1')
Employee1.add_company_ceo('CEO-2')  # add_company_ceo(Employee, 'CEO-1')
Employee2.add_company_ceo('CEO-3') #  # add_company_ceo(Employee, 'CEO-1')
# We can call using any INSTANCE OBJECT,

print("Ceo Name : ", NewEmployeeClass.view_company_ceo()) # CEO-3
print("Ceo Name : ", Employee1.view_company_ceo())# CEO-3
print("Ceo Name : ", Employee2.view_company_ceo())# CEO-3

sal1 = Employee1.view_salary()
sal2 = Employee2.view_salary()
avg_sal = NewEmployeeClass.compute_avg_salary(sal1, sal2)
print("avg_sal : ", avg_sal)


print("-"*40)
# --------------------------

