"""
Get data from DB and send to
db_dump_3.txt
db_dump_4.csv
db_dump_5.xlsx
db_dump_6.json
"""

# Split into smallers tasks
# ------------------------
# Task - 1 : Get data from database and store in a variable
# Task - 2 : Send db data present in a variable to files
# ------------------------
print("# Task - 1 : Get data from database and store in a variable")
print("#"*20)
# --------------------------
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

print("# Task - 2 : Send db data present in a variable to files")
print("#"*20)
# --------------------------

# create DataFrame class object with my_db_result data, so that we can use methods
# present inside dataframe

import pandas as pd
my_db_df = pd.DataFrame(my_db_result, columns=["IP", "DATE", "PICS", "URL"])
print(my_db_df)

print("-"*40, end="\n\n")
# --------------------------

print("# Writing to files")
print("#"*20)
# --------------------------

my_db_df.to_csv('db_dump_3.txt', sep="\t")
my_db_df.to_csv('db_dump_4.csv') # default sep=','
my_db_df.to_excel('db_dump_5.xlsx')
my_db_df.to_json('db_dump_6.json')

print("-"*40, end="\n\n")
# --------------------------
