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

print(my_set_1)
print(my_set_1, my_set_2, sep="\n")

print("#"*40, end="\n\n")
#########################

print("Set PART - 2 : Methods inside set class")
print("-"*20)
# -----------------------
# list to tuple, tuple to list etc we can convert
# Ex: list(my_set_1)

print(dir(my_set_1),sep="\n")

print("#"*40, end="\n\n")
#########################

listOfSetMethods = dir(my_set_1)

print(listOfSetMethods.__len__())


print("#"*40)

sb_account= {"Cust1","Cust2","Cust3"}

curr_accounts = {"Cust3"}

common_account = sb_account.intersection(curr_accounts)

print(common_account)

diff_account = sb_account.difference(curr_accounts);

print(diff_account);

print(type(diff_account))

union_account = sb_account.union(curr_accounts)

print(union_account)



#7. frozenset: Set only but IMMUTABLE

print("FrozenSet PART - 1")
print("-"*20)
# -----------------------

my_set_1 = frozenset({10, 10, 10, "Python", "Python", "Python", "Java", "C"})

my_set_2 = frozenset({10, 10, 10, "Python", "Python", "Python", "Java", "C"})

my_set_1 = ["hui"]

print(my_set_1, my_set_2, sep="\n")

print("#"*40, end="\n\n")
#########################

print(dir(my_set_1))


print("FrozenSet PART - 3 : Trying few methods")
print("-"*20)
# -----------------------

sb_account_customers = frozenset({"Cust-1", "Cust-2", "Cust-3", "Cust-4"})
ca_account_customers = frozenset({"Cust-3", "Cust-4", "Cust-5", "Cust-6"})

all_unique_customers = sb_account_customers.union(ca_account_customers)
print("all_unique_customers : ", all_unique_customers)

cust_having_both = sb_account_customers.intersection(ca_account_customers)
print("cust_having_both : ", cust_having_both)

only_sb_not_ca = sb_account_customers.difference(ca_account_customers)
print("only_sb_not_ca : ", only_sb_not_ca)


print("#"*40, end="\n\n")
#########################