"""
Multiple Inheritance

class A:
    pass

class B:
    pass

# inheriting from more than one class
class C(A,B):
    pass
"""

'''
Requirement : Extend NewEmployeeClass and 
    add methods for phone_no and email_id

NOTE: we can make use of PersonalDetailsClass class for phone_no
but methods for email-id, we need to write
'''

class PersonalDetailsClass:
    def add_phone_no(self, pn):
        self.phne_no = pn
    def view_phone_no(self):
        return self.phne_no


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


class BrandNewEmployeeClass(NewEmployeeClass, PersonalDetailsClass):
    def add_email_id(self, em):
        self.email = em
    def view_email_id(self):
        return self.email


# Requirement : store 2 employee details name,salary,company_name
# and print both employee details


Employee1 = BrandNewEmployeeClass()
Employee2 = BrandNewEmployeeClass()

Employee1.add_name('emp-1') # add_name(Employee1, 'emp-1') # self=Employee1
Employee1.add_salary(20000)
Employee1.add_tax(2000)

Employee2.add_name('emp-2')
Employee2.add_salary(22000)
Employee2.add_tax(2200)

print("employee_1_name : ", Employee1.view_name())
print("employee_1_salary : ", Employee1.view_salary())
print("employee_1_tax : ", Employee1.view_tax())
print("employee_1_company : ", BrandNewEmployeeClass.company_name)

print("employee_2_name : ", Employee2.view_name())
print("employee_2_salary : ", Employee2.view_salary())
print("employee_2_tax : ", Employee2.view_tax())
print("employee_2_company : ", BrandNewEmployeeClass.company_name)

BrandNewEmployeeClass.add_company_ceo('CEO-1') # add_company_ceo(Employee, 'CEO-1')
Employee1.add_company_ceo('CEO-2')  # add_company_ceo(Employee, 'CEO-1')
Employee2.add_company_ceo('CEO-3') #  # add_company_ceo(Employee, 'CEO-1')
# We can call using any INSTANCE OBJECT,

print("Ceo Name : ", BrandNewEmployeeClass.view_company_ceo()) # CEO-3
print("Ceo Name : ", Employee1.view_company_ceo())# CEO-3
print("Ceo Name : ", Employee2.view_company_ceo())# CEO-3

sal1 = Employee1.view_salary()
sal2 = Employee2.view_salary()
avg_sal = BrandNewEmployeeClass.compute_avg_salary(sal1, sal2)
print("avg_sal : ", avg_sal)


Employee1.add_phone_no('111111')
Employee2.add_phone_no('22222')

Employee1.add_email_id('a@b')
Employee2.add_email_id('b@c')

print('Employee1 phone : ', Employee1.view_phone_no())
print('Employee1 email : ', Employee1.view_email_id())

print('Employee2 phone : ', Employee2.view_phone_no())
print('Employee2 email : ', Employee2.view_email_id())

print("-"*40)
# --------------------------

# --------------------------
import pandas as pd
class MyDataFrame(pd.DataFrame):
    def add_my_name(self, n):
        self.name = n
    def view_my_name(self):
        return self.name

my_df = MyDataFrame()
my_df.add_my_name('XYZ')
print("MyName is : ", my_df.view_my_name())
# --------------------------

print(dir(my_df))