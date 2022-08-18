"""
7. frozenset: Set only but IMMUTABLE
"""

print("FrozenSet PART - 1")
print("-"*20)
# -----------------------

my_set_1 = frozenset({10, 10, 10, "Python", "Python", "Python", "Java", "C"})

my_set_2 = frozenset({10, 10, 10, "Python", "Python", "Python", "Java", "C"})

print(my_set_1, my_set_2, sep="\n")

print("#"*40, end="\n\n")
#########################

print("FrozenSet PART - 2 : Methods inside set class")
print("-"*20)
# -----------------------

print(dir(my_set_1))

print("#"*40, end="\n\n")
#########################

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

