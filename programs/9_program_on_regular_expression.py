"""
Get log data from website and extract
IP
DATE
PICS
URL
using regular expression
"""

# Spilt into smaller tasks
# -------------------------------
# Task - 1 : get html content from the web
# Task - 2 : get log data from html content
# Task - 3 : Extract the info using regular expression
# -------------------------------

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as ur

# -----------------------
my_web_file_handle = ur.urlopen('https://www.jafsoft.com/searchengines/log_sample.html')
website_content = my_web_file_handle.read()
website_content = website_content.decode()
my_web_file_handle.close()
#print(website_content)
# -----------------------

print("-"*40, end="\n\n")
# --------------------------

print("# Task - 2 : pass html contnent to soup class object and parse")
print("#"*20)
##############################

from bs4 import BeautifulSoup
# BeautifulSoup is one class like list, tuple, dict etc
soup = BeautifulSoup(website_content, 'html.parser')
log_data = soup.body.pre.text
list_of_lines = log_data.split('\n')
print(list_of_lines)

print("-"*40, end="\n\n")
# --------------------------

import re

#for line in list_of_lines:
#   print("IIIIIIIPPPPPPP",re.match('(\d\d\d.{4}',line))


for each_line in list_of_lines:
    #match_result = re.match('what pattern you want match?', 'on which string you want to match?')
    match_result = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*',each_line)
    #match_result = re.match('(\d\d\d\.){3}[.]\d(\d\d\d\.){3}',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)

# COMMENT-1
# --------------------------
# IDENTIFIERS
#  \d -> used to represent any ONE digit from 0-9
#  \D -> used to represent any ONE non-digit (except 0-9)
#  . -> used to represent any ONE any character
# \. -> used to represent DONT only
# [.] -> used to represent DONT only
#
# MODIFIERS
# * -> 0 or more times
# + -> 1 or more times
# ? -> 0 or 1 time
#
# QUANTIFIERS
# \d{3} -> internally it will make \d\d\d
# \d{1,3} -> internally it will make (\d | \d\d | \d\d\d)
# [0-9]{3} -> internally it will make [0-9][0-9][0-9]
# --------------------------

# COMMENT-2
# --------------------------
# - match_result = re.match('\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}.*',each_line)
# - here match_result having complete line if given pattern matches
# - here match_result having None if given pattern NOT matches
#
# - Our requirement is, if there is a match then extract IP address
# - we need to put bracket for IP address, match capture that portion separately
#   called group, for each group/capture it will assign the numbers starting from 1
#
# - match_result = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*',each_line)
#
# - which means, if there is a match give me group(1)
# --------------------------

print("-"*40, end="\n\n")
# --------------------------

print("Extract IP, DATE")
print("#"*20)
##############################

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT
# ------------------
# 26/Apr/2000
#
# 26
# ----
# \d\d
# \d{2}
# [0-9][0-9]
# [0-9]{2}
# \d{1,2}
# [0-9]{1,2}
# \d?\d
# [0-9]?[0-9]
#
# Apr
# ---------
# [A-Z][a-z]{2}
# [a-zA-Z]{3}
# (Jan|Feb|Mar)
# ------------------

print("-"*40, end="\n\n")
# --------------------------


print("Extract IP, DATE, PICS")
print("#"*20)
##############################

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*GET\s+/(pics/([a-zA-Z0-9]+\.(jpg|gif)))?.*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(4)
        if img is None:
            img = "No Image"
        print(ip, dt,img)

# COMMENT
# -------------------------
# \s -> one SPACE
# \S -> one non-SPACE character
# -------------------------

print("-"*40, end="\n\n")
# --------------------------

print("Extract IP, DATE, PICS, URL")
print("#"*20)
##############################

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*GET\s+/(pics/([a-zA-Z0-9]+\.(jpg|gif)))?.*(http[s]?://\S+)".*',each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(4)
        if img is None:
            img = "No Image"
        url = match_result.group(6)
        print(ip, dt,img, url)

print("-"*40, end="\n\n")
# --------------------------