a = 100
b = 200

import sys

print("total ref of a are", sys.getrefcount(a))

a= 900
b= 900
c=900
d=900

print("id of a is ", id(a),id(b),id(c),id(d))

a = 900+1;
b = 900+1;

print("id of a is ", id(a),id(b),id(c),id(d))