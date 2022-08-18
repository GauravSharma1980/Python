"""
Instance Methods
"""

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

print("-"*40)
# --------------------------

