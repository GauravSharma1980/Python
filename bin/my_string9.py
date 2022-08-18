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

str = "HariSharma"

print(dir(str))

str = 56

print(str)