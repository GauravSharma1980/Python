"""
Added welcome html page
"""

'''
To add html page
1. create directory with the name 'templates'
2. inside 'templates' directory, keep all html
'''

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
# Run the server
# ----------------------
my_website_app.run()
# my_website_app.run(host='19.168.1.22', port='1234')
# ----------------------
