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