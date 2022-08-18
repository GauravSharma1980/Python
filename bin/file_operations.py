"""
Our program will communicate with resources outside the program
Text files with any extension .txt, .csv, .log, .mylog, .yourlog
finally any file which can be opened in NOTEPAD
"""
'''
Since we are communicating with resources outside the program
then we need to follow 3 steps
Step - 1 : Connect to file
Step - 2 : Read/Write
Step - 3 : Disconnect
'''


'''
3 steps
Step - 1 : Connect to file
        - open function
        
Step - 2 : Read/Write
        - Write : 1) write 2) writelines 3) print function
        - Read : 1) read 2) readline 3) readline using for loop
        4) readlines 5)list/tuple/set/dictionary

Step - 3 : Disconnect
        - flush() # Send data from buffer to file
        - close() # 1st call flush() then close the connection
'''



print("Write Operations")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
# my_file_handle = open('file name or file path', 'mode')
my_file_handle = open('my_out_file.txt', 'w')
# mode 'w' : Write Only
# mode 'w' : It creates new file if not present
# mode 'w' : ERASE all content if file present

# Step - 2 : Write 1) write 2) writelines 3) print function
# -----------------------
x = 10
s = "Python\n"
x = str(x) + "\n" # becasue write & writelines are expecting str data

# 1) write : It takes ONE string, all data should be in single string
my_file_handle.write(x) # Send data buffer
my_file_handle.write(s) # Send data buffer
my_file_handle.flush() # send data from buffer to file

my_data = [x,s]
my_file_handle.writelines(my_data)
my_file_handle.flush()

print(x,s,"Gaurav",file=my_file_handle,flush=True)

print("#######################",file=my_file_handle,flush=True)
# 3) print function
#print(x, s, 20, "\n", "Java", sep="", end="", file=my_file_handle, flush=True)
# OR
print(x.strip(), s.strip(), 20, "Java", sep="\n", end="", file=my_file_handle, flush=True)

# my_file_handle.flush() # This is not required

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("Write operations completed. Please check 'my_out_file.txt' ")

print("-"*40)
# -----------------------

print("Read Operations: 1) read")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_file_handle = open('my_out_file.txt', 'r')
# mode 'r' : Read Only
# mode 'r' : It will NOT create file if not present

# Step - 2 : Read using 1) read : it will read complete file content and return in ONE string
# -----------------------
file_content = my_file_handle.read()
print("file_content : ", file_content)
print("file_content in RAW Form: ", repr(file_content))

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("-"*40)
# -----------------------


print("Read Operations: 2) readline")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_file_handle = open('my_out_file.txt', 'r')

# Step - 2 : Read using 2) readline : It will read one line in each call
# -----------------------
file_content = my_file_handle.readline()
print("1st line : ", file_content)

file_content = my_file_handle.readline()
print("2nd line : ", file_content)

file_content = my_file_handle.readline()
print("3rd line : ", file_content)

my_file_handle.seek(0) # reset seek to 0th character (Beginning of the file)
file_content = my_file_handle.readline()
print("1st line : ", file_content)

my_file_handle.seek(0,2) # EOF # 2-> END
file_content = my_file_handle.readline()
print("EMPTY : ", file_content)

#my_file_handle.seek(-4,1) # 4 characters backward from current position(EOF)
#file_content = my_file_handle.readline()
#print("Last 4 characters : ", file_content)

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("-"*40)
# -----------------------

print("Read Operations: 3) readline using for loop")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_file_handle = open('my_out_file.txt', 'r')

# Step - 2 : Read using 3) readline using for loop
# -----------------------
for each_line in my_file_handle:
    print("each_line ==>: ", each_line)

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("-"*40)
# -----------------------

print("Read Operations: 4) readlines")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_file_handle = open('my_out_file.txt', 'r')

# Step - 2 : Read using 4) readlines:  complete file content in list
# -----------------------
file_content = my_file_handle.readlines()
print("file_content : ", file_content )

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("-"*40)
# -----------------------


print("Read Operations: 5) list/tuple/set")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_file_handle = open('my_out_file.txt', 'r')

# Step - 2 : Read using 5) list/tuple/set
# -----------------------
file_content = list(my_file_handle)
print("file_content in list : ", file_content)

my_file_handle.seek(0)
file_content = tuple(my_file_handle)
print("file_content in tuple : ", file_content)

my_file_handle.seek(0)
file_content = set(my_file_handle)
print("file_content in set : ", file_content)

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("-"*40)
# -----------------------

# -----------------------
# >>> L = [100, 200, 300]
# >>> dict(L)
# Traceback (most recent call last):
#   File "<pyshell#1>", line 1, in <module>
#     dict(L)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
# -----------------------
# >>> M=[(0,100),(1,200),(2,300)]
# >>> dict(M)
# {0: 100, 1: 200, 2: 300}
# >>> #------------------
# >>> # Instead of manually making pair, we can make use of
#       enumerate function to make a pair
# >>> L = [100, 200, 300]
# >>> e= enumerate(L)
# >>> list(e)
# [(0, 100), (1, 200), (2, 300)]
# >>> dict(enumerate(L))
# {0: 100, 1: 200, 2: 300}
# >>> # even we can pass file handle
# >>>
# -----------------------

print("Read Operations: 6) dictionary")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_file_handle = open('my_out_file.txt', 'r')

# Step - 2 : Read using 6) dict
# -----------------------
file_content = dict(enumerate(my_file_handle))
print("file_content in dict : ", file_content)

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("-"*40)
# -----------------------


# -----------------------
# Modes:
# -----------------------
# mode 'w' : Write Only, Erase the data, create new file
# mode 'r' : Read Only, It will not create file if not present
# mode 'a' : Append Only, It will create file only if not present
# mode 'w+' : RW, Erase the data, create new file
# mode 'r+' : RW, It will not create file if not present
# mode 'a+' : RW, It will create file only if not present
# -----------------------

