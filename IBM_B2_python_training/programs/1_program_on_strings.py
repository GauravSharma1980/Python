"""
Requirement:
From the below string, extract
IP: 123.123.123.123
DATE:26/Apr/2000
PICS:wpaper.gif
URL: http://www.jafsoft.com/asctortf/

"""

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

print("#"*40, end="\n\n")
#################################

print("Methods inside 'str' class ")
print("-"*20)
# ---------------------------------

print(dir(in_string))

print("#"*40, end="\n\n")
#################################

print("Extract - IP - 1 -way")
print("-"*20)
# ---------------------------------

ip = in_string[0:15]
print("IP : ", ip)

print("#"*40, end="\n\n")
#################################

print("Extract - IP - 2 -way")
print("-"*20)
# ---------------------------------

first_space_index = in_string.index(" ")#15
ip =in_string[0:first_space_index]
print("IP : ", ip)

print("#"*40, end="\n\n")
#################################

print("Extract - IP - 2 -way")
print("-"*20)
# ---------------------------------

first_space_index = in_string.index(" ")
ip =in_string[0:first_space_index]
print("IP : ", ip)

print("#"*40, end="\n\n")
#################################

print("Extract - IP - 3 -way")
print("-"*20)
# ---------------------------------

sp = in_string.split()
print("sp : ", sp)
ip = sp[0]
print("IP : ", ip)

print("#"*40, end="\n\n")
#################################

print("Extract - DATE - 1 -way")
print("-"*20)
# ---------------------------------

first_square_bracket_index = in_string.index("[")+1
first_colon_index = in_string.index(":")
dt = in_string[first_square_bracket_index : first_colon_index]
print(dt)

print("#"*40, end="\n\n")
#################################

print("Extract - DATE - 2 -way")
print("-"*20)
# ---------------------------------

raw_dt = sp[3] # '[26/Apr/2000:00:23:48'
first_colon_index = raw_dt.index(":")
dt = raw_dt[1:first_colon_index]
print(dt)

print("#"*40, end="\n\n")
#################################

print("Extract - PICS")
print("-"*20)
# ---------------------------------

raw_img = sp[6] # '/pics/wpaper.gif'

# 1-way to remove /pics/
index_of_last_slash = raw_img.rindex('/')
img_1 = raw_img[index_of_last_slash + 1 : ]

# 2-way to remove /pics/
sp_raw_img = raw_img.split("/") # ['', 'pics', 'wpaper.gif']
img_2 = sp_raw_img[2]
img_3 = sp_raw_img[-1]

# 3-way to remove /pics/
img_4 = raw_img.lstrip('/pics/') # remove all occurances of /pics/
#img_5 = raw_img.removeprefix('/pics/') # remove 1st occurance

# 3-way to remove /pics/
img_6 = raw_img.replace('/pics/', '') # replace all occurances of /pics/

print(img_1, img_2, img_3, img_4, img_6, sep="\n")

print("#"*40, end="\n\n")
#################################

print("Extract - Url")
print("-"*20)
# ---------------------------------

url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
url = url[1:-1]
print(url)

print("#"*40, end="\n\n")
#################################
