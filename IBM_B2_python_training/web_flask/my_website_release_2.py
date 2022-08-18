"""
Added welcome page
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
@my_website_app.route('/') # decorator function
def my_index_page():
    return "Welcome"
########################

# ----------------------
# Run the server
# ----------------------
my_website_app.run()
# my_website_app.run(host='', port='')
# ----------------------
