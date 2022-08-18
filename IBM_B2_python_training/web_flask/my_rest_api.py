"""
Using flask framework,
1. We can develop websites
2. We can develop RESTFul web services
3. We can develop Micro Services,

In this section, we are discussing about
2. We can develop RESTFul web services
3. We can develop Micro Services,

Create REST API to provide access to log data.
"""

'''
Suppose we need to share log data with others/other application

OPTION-1: We can provide database name, table name, user, password, host 
so that others can connect like example
import cx-oracle
cx-oracle.connect(user, pass, host etc) 

it will be like
Our Application    <---->  Others

OPTION-1 will not work, because we can't share all credentials
'''

'''
Some way we wanted to give access.
We got 2 solutions
1) SOAP - Simple Object Access Protocol
2) REST - REpresentational State Transfer

Both solutions will tell, DONT use OPTION-1, instead,
provide some INTERFACE/GATE between our application with others
like

Our Application    <--INTERFACE/GATE-->  Others
'''

'''
INTERFACE also called as APPLICATION PROGRAMMING INTERFACE or API
- SOAP API
- REST API
'''

'''
flask is already implemented REST architecture, if we want to create
API then we need to ENDPOINT and return data in json
'''

# ----------------------
# Create App for our website
# ----------------------
import flask
my_rest_api_app = flask.Flask('MyRESTApp')
# ----------------------


# ----------------------
# API END POINT : URL http://127.0.0.1:1234 mapped to '/'
# ----------------------
@my_rest_api_app.route('/', methods=['GET'])
def my_API_function(name):
    """
    Tasks
    1. Get log data from db
    2. return log data in json
    """

    # --------------------------------
    # 1. Get log data from db
    # --------------------------------
    import sqlite3

    print("Create/Connect to database 'my_database.sqlite3'")
    my_db_connection = sqlite3.connect('../programs/my_database.sqlite3')
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
    # --------------------------------

    # --------------------------------
    # 2. return log data in json
    # --------------------------------
    return flask.jsonify(my_db_result)
    # --------------------------------


# ----------------------
# Run the server
# ----------------------
my_rest_api_app.run(port=1234)
# ----------------------
