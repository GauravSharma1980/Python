"""
In this section, we are discussing about,
4. Tuple:  We already have option to store collection of elements like list 0f names, list of email-ids etc
                    But we dont know how to use it
                    -IMMUTABLE: After creating the list, throught the program we CAN'T alter/modify
                        (we CAN'T add element / we CAN'T remove element / we CAN'T update element)
                    - Automatically index number will be assigned to each value we store

"""

print("Tuple PART - 1")
print("-"*20)
# ------------------------

my_tuple_1 = (10, 12.5, "Python", "Java", [100, 200])
# Or we can also use class name to create
my_tuple_2 = tuple([10, 12.5, "Python", "Java", [100, 200]])

print(my_tuple_1, my_tuple_2, sep="||")

print(40*"#", end="\n\n")
##########################

print("Tuple PART - 2")
print("-"*20)
# ------------------------

# ------------------------
# - Similar to strings, we have indexes in tuple as well
# - similar to strings, we can do slicing, reverse travesal etc
#   will work in tuple as welll
# ------------------------

print("Value at index 2 : ", my_tuple_1[2]) # Python
print("2nd  character of Value at index 2 : ", my_tuple_1[2][2]) # 't'

print("#"*40, end="\n\n")
##########################

print("Tuple PART - 4: Trying few methods")
print("-"*20)
# ------------------------

my_tuple_3 = ("Java","Python" ,"Java", "C++", "Java", "Java")
print("my_tuple_3 : ", my_tuple_3)

java_count = my_tuple_3.count('Java')
print("java_count : ", java_count)

index_of_python = my_tuple_3.index("Python")
print("index_of_python : ", index_of_python)

print("#"*40, end="\n\n")
##########################