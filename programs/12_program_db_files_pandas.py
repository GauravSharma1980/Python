"""
Get data from db
and
send to files db_dump_1.txt and db_dump_2.txt
"""

# Split into smallers tasks
# ------------------------
# Task - 1 : Get data from database and store in a variable
# Task - 2 : Send db data present in a variable to files
# ------------------------

# Task - 1 : Get data from database and store in a variable


import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect('my_database.sqlite3')
print('Done')

print("Create cursor object, through this we can execute queries")
my_db_cursor = my_db_connection.cursor()
print("Done")

print("Executing select query")
my_query = "SELECT * FROM MY_LOG_DATA_TABLE"
my_db_cursor.execute(my_query)
print("Done")

print("Retrieve all records from cursor")
my_db_result = my_db_cursor.fetchall()  # get all records
print("Done")

print("my_db_result : ", my_db_result, sep="\n")

print("-"*40, end="\n\n")
# --------------------------

# Task - 2 : Send db data present in a variable to files

import pandas as pd

my_df_1 = pd.DataFrame(my_db_result,columns=["IP","DATE","PICS","URL"])

my_df_1.to_csv('db_dump_3.txt',sep='\t')
my_df_1.to_csv('db_dump_4.csv')
my_df_1.to_excel('db_dump_5.xlsx')


print(my_df_1)

print("-"*40, end="\n\n")
# --------------------------



