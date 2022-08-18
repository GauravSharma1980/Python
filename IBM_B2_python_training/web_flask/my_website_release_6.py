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
# Run the server
# ----------------------
my_website_app.run()
# my_website_app.run(host='19.168.1.22', port='1234')
# ----------------------
