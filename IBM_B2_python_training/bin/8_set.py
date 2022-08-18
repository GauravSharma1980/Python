"""
In this section, we are discussing about,
6. Set:  We already have option to store collection of elements like list 0f names, list of email-ids etc
        But we dont know how to use it
        - MUTABLE: After creating the set, throught the program we can alter/modify
            (we can add element / we can remove element / we can update element)
        - Keeps only UNIQUE values
        - No index # convert to list if we want index to access each element
        - Un-ordered,
        - we can store only IMMUTABLE objects
"""

print("Set PART - 1")
print("-"*20)
# -----------------------

my_set_1 = {10, 10, 10, "Python", "Python", "Python", "Java", "C"}
# if we pass key:value then it will be dictionary
my_set_2 = set({10, 10, 10, "Python", "Python", "Python", "Java", "C"})

print(my_set_1, my_set_2, sep="\n")

print("#"*40, end="\n\n")
#########################

print("Set PART - 2 : Methods inside set class")
print("-"*20)
# -----------------------
# list to tuple, tuple to list etc we can convert
# Ex: list(my_set_1)

print(dir(my_set_1))

print("#"*40, end="\n\n")
#########################


print("Set PART - 3 : Trying few methods")
print("-"*20)
# -----------------------

sb_account_customers = {"Cust-1", "Cust-2", "Cust-3", "Cust-4"}
ca_account_customers = {"Cust-3", "Cust-4", "Cust-5", "Cust-6"}

all_unique_customers = sb_account_customers.union(ca_account_customers)
print("all_unique_customers : ", all_unique_customers)

cust_having_both = sb_account_customers.intersection(ca_account_customers)
print("cust_having_both : ", cust_having_both)

only_sb_not_ca = sb_account_customers.difference(ca_account_customers)
print("only_sb_not_ca : ", only_sb_not_ca)

print("#"*40, end="\n\n")
#########################

