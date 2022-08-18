"""
Static Methods
"""

'''
Requirement: add method to compute avg of 2 salaries.
Which means, we pass 2 values, function should return average

Here, No need of INSTANCE/CLASS OBJECT inside the method, so
we can use staticmethod whic will not pass either INSTANCE or CLASS OBJECT

@staticmethod to write static method
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

sal1 = Employee1.view_salary()
sal2 = Employee2.view_salary()
avg_sal = Employee.compute_avg_salary(sal1, sal2)
print("avg_sal : ", avg_sal)

print("-"*40)
# --------------------------

