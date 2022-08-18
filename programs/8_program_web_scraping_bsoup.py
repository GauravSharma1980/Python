"""
Read data from website
parse html using bsoup
and also print log data
"""
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Split into smaller tasks
# ------------------------
# Task - 1 : Get html content from website
# Task - 2 : pass html contnent to soup class object and parse
# ------------------------

print("# Task - 1 : Get html content from website")
print("#"*20)
##############################

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
#print(soup)

print("-"*40, end="\n\n")
# --------------------------


print("Methods inside beautiful soup class ")
print("#"*20)
##############################

#print(dir(soup))

print("-"*40, end="\n\n")
# --------------------------

print("Head Tag")
print("#"*20)
##############################

print(soup.head)

print("-"*40, end="\n\n")
# --------------------------

print("Title inside of Head Tag")


print(soup.head.text)


print("-"*40, end="\n\n")
# --------------------------

print("1st link tag")
print("#"*20)
##############################

print(soup.head.link)

print("-"*40, end="\n\n")
# --------------------------


print("1st link tag Attributes")
print("#"*20)
##############################

print("link Tag : ", soup.head.link)
print("Attribute REL : ", soup.head.link.get('rel'))
print("Attribute href : ", soup.head.link.get('href'))
print("Attribute type : ", soup.head.link.get('type'))

print("-"*40, end="\n\n")
# --------------------------

print("all link tags")
print("#"*20)
##############################

all_link_tags = soup.head.find_all('link')
print(all_link_tags)

print("-"*40, end="\n\n")
# --------------------------

print("all link tags")
print("#"*20)
##############################

all_link_tags = soup.head.find_all('link')

for each_link_tag in all_link_tags:
    print("Each Link Tag : ", each_link_tag)
    print("Each Link Tag Attribute href: ", each_link_tag.get('href'))

print("-"*40, end="\n\n")
# --------------------------

print("log data")
print("#"*20)
##############################


log_data = soup.body.pre
print('log_data wihtout pre',log_data)

print("-"*40, end="\n\n")
# --------------------------

log_data = soup.body.pre.text
print(log_data)

print("-"*40, end="\n\n")
# --------------------------