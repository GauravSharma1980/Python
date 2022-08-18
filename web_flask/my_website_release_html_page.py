"""
Web development using flask framework
"""

#"Creating a Welcome html Page "

"""

For this framework we have to do following 2 things

Task1 : Create a templates folder 

Task2 : put all the .html files in this
"""

import flask

#Creating an app for our  website...
my_web_site = flask.Flask('MyWebApp')



# ----------------------
# END POINT - 1 : URL http://127.0.0.1:5000/ mapped to '/'
# ----------------------
# @my_website_app.route('/') # decorator function
# def my_index_page():
#     return "Welcome"
########################

# ----------------------
# END POINT - 2 : URL http://localhost:8080/ mapped to '/'
# ----------------------
@my_web_site.route('/') # decorator function
def my_index_page():
    return flask.render_template('index.html')
########################

# ----------------------
# END POINT - 3 : For not found uri in the main URL
# ----------------------

@my_web_site.errorhandler(404)
def error_handler(myerror):
    return "no such page....."


# ----------------------
# END POINT - 4 : URL http://localhost:8080/about mapped to '/about'
# ----------------------

@my_web_site.route('/about')
def my_about_page():
    return flask.render_template('about.html') 

# ----------------------
# END POINT - 5 : URL http://localhost:8080/login mapped to '/login'
# ----------------------

@my_web_site.route('/login')
def my_login_page():
    return flask.render_template('login.html')     

my_web_site.run(host='localhost',port=8080)