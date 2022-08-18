"""
Added registration html page
"""


# ----------------------
# Create App for our website
# ----------------------
import flask
my_website_app = flask.Flask('MyWebApp')
# ----------------------

# ----------------------
# END POINT - 1 : URL http://127.0.0.1:5000/ mapped to '/'
# ----------------------
# @my_website_app.route('/') # decorator function
# def my_index_page():
#     return "Welcome"
########################

# ----------------------
# END POINT - 2 : URL http://127.0.0.1:5000/ mapped to '/'
# ----------------------
@my_website_app.route('/') # decorator function
def my_index_page():
    return flask.render_template('index.html')
########################

# ----------------------
# END POINT - 3 : URL http://127.0.0.1:5000/about mapped to '/about'
# ----------------------
@my_website_app.route('/about')
def my_about_page():
    return flask.render_template('about.html')
########################

# ----------------------
# END POINT - 4 : URL http://127.0.0.1:5000/login mapped to '/login'
# ----------------------
@my_website_app.route('/login')
def my_login_page():
    return flask.render_template('login.html')
########################

# ----------------------
# END POINT - 5 : URL http://127.0.0.1:5000/registeruser mapped to '/registeruser'
# ----------------------
@my_website_app.route('/registeruser')
def my_registeruser_page():
    return flask.render_template('registeruser.html')
########################


# ----------------------
# END POINT - 6 : URL http://127.0.0.1:5000/addnewuser mapped to '/addnewuser'
# ----------------------
@my_website_app.route('/addnewuser', methods=['POST'])
def my_addnewuser_page():
    """
    Our Plan
    1. Get all details from front end
    2. Verify both the passwords are matching
    3. Verify whether user already exists
    4. add new user details to database
    5. return registration successful
    """
    # --------------------------------
    # 1. Get all details from front end
    # --------------------------------
    # all the data will be captured by framework in 'flask.request.form' dictionary
    entered_username = flask.request.form.get('uname')
    entered_password_1 = flask.request.form.get('pw1')
    entered_password_2 = flask.request.form.get('pw2')
    entered_email = flask.request.form.get('email')
    # --------------------------------

    # --------------------------------
    # 2. Verify both the passwords are matching
    # --------------------------------
    if entered_password_1 != entered_password_2:
        return "Both passwords are not matching.<br><br> <a href='/registeruser'>Go Back</a>"
    # --------------------------------

    # --------------------------------
    # 3. Verify whether user already exists
    # --------------------------------
    import sqlite3

    print("Create/Connect to database 'users_database.sqlite3'")
    my_db_connection = sqlite3.connect('users_database.sqlite3')
    print('Done')

    print("Create cursor object, through this we can execute queries")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table if not exists")
    my_query = '''
    CREATE TABLE IF NOT EXISTS USERS_TABLE(
    NAME VARCHAR(100),
    PASSWORD VARCHAR(100),
    EMAIL VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    my_query = f"SELECT * FROM USERS_TABLE WHERE NAME='{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()  # get all records
    if len(my_db_result) > 0:
        return "User Already Exists. <br><br><a href='/registeruser'>Go Back</a>"
    # --------------------------------

    # --------------------------------
    # 4. add new user details to database
    # --------------------------------
    my_query = f"INSERT INTO USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    # --------------------------------

    # --------------------------------
    # 5. return registration successful
    # --------------------------------
    return "User Registration Success.<br><br> <a href='/login'>Click Here to Login</a>"
    # --------------------------------


########################

# ----------------------
# Run the server
# ----------------------
my_website_app.run()
# my_website_app.run(host='19.168.1.22', port='1234')
# ----------------------
