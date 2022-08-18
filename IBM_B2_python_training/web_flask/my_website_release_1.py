"""
Web development using flask framework
"""
'''
We have many framework for web development

bottle framework
flask framework - Micro Framework
django framework - MVT (Model View Template)
web2py framework
pyramid framework
falcon framework
etc
'''

'''
In this section we are discussing about
flask framework
'''

'''
Using flask framework,
1. We can develop websites
2. We can develop RESTFul web services
3. We can develop Micro Services
'''

'''
In this section, we are discussing about
Using flask framework,
1. We can develop websites
'''

'''
For any web application, we need 3 things
1. web server : flask is having builtin webserver which can be used for development
2. database : sqlite
3. browser
'''

# ----------------------
# Create App for our website
# ----------------------
import flask
my_website_app = flask.Flask('MyWebApp')
# ----------------------

# EMPTY WEBSITE

# ----------------------
# Run the server
# ----------------------
my_website_app.run()
# my_website_app.run(host='', port='')
# ----------------------
