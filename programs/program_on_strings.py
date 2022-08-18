"""
Requirement:
From the below string, extract
IP: 123.123.123.123
DATE:26/Apr/2000
PICS:wpaper.gif
URL: http://www.jafsoft.com/asctortf/

"""

from operator import index
from posixpath import split
from readline import insert_text


print("in_string")
print("-"*20)
# ---------------------------------

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(in_string)

print("#"*40, end="\n\n")
#################################

print("type of in_string")
print("-"*20)
# ---------------------------------

print(type(in_string))


print("following methods are there in str")
print(dir(in_string))

print(in_string[0:15])

print("IP",in_string[0:in_string.index('-')])

print("split",in_string.split()[0])

print("#"*40, end="\n\n")
#################################

# expected o/p ==>"[26/Apr/2000:00:23:48 -0400]"

print(in_string.split()[3][1:12])

str_date = in_string[in_string.index('[')+1:in_string.index(']')]

print(str_date[0:11])


print(in_string[in_string.index('[')+1:in_string.index(']')][0:11])

#expected o/p==>PICS:wpaper.gif

str_file = in_string[in_string.index("GET")+3:in_string.index("HTTP/1.0")]

print("str_file",str_file)

indexOfFirst = str_file.rindex('/')

print(str_file[indexOfFirst+1:])