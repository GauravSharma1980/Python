'''
In this section, we are discussing about,
2nd way is we can pass values in the form of key/value pair
'''

print("Function with KEYWORD ARGUMENTS")
print("#"*20)
##############################

# name, company are called KEYWORD ARGUMENTS
def employee(*, name, company):
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee(name='emp-1', company="XYZ Company")
print("received_value : ", received_value)

received_value = employee(company="XYZ Company", name='emp-1')
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------


print("Function with KEYWORD ARGUMENTS with default values")
print("#"*20)
##############################

# name, company are called KEYWORD ARGUMENTS
def employee(*, name, company="XYZ Company"):
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee(name='emp-1') # company will make use of default values
print("received_value : ", received_value)

received_value = employee(name='emp-1', company="XYZ Company")
print("received_value : ", received_value)

received_value = employee(name='emp-1', company="ABC Company")
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------


print("Function with VARIABLE KEYWORD ARGUMENTS")
print("#"*20)
##############################


# **prev_companies called VARIABLE KEYWORD ARGUMENTS
def employee(*, name, company="XYZ Company", **prev_companies):
    print("name : ", name)
    print("company : ", company)
    print("prev_companies : ", prev_companies)
    return [name, company, prev_companies]


received_value = employee(name='emp-1') # company="XYZ Company", prev_companies={}
print("received_value : ", received_value)

received_value = employee(name='emp-1', company="XYZ Company") # company="XYZ Company", prev_companies={}
print("received_value : ", received_value)

received_value = employee(name='emp-1', company="ABC Company") # company="ABC Company", prev_companies={}
print("received_value : ", received_value)

received_value = employee(name='emp-1', company="ABC Company", c1="comp-1")
# company="ABC Company", prev_companies={c1:"comp-1"}
print("received_value : ", received_value)

received_value = employee(name='emp-1', company="ABC Company", c1="comp-1", c2="comp-2", c3="comp-3")
# company="ABC Company", prev_companies={c1:"comp-1",c2:"comp-2", c3:"comp-3"}
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------