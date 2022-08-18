x = 10
y = 30
z = 40

soutput =f"the values are {x} {y} {z}"

print(soutput)


print("#"*40, end="\n\n")
#####################
print("Strings PART - 3 ")
print("-"*20)
# -------------------------
my_string_7 = "C:\newfolder\test.py"
#\n, \t will get replaced with newline and tab space
print(my_string_7)

print("Strings PART - 4 ")
print("-"*20)
# -------------------------
my_string_8 = r"C:\newfolder\test.py"
# r - > raw string
#\n, \t will print/store as it is
print(my_string_8)
print("#"*40, end="\n\n")
#####################


print("Strings PART - 5 : Display existing string in RAW format ")
print("-"*20)
# -------------------------
my_string_9 = "C:\newfolder\test.py"
print("my_string_9 : ", my_string_9)
print("my_string_9 in RAW: ", repr(my_string_9))
print("my_string_9 length: ", len(my_string_9))
print("#"*40, end="\n\n")
#####################


str = "GAURAV"

print("first character of str is ", str[0],str[-6])

print("Strings PART - 6 : Access each character using index ")
print("-"*20)
# -------------------------
my_string = "WEL COME"
print("my_string : ", my_string)
# Refer 4_strings.xlsx SECTION-1
print("0th character using +ve index no : ", my_string[0])
print("0th character using -ve index no : ", my_string[-8])
print("1st character using +ve index no : ", my_string[1])
print("1st character using -ve index no : ", my_string[-7])
# print("10th character using +/-ve index no : ", my_string[10]) # IndexError
print("#"*40, end="\n\n")
#####################

# Refer 4_strings.xlsx SECTION-2
print("Substring from index 1 to 6 using +ve index nos: ", my_string[1:6]) # EL CO
print("Substring from index 1 to 6 using -ve index nos: ", my_string[-7:-2]) # EL CO
# we can mix +ve and -ve index number
print("Substring from index 1 to END using +ve index nos: ", my_string[1:]) # EL COME
print("Substring from index 1 to END using -ve index nos: ", my_string[-7:]) # EL COME
print("Substring from index BEGINNING to 6 using +ve index nos: ", my_string[:6]) # WEL CO
print("Substring from index BEGINNING to 6 using -ve index nos: ", my_string[:-2]) # WEL CO
print("Substring from index BEGINNING to END : ", my_string[:]) # WEL COME
print("#"*40, end="\n\n")
#####################