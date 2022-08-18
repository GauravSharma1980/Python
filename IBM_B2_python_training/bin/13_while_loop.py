"""
while loop : Based on the condition if we want to execute the loop
"""

print("while example - 1")
print("#"*20)
############################

x = 0
while x < 10:
    print("Value of x is : ", x)
    x = x + 1

print("-"*40,end="\n\n")
# --------------------------

print("print each character using while loop")
print("-"*20)
# -------------------

my_string = "Python"
print("my_string : ", my_string)

index_no = 0
while index_no < len(my_string):
    print("Each Char : ", my_string[index_no])
    index_no += 1

# for each_char in my_string[::5]:
#     print("each_char : ", each_char,end="")

print("#"*40)
#####################

# 2 Cases
# -------------------
# Case - 1 : break : to stop for loop in between
# Case - 2 : continue : in between if we want to send/jump to next iteration
# -------------------

print("Case - 1 : break : to stop while loop in between")
print("-"*20)
# -------------------

my_courses = ["C", "Java-1", "C++", "Java-2", "Python"]
print("my_courses : ", my_courses)

# Requirement: Findout are there any element which is starting with 'Java',
# if one element found then not require to verify other element.

index_no = 0
while index_no < len(my_courses):
    if my_courses[index_no].startswith("Java"):
        print("Found and course name is : ", my_courses[index_no])
        break
    index_no += 1

# for each_course in my_courses:
#     if each_course.startswith("Java"):
#         print("Found and course name is : ", each_course)
#         break

print("#"*40, end="\n\n")
#####################

print("Case - 2 : continue : in between if we want to send/jump to next iteration")
print("-"*20)
# -------------------

my_courses = ["C", "Java-1", "C++", "Java-2", "Python"]
print("my_courses : ", my_courses)

index_no = 0
while index_no < len(my_courses):
    if not my_courses[index_no].startswith("Java"):
        index_no += 1
        continue # directly go for next iteration
    # Below code is applicable for only Java course
    print("This is Java Course and name is : ", my_courses[index_no])
    print("This is one version of Java")
    print("This Java course duration is 10 days")
    print("-" * 10)
    index_no += 1

# for each_course in my_courses:
#     if not each_course.startswith("Java"):
#         continue # directly go for next iteration
#     # Below code is applicable for only Java course
#     print("This is Java Course and name is : ", each_course)
#     print("This is one version of Java")
#     print("This Java course duration is 10 days")
#     print("-" * 10)

print("#"*40, end="\n\n")
#####################
