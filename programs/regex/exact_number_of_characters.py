import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)


txt = "Today is the day!!"

x = re.findall("T.{3}y",txt)

print(x)

