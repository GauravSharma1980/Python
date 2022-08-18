"""
Web development using flask framework
"""

"Creating a Welcome Page "

import flask

#Creating an app for our  website...
my_web_site = flask.Flask('MyWebApp')

#End Point -1: URL http://localhost:8080 mapped to '/welcome'
@my_web_site.route('/welcome')
def my_index_page():
    return "Welcome"

@my_web_site.errorhandler(404)
def error_handler(myerror):
    return "no such page....."

my_web_site.run(host='localhost',port=8080)



