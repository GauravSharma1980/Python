"""
pandas : One library, Many classes & functions in it
1 class name is : DataFrame
DataFrame is one class like list, tuple, etc
DataFrame is to keep 2 dimentional data, csv, xlsx data
    like my_db_result data in 11th program
"""

print("my_df_1")
print("#"*20)
##########################

import pandas as pd

my_df_1 = pd.DataFrame([[10, 20, 30],[40, 50, 60]],index=["r1","r2"],columns=["c1","c2","c3"])


print(my_df_1)

print("-"*40, end="\n\n")
# --------------------------

print(len(dir(my_df_1)))