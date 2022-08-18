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
