"""
in this section, we are discussing about,
2. Strings: We already have option to store collection of characters like name, email-id etc
                    But we dont know how to use it
                    - IMMUTABLE
                    - Automatically index number will be assigned to each character we store

"""
print("Strings PART - 1 ")
print("-"*20)
# -------------------------

my_string_1 = 'PERSON'
my_string_2 = "PERSON'S"
my_string_3 = 'PERSON\'S'
my_string_4 = '''PERSON'S HEIGHT IN XYZ" (" represents inch)'''
my_string_5 = """PERSON'S HEIGHT IN XYZ" (" represents inch)"""

print(my_string_1, my_string_2, my_string_3, my_string_4, my_string_5, sep="\n")

print("#"*40, end="\n\n")
#####################

print("Strings PART - 2 ")
print("-"*20)
# -------------------------
x = 10
y = 20
z = x + y

my_string_6 =f"add of {x} and {y} is {z}"
# f -> format : it replaces {var_name} with value
print(my_string_6)

print("#"*40, end="\n\n")
#####################

print("Strings PART - 3 ")
print("-"*20)
# -------------------------

my_string_7 = "C:\newfolder\test.py"
#\n, \t will get replaced with newline and tab space
print(my_string_7)

print("#"*40, end="\n\n")
#####################

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

print("Strings PART - 6 : SLICING : Getting substrings ")
print("-"*20)
# -------------------------

my_string = "WEL COME"
print("my_string : ", my_string)

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

print("Strings PART - 7 : SLICING : Provide step value to skip characters in between ")
print("-"*20)
# -------------------------

my_string = "WEL COME"
print("my_string : ", my_string)

# Refer 4_strings.xlsx SECTION-3
print("Substring from index 1 to 6 using +ve index nos, step by 1: ", my_string[1:6]) # EL CO
print("Substring from index 1 to 6 using -ve index nos, step by 1: ", my_string[-7:-2]) # EL CO
# Default step value is 1 : Which means, give me every character from 1 to 6
print("-"*10)

print("Substring from index 1 to 6 using +ve index nos, step by 1: ", my_string[1:6:1]) # EL CO
print("Substring from index 1 to 6 using -ve index nos, step by 1: ", my_string[-7:-2:1]) # EL CO
# same as above, step value is 1 : Which means, give me every character from 1 to 6
print("-"*10)

print("Substring from index 1 to 6 using +ve index nos, step by 2: ", my_string[1:6:2]) # E O
print("Substring from index 1 to 6 using -ve index nos, step by 2: ", my_string[-7:-2:2]) # E O
# step value is 2 : Which means, give me every 2nd character from 1 to 6
print("-"*10)

print("Substring from index 1 to 6 using +ve index nos, step by 3: ", my_string[1:6:3]) # EC
print("Substring from index 1 to 6 using -ve index nos, step by 3: ", my_string[-7:-2:3]) # EC
# step value is 3 : Which means, give me every 3rd character from 1 to 6
print("-"*10)

print("#"*40, end="\n\n")
#####################

print("Strings PART - 8 : Reverse Order ")
print("-"*20)
# -------------------------

my_string = "WEL COME"
print("my_string : ", my_string)

# Refer 4_strings.xlsx SECTION-4

print("Substring from index 6 to 1 using +ve index nos, step by '-1': ", my_string[6:1:-1]) # MOC L
print("Substring from index 6 to 1 using -ve index nos, step by '-1': ", my_string[-2:-7:-1]) # MOC L
# step value is (minus 1) -1 : Which means, give me every character from 6 to 1
print("-"*10)

print("Substring from index 6 to 1 using +ve index nos, step by '-2': ", my_string[6:1:-2]) #MCL
print("Substring from index 6 to 1 using -ve index nos, step by '-2': ", my_string[-2:-7:-2]) #MCL
# step value is (minus 2) -2 : Which means, give me every 2nd character from 6 to 1
print("-"*10)

print("#"*40, end="\n\n")
#####################

print("Complete Builtins List ")
print("-"*20)
# -------------------------

print(dir(__builtins__))

print("#"*40, end="\n\n")
#####################

print("Strings PART - 9 : Methods inside str class ")
print("-"*20)
# -------------------------

my_string = "WEL COME"
print(dir(my_string))

print("#"*40, end="\n\n")
#####################

print("Strings PART - 10 : Concatinate 2 strings ")
print("-"*20)
# -------------------------

my_string_1 = "Hello"
my_string_2 = "Python"

result1 = my_string_1 + my_string_2
result2 = my_string_1.__add__(my_string_2)
print(result1, result2)

print("#"*40, end="\n\n")
#####################

print("Strings PART - 11 : Trying few methods ")
print("-"*20)
# -------------------------

my_string = "WEL COME"
print("my_string : ", my_string)

result = my_string.startswith("WEL") # True/False
print('my_string.startswith("WEL") : ', result)

my_string_2 = "    WEL       COME    "
print("my_string_2 : ", my_string_2)

result = my_string_2.strip() # removes extra spaces from both the ends, not in between
print("my_string_2.strip() : ", result)

my_string_3 = "XYXYXYXYWEL XY COMEXYXYXY"
print("my_string_3 : ", my_string_3)

result = my_string_3.strip('XY') # removes all XY from both the ends, not in between
print("my_string_3.strip('XY') : ", result) # 'WEL XY COME'

result = my_string_3.removeprefix('XY')
print("my_string_3.removeprefix('XY') : ", result) #"XYXYXYWEL XY COMEXYXYXY"

print("#"*40, end="\n\n")
#####################
