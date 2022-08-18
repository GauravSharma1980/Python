
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

db_dump_1_handler =  open("db_dump_1.txt","w")

print("IP ","DATE", "IMG","URL",file=db_dump_1_handler,flush=True)


for i, j, k, l in my_db_result:
        print(i,j,k,l, sep="\t", file=db_dump_1_handler, flush=True)
        #print(i,j,k,l, sep=",", file=my_csv_file_handle, flush=True)

db_dump_1_handler.close()
#my_csv_file_handle.close()

