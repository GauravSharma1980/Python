"""
Get log data from website and extract
IP
DATE
PICS
URL
using regular expression
and send extracted data to SQL database
"""

'''
SQLite -> SQL Database
SQLite -> Serverless database
How to create database
1) Through python program we can create database, tables and execute the queries
2) Through DB browser software for SQLite,we can create database, tables and execute the queries
'''

'''
How python will communicate with database?
python program  <--Communicate using Library-->  SQL Databases / No-SQL Databases

Example:
python program  <--Communicate using Library (cx-oracle)-->  Oracle Database
python program  <--Communicate using Library (pymysql)-->  MySQL Database
python program  <--Communicate using Library (sqlite3)-->  SQLite Database
'''
# Spilt into smaller tasks
# -------------------------------
# Task - 1 : get html content from the web
# Task - 2 : get log data from html content
# Task - 3 : Create database and table
# Task - 4 : Extract the info using regular expression
# -------------------------------

print("# Task - 1 : Get html content from website")
print("#"*20)
##############################

import urllib.request as ur

# -----------------------
my_web_file_handle = ur.urlopen('https://www.jafsoft.com/searchengines/log_sample.html')
website_content = my_web_file_handle.read()
website_content = website_content.decode()
my_web_file_handle.close()
print(website_content)
# -----------------------

print("-"*40, end="\n\n")
# --------------------------

print("# Task - 2 : pass html contnent to soup class object and parse")
print("#"*20)
##############################

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_content, 'html.parser')
log_data = soup.body.pre.text
list_of_lines = log_data.split('\n')
print(list_of_lines)

print("-"*40, end="\n\n")
# --------------------------

print("# Task - 3 : Create database and table")
print("#"*20)
##############################

import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect('my_database.sqlite3')
print('Done')

print("Create cursor object, through this we can execute queries")
my_db_cursor = my_db_connection.cursor()
print("Done")

print("Create table if not exists")
my_query='''
CREATE TABLE IF NOT EXISTS MY_LOG_DATA_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
'''
my_db_cursor.execute(my_query)
print("Done")

print("-"*40, end="\n\n")
# --------------------------

print("# Task - 4 : Extract the info using regular expression")
print("#"*20)
##############################

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*GET\s+/(pics/([a-zA-Z0-9]+\.(jpg|gif)))?.*(http[s]?://\S+)".*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(4)
        if img is None:
            img = "No Image"
        url = match_result.group(6)

        print("Check whether record already present in database")
        # ---------------------------
        my_query = f"SELECT * FROM MY_LOG_DATA_TABLE WHERE IP='{ip}' AND DATE='{dt}' AND PICS='{img}' AND URL='{url}'"
        my_db_cursor.execute(my_query)
        my_db_result = my_db_cursor.fetchall() # get all records
        if len(my_db_result) > 0:
            print("Record already exists. Proceeding for next record\n")
            continue
        # ---------------------------
        print("Record Not Present, Inserting New One\n")

        my_query = f"INSERT INTO MY_LOG_DATA_TABLE VALUES('{ip}', '{dt}', '{img}', '{url}')"
        print("Executing Query : ", my_query)
        my_db_cursor.execute(my_query)
        print("One row inserted")
        print("-"*20)

my_db_connection.commit()
print("\nAll records saved to database. Please check your db")
my_db_connection.close()

print("-"*40, end="\n\n")
# --------------------------
