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