"""
In this section, we are discussing about,

5. Dictionary:  We already have option to store collection of elements like list 0f names, list of email-ids etc
                    But we dont know how to use it
                    - MUTABLE: After creating the dictionary, throught the program we can alter/modify
                        (we can add element / we can remove element / we can update element)
                    - We can provide our own index. We also call this as KEY:VALUE pair
"""

print("Dictionary PART - 1")
print("-"*20)
# ------------------------

my_dict_1 = {0: "Python", 1: 10, 2: "Online"}
my_dict_2 = {"course": "Python", "duration": 10, "mode": "Online","course":"Maths"}
my_dict_3 = dict({"course": "Python", "duration": 10, "mode": "Online"})
# Any IMMUTABLE object can be used for KEY
# Value can be any value/object

print(my_dict_1, my_dict_2, my_dict_3, sep="\n")

print("#"*40, end="\n\n")
##########################

print("Dictionary PART - 2")
print("-"*20)
# ------------------------

my_dict_4 = {"courses": ["Python", "Java"], "duration": 10, "mode": ["Online","Offline"]}

my_dict_5 = { "duration": 10,
              "mode": ["Online","Offline"],
              "courses":{
                            "online":["C", "C+"],
                            "offline":["Java", "Python"]
                        }
            }

print("my_dict_4 : ", my_dict_4)
print("my_dict_5 : ", my_dict_5)

print("mode : ", my_dict_5["mode"]) # ["Online","Offline"]
print("1st element in mode : ", my_dict_5["mode"][0]) # Online
print("-"*10)

print("courses : ", my_dict_5['courses'])
# "courses":{ "online":["C", "C+"], "offline":["Java", "Python"] }
print("online courses : ", my_dict_5['courses']['online']) # ["C", "C+"]
print("1st online courses : ", my_dict_5['courses']['online'][0]) # 'C'
print("-"*10)

print("#"*40, end="\n\n")
##########################

print("Dictionary PART - 3 : Methods inside dictionary class")
print("-"*20)
# ------------------------

print(dir(my_dict_1))

print("#"*40, end="\n\n")
##########################

print("Dictionary PART - 4 : Methods inside dictionary class")
print("-"*20)
# ------------------------

my_dict_6 = {"course":"Maths","duration":"6"}

print(my_dict_6)

print(my_dict_6["course"])

print(my_dict_6.get("course"))

print("#"*40, end="\n\n")

#my_dict_6.update("course","Hindi")

print(my_dict_6)
##########################

# Add
my_dict_6["location"] = "India" # if key not present add new key else update
print('my_dict_6 after adding my_dict_6["location"] = "India" : ', my_dict_6)

# update
my_dict_6["course"] = ["Java", "C++"]
print("my_dict_6 after updating course : ", my_dict_6)

# remove
my_dict_7 = my_dict_6.copy()
print("copy my_dict_7 : ", my_dict_7)

removed_element = my_dict_7.pop('duration') # it will remove and also return removed value
print("my_dict_7 after my_dict_7.pop('duration') : ", removed_element)

removed_element = my_dict_7.popitem() # remove last element and return both (key,value)
print("my_dict_7.popitem() : ", removed_element)

print("#"*40, end="\n\n")
##########################

print("keys::  ",my_dict_6.keys())

print("values::",my_dict_6.values())

