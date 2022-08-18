import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)


txt = "Gaurav sharma is great"

x = re.findall("^Ga.+v",txt)

print(x)