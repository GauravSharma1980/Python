"""
In this program, we are making use of functions and variables,
defined in MyModule.py Library
"""

print("print all global variables")
print("#"*20)
###############################
import MyModule
# - import will execute MyModule.py
# - import will create one object called 'MyModule'
# - inside 'MyModule' object,
#   it will keep all the objects created from MyModule.py inside 'MyModule' object.
#   in this case, from MyModule.py we will get 2 objects 1) location 2)log_process_func_keyword
#   both the object are stored in 'MyModule' object
#

# display all variables in current scope(here it global scope)
print(locals())

print("-"*40)
# --------------------

print("What is inside MyModule object")
print("#"*20)
###############################

print(dir(MyModule))

print("-"*40)
# --------------------

print("1-way to import")
print("#"*20)
###############################
import MyModule

print("location : ", MyModule.location)
print("log result : ", MyModule.log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------


print("2-way to import")
print("#"*20)
###############################
import MyModule as mm

print("location : ", mm.location)
print("log result : ", mm.log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------

print("3-way to import")
print("#"*20)
###############################

from MyModule import location, log_process_func_keyword

print("location : ", location)
print("log result : ", log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------


print("4-way to import")
print("#"*20)
###############################

from MyModule import location as lc, log_process_func_keyword as lpf

print("location : ", lc)
print("log result : ", lpf(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------


print("5-way to import")
print("#"*20)
###############################

from MyModule import *

print("location : ", location)
print("log result : ", log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------

# --------------------
# - If we are developing more and more modules then we can
#   organize in a folders/sub-folders - these folders are called PACKAGES
# - We can directly import from the PACKAGE
# --------------------

print("1-way to import")
print("#"*20)
###############################
import MyPackage.aws.MyModule

print("location : ", MyPackage.aws.MyModule.location)
print("log result : ", MyPackage.aws.MyModule.log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------

print("2-way to import")
print("#"*20)
###############################
import MyPackage.aws.MyModule as mm

print("location : ", mm.location)
print("log result : ", mm.log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------

print("3-way to import")
print("#"*20)
###############################

from MyPackage.aws.MyModule import location, log_process_func_keyword

print("location : ", location)
print("log result : ", log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------

print("4-way to import")
print("#"*20)
###############################

from MyPackage.aws.MyModule import location as lc, log_process_func_keyword as lpf

print("location : ", lc)
print("log result : ", lpf(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------

print("5-way to import")
print("#"*20)
###############################

from MyPackage.aws.MyModule import *

print("location : ", location)
print("log result : ", log_process_func_keyword(log_file_path="../log/server_log.txt"))

print("-"*40)
# --------------------
