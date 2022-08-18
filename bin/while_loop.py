
print("#"*40)

x = 0

while x < 10:
 print(x)
 x +=1

 print("#"*40)


print("#"*40)

str = "Python"

length =len(str)-1
while  length >= 0:
  print(str[length])
  length -= 1


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

