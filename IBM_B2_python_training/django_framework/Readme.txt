# ---------------------
# About DJango
# ---------------------
# - It is web development framework
# - it is MVT (Model View Template)
# - for Highly scalable application
# - Using DJango,
#   - We can develop web applications
#   - We can develop RESTFul services like REST API
# - Django is App based
#   for each page/module we need to create APP and use it
#
# - DJango is coming up with few APPS pre installed
#   in that 'admin' app also one.
#######################

# ---------------------
# Create Project
# ---------------------
# command:
# django-admin startproject myproject_1
#
# Example:
# C:\python_training\django_framework> django-admin startproject myproject_1
#######################

# ---------------------
# Run the Server
# ---------------------
# command:
# python manage.py runserver
#
# Example:
# C:\IBM_B2_python_training\django_framework\myproject_1> python manage.py runserver
#######################

# ---------------------
# Admin Page
# ---------------------
# In browser:
# http://127.0.0.1:8000/admin
#######################

# ---------------------
# Prepare Schema and Execute Schema
# ---------------------
# command - prepare schema.
# python manage.py makemigrations
#
# command - execute schema.
# python manage.py migrate
#######################

# ---------------------
# Create Admin Credentials
# ---------------------
# command:
# python manage.py createsuperuser
#
#######################

# ---------------------
# Create New App
# ---------------------
# command:
# python manage.py startapp home
#
#######################

# ---------------------
# Steps to configure New App
# ---------------------
# Step - 1. Add it in settings.py - INSTALLED_APPS
# Step - 2. 1st request, when we type url in browser, request will come to
#           myproject_1/urls.py -> ENTRY POINT
# Step - 3. home/urls.py
# Step - 4. views.py
#######################


# ---------------------
# Steps in Short
# ---------------------
# 1. django-admin startproject myproject_2
#   -cd myproject_2
# 2. python manage.py makemigrations
# 3. python manage.py migrate
# 4. python manage.py createsuperuser
# 5. python manage.py startapp home
# 6. add appname in settings.py
# 7. myproject_2/urls.py
# 8. home/url.py
# 9. views.py
# 10. python manage.py runserver
#######################

# ---------------------
# How to keep html files
# ---------------------
# - create 'templates' folder
# - keep all html files inside 'templates'
#######################

# ---------------------
# How to keep css/js/images
# ---------------------
# - create 'static' folder
# - keep all css/js/images files inside 'static'
#######################

# How URL Mapping?
# Example : 1
# http://127.0.0.1:8000/about
# 1st step : look for about/
#   if not look for '', and go inside the app
#   inside the app check whether 'about/' present
#
# Ex:2
# # http://127.0.0.1:8000/about/abc/xyz/mnc
#
# 1st look for mnc/ and go inside the app and look for remaining mapping ''
# if mnc/ not present look for for 'xyz' check whether 'mnc' in app
# if xyz/ not present then check 'abc' and check whether /xyz/mnc


# ---------------------
# Steps for login
# ---------------------
# 1. python manage.py startapp login
# 2. add appname in settings.py
# 3. myproject_2/urls.py
# 4. login/url.py
# 5. login/views.py
# 6. create 'templates' folder inside login folder
# 7. copy all htmls except index.html & about.html
# 8. python manage.py runserver
#######################

# ---------------------
# Procedure to create table
# ---------------------
# 1. Create model class in login/models.py
# 2. Register model in admin.py
# 3. makemigrations
# 4. migrate
#######################

# ---------------------
# Register user page configuratiom
# ---------------------
# 1. myproject_2/ulrs./py - NO CHANGE
# 2. login/urls.py - add path
# 3. login/views.py - write function
#######################