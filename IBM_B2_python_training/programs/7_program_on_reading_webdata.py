"""
Read data from website and print
"""

print("Read data from website and print")
print("-"*20)
# -----------------------

import urllib.request as ur

# 1. Connect
# -----------------------
my_web_file_handle = ur.urlopen('https://www.jafsoft.com/searchengines/log_sample.html')

# 2. Read
# -----------------------
website_content = my_web_file_handle.read()
website_content = website_content.decode()

# 3. disconnect
# -----------------------
my_web_file_handle.close()

print(website_content)

print("-"*40)
# -----------------------
