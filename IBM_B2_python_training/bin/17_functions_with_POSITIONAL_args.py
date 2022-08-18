"""
In this section, we are discussing about,
# Case - 2 : How to pass values to variables inside the function
"""
'''
2 ways to pass values
1-way is we can pass only values
2nd way is we can pass values in the form of key/value pair
'''
'''
In this section, we are discussing about
1-way is we can pass only values
'''

print("Function with POSITIONAL ARGUMENTS")
print("#"*20)
##############################

# name, company are called POSITIONAL ARGUMENTS
def employee(name, company):
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee('emp-1', "XYZ Company") # pass values in the same sequence as definition
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------

print("Function with POSITIONAL ARGUMENTS with default values")
print("#"*20)
##############################

# name, company are called POSITIONAL ARGUMENTS
# order: 1st non-default then default args will come
def employee(name, company="XYZ Company"):
    print("name : ", name)
    print("company : ", company)
    return [name, company]


received_value = employee('emp-1') # company will make use of default values
print("received_value : ", received_value)

received_value = employee('emp-1', "XYZ Company")
print("received_value : ", received_value)

received_value = employee('emp-1', "ABC Company")
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------

print("Function with VARIABLE POSITIONAL ARGUMENTS")
print("#"*20)
##############################


# *prev_companies called VARIABLE POSITIONAL ARGUMENTS
def employee(name, company="XYZ Company", *prev_companies):
    print("name : ", name)
    print("company : ", company)
    print("prev_companies : ", prev_companies)
    return [name, company, prev_companies]


received_value = employee('emp-1') # company="XYZ Company", prev_companies=()
print("received_value : ", received_value)

received_value = employee('emp-1', "XYZ Company") # company="XYZ Company", prev_companies=()
print("received_value : ", received_value)

received_value = employee('emp-1', "ABC Company") # company="ABC Company", prev_companies=()
print("received_value : ", received_value)

received_value = employee('emp-1', "ABC Company", "comp-1")
# company="ABC Company", prev_companies=("comp-1")
print("received_value : ", received_value)

received_value = employee('emp-1', "ABC Company", "comp-1", "comp-2", "comp-3")
# company="ABC Company", prev_companies=("comp-1","comp-2", "comp-3")
print("received_value : ", received_value)

print("-"*40, end="\n\n")
#-----------------------------

