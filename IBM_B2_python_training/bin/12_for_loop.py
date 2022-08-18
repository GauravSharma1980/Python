"""
for loop : To iterate ny collection like str, list, tuple, dict etc
"""

print("print each character without using for loop")
print("-"*20)
# -------------------

my_string = "Python"
print("my_string : ", my_string)

print("Each char : ", my_string[0])
print("Each char : ", my_string[1])
print("Each char : ", my_string[2])
print("Each char : ", my_string[3])
print("Each char : ", my_string[4])
print("Each char : ", my_string[5])

print("#"*40)
#####################

print("print each character using for loop")
print("-"*20)
# -------------------

my_string = "Python"
print("my_string : ", my_string)

for each_char in my_string[::-1]:
    print("each_char : ", each_char,end="")

print("#"*40)
#####################

# -------------------
# list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(2,10))
# [2, 3, 4, 5, 6, 7, 8, 9]
# list(range(2,10,2))
# [2, 4, 6, 8]
# -------------------

print("print each element in list/tuple/set/any other collection")
print("-"*20)
# -------------------

my_courses = ["Java", "C", "C++", "Python"]
print("my_courses : ", my_courses)

for each_course in my_courses:
    print("each_course : ", each_course)

print("#"*40, end="\n\n")
#####################



print("Dictionary : my_dict.keys() ")
print("-"*20)
# -------------------

my_dict = {"course": "Python", "duration": 10, "mode": "online"}
print("my_dict : ", my_dict)
# >>> my_dict = {"course": "Python", "duration": 10, "mode": "online"}

# >>> my_dict.keys()
# dict_keys(['course', 'duration', 'mode'])

for each_key in my_dict.keys():
    print("each_key : ", each_key)
    print("Value for each_key is : ", my_dict[each_key])

print("#"*40, end="\n\n")
#####################


print("Dictionary : my_dict.values() ")
print("-"*20)
# -------------------

my_dict = {"course": "Python", "duration": 10, "mode": "online"}
print("my_dict : ", my_dict)
# >>> my_dict = {"course": "Python", "duration": 10, "mode": "online"}

# >>> my_dict.values()
# dict_values(['Python', 10, 'online'])
for each_value in my_dict.values():
    print("each_value : ", each_value)

print("#"*40, end="\n\n")
#####################


print("Dictionary : my_dict.items() ")
print("-"*20)
# -------------------

my_dict = {"course": "Python", "duration": 10, "mode": "online"}
print("my_dict : ", my_dict)
# >>> my_dict = {"course": "Python", "duration": 10, "mode": "online"}

# >>> my_dict.items()
# dict_items([('course', 'Python'), ('duration', 10), ('mode', 'online')])
for each_item in my_dict.items():
    print("Each Item : ", each_item) # ('course', 'Python')
    print("Key in Each Item : ", each_item[0])
    print("Value in Each Item : ", each_item[1])

print("#"*40, end="\n\n")
#####################

print("Dictionary : my_dict.items() - 2nd way")
print("-"*20)
# -------------------

my_dict = {"course": "Python", "duration": 10, "mode": "online"}
print("my_dict : ", my_dict)
# >>> my_dict = {"course": "Python", "duration": 10, "mode": "online"}

# >>> my_dict.items()
# dict_items([('course', 'Python'), ('duration', 10), ('mode', 'online')])
for each_key, each_value in my_dict.items():
    print("Key in Each Item : ", each_key)
    print("Value in Each Item : ", each_value)

print("#"*40, end="\n\n")
#####################

# 2 Cases
# -------------------
# Case - 1 : break : to stop for loop in between
# Case - 2 : continue : in between if we want to send/jump to next iteration
# -------------------

print("Case - 1 : break : to stop for loop in between")
print("-"*20)
# -------------------

my_courses = ["C", "Java-1", "C++", "Java-2", "Python"]
print("my_courses : ", my_courses)

# Requirement: Findout are there any element which is starting with 'Java',
# if one element found then not require to verify other element.

for each_course in my_courses:
    if each_course.startswith("Java"):
        print("Found and course name is : ", each_course)
        break

print("#"*40, end="\n\n")
#####################

print("Case - 2 : continue : in between if we want to send/jump to next iteration")
print("-"*20)
# -------------------

my_courses = ["C", "Java-1", "C++", "Java-2", "Python"]
print("my_courses : ", my_courses)

for each_course in my_courses:
    if not each_course.startswith("Java"):
        continue # directly go for next iteration
    # Below code is applicable for only Java course
    print("This is Java Course and name is : ", each_course)
    print("This is one version of Java")
    print("This Java course duration is 10 days")
    print("-" * 10)

print("#"*40, end="\n\n")
#####################

