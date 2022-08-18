"""
Requirement:
Read from server_log.txt and extract
IP
DATE
PICS
URL
and send extracted info to log_report.txt and log_report.csv
"""

# We can split into smaller tasks
# --------------------
# Task - 1 : Get data from server_log.txt and keep it in a variable
# Task - 2 : create log_report.txt and log_report.csv
#            and add heading line
# Task - 3 : Extract and write to files
# --------------------

print("# Task - 1 : Get data from server_log.txt and keep it in a variable")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_file_handle = open('../log/server_log.txt', 'r')

# Step - 2 : Read
# -----------------------
list_of_lines = my_file_handle.readlines()
print(list_of_lines )

# Step - 3 : Disconnect
# -----------------------
my_file_handle.close()

print("-"*40, end="\n\n")
# -----------------------


print("# Task - 2 : create log_report.txt and log_report.csv and add heading line")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_txt_file_handle = open('log_report.txt', 'w')
my_csv_file_handle = open('log_report.csv', 'w')

# Step - 2 : Write 1) write 2) writelines 3) print function
# -----------------------
# header to txt file
# my_txt_file_handle.write("IP\tDATE\tPICS\tURL\n")
# my_txt_file_handle.writelines(["IP\t", "DATE\t", "PICS\t", "URL\n"])
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle, flush=True)

# header to csv file
# my_csv_file_handle.write("IP,DATE,PICS,URL\n")
# my_csv_file_handle.writelines(["IP,", "DATE,", "PICS,", "URL\n"])
print("IP", "DATE", "PICS", "URL", sep=",", file=my_csv_file_handle, flush=True)

print("files log_report.txt and log_report.csv created with header. please check")

print("-"*40, end="\n\n")
# -----------------------

for instr in list_of_lines:
    if not instr.startswith("123"):
     continue
    else:
     print("got it",instr)
     ipaddress = instr.split()[0]
     print("ipaddresscollected",ipaddress)
     dateInString = instr.split()[3]
     print("datestring",dateInString)
     dateCollected = dateInString[dateInString.index('[')+1:dateInString.index(':')][0:11]
     print("dateCollected",dateCollected)
     picString = instr[instr.index("GET")+3:instr.index("HTTP/1.0")]
     print("picString",picString)
     picCollected =picString[picString.rindex("/")+1:]
     print("picCollected",picCollected)
     urlString=instr.split()[10]
     print("urlString",urlString)
     urlCollected =urlString[urlString.index("\"")+1:urlString.rindex("\"")] 
     print("urlColleted",urlCollected)
     print(ipaddress, dateInString,picCollected, urlCollected, sep="\t", file=my_txt_file_handle, flush=True)
     print(ipaddress, dateInString, picCollected, urlCollected, sep=",", file=my_csv_file_handle, flush=True)

my_txt_file_handle.close()
my_csv_file_handle.close()

print("log_report.txt and log_report.csv created, please check")

print("-"*40, end="\n\n")
# -----------------------