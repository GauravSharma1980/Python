"""
In this section, we are discussing about,
3. list:  We already have option to store collection of elements like list 0f names, list of email-ids etc
                    But we dont know how to use it
                    - MUTABLE: After creating the list, throught the program we can alter/modify
                        (we can add element / we can remove element / we can update element)
                    - Automatically index number will be assigned to each value we store

"""

print("List PART - 1")
print("-"*20)
# ------------------------

my_list_1 = [10, 12.5, "Python", "Java", [100, 200]] # internally it will call list class to create object
# Or we can also use class name to create
my_list_2 = list([10, 12.5, "Python", "Java", [100, 200]])

print(my_list_1, my_list_2, sep="\n")

print("#"*40, end="\n\n")
##########################

print("List PART - 2")
print("-"*20)
# ------------------------

# ------------------------
# - Similar to strings, we have indexes in list as well
# - similar to strings, we can do slicing, reverse travesal etc
#   will work in list as welll
# ------------------------

print("Value at index 2 : ", my_list_1[2]) # Python
print("2nd  character of Value at index 2 : ", my_list_1[2][2]) # 't'

print("#"*40, end="\n\n")
##########################

print("List PART - 3")
print("-"*20)
# ------------------------

print(dir(my_list_1))

print("#"*40, end="\n\n")
##########################

print("List PART - 4 : Trying few methods")
print("-"*20)
# ------------------------

my_list_3 = ["Java", "Python", "C", "C++"]
print("my_list_3 : ", my_list_3)

# add "Perl"
my_list_3.append("PERL") # add at the end
print('my_list_3 after my_list_3.append("PERL") : ', my_list_3)

# update 3rd element "C" to "R"
my_list_3[2] = "R"
print('my_list_3 after update 3rd element "C" to "R" : ', my_list_3)

# remove C++ : from left, 1st occurance will be removed
my_list_3.remove('C++')
print("my_list_3 after my_list_3.remove('C++') : ", my_list_3)

print("#"*40, end="\n\n")
##########################
