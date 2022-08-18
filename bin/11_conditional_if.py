"""
If : Based on the condition if we want to execute the statements
"""
'''
In other language,
if cond{
s1
    s2
        s3
    s4
s5
}
s6

In python, we wont use {} to make block, instead we use INDENTATION,

if cond:
    s1
    s2
    s3
    s4
    s5
    if cond:
        s1
        s2
        s3
        s4
        s5
s6
'''

print("Only if")
print("-"*20)
# ---------------------
x = 10
if x == 10:
    print("Value of x is 10")
if x > 10:
    print("Value of x is greater than 10")
if x < 10:
    print("Value of x is less than 10")


print("#"*40, end="\n\n")
#######################


x = 10
if x == 10:
    print("Value of x is 10")
elif x > 10:
    print("Value of x is greater than 10")
elif x < 10:
    print("Value of x is less than 10")
else:
    print("ERRRRRR")    

print("#"*40, end="\n\n")
#######################

print("if-elif-else")
print("-"*20)
# ---------------------
x = 10
if x == 10:
    print("Value of x is 10")
elif x > 10:
    print("Value of x is greater than 10")
else:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
#######################

print("if-elif-else")
print("-"*20)
# ---------------------
x = 10
if x == 10:
    print("Value of x is 10")
elif x > 10:
    print("Value of x is greater than 10")
else:
    print("Value of x is less than 10")

print("#"*40, end="\n\n")
#######################

print("if with strings")
print("-"*20)
# ---------------------

course = "Pythin"
print("course : ", course)

if course != "Java":
    print("Course not equal to java")

if ("th" in course) and ("on" in course) : # or, not
    print("Sub string found")

if not course.startswith("C++"):
    print("Course is not C++ ")

print("#"*40, end="\n\n")
#######################

print("if with list/tuple/set and any other collection")
print("-"*20)
# ---------------------

my_courses_1 = ["Java", "Python", "C"]
my_courses_2 = ["Java", "Python","C"]

print("my_courses_1 : ", my_courses_1)
print("my_courses_2 : ", my_courses_2)

if "Python" in my_courses_1:
    print("Course Python Found")

if my_courses_1 == my_courses_2:
    print("Both lists are equal")
else:
    print("Both the lists are NOT equal")
    
print("#"*40, end="\n\n")
#######################

mydictionary = {"course":"Python","fee":"10000"}

if "Python" in mydictionary.values():
    print("Python is present")


print("if with Dictionary")
print("-"*20)
# ---------------------

my_dict = {"course": "Python", "duration": 10, "mode": "online"}
print("my_dict : ", my_dict)
# >>> my_dict = {"course": "Python", "duration": 10, "mode": "online"}

# >>> my_dict.keys()
# dict_keys(['course', 'duration', 'mode'])
if 'course' in my_dict.keys():
    print("Key 'course' present ")

# >>> my_dict.values()
# dict_values(['Python', 10, 'online'])
if "Python" in my_dict.values():
    print("Value 'Python' present ")

# >>> my_dict.items()
# dict_items([('course', 'Python'), ('duration', 10), ('mode', 'online')])
if ('course', 'Python') in my_dict.items():
    print("Item ('course', 'Python') Found")

print("#"*40, end="\n\n")
#######################