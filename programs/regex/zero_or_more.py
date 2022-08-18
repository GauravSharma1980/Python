import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)


txt = "Gaurav Sharma is great"

x = re.findall("^Gaurav.* great$",txt)

print(x)