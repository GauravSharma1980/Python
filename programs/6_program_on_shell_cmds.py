"""
Execute below shell command
'type ..\log\server_log.txt'
and capture the output, from the output
IP
DATE
PICS
URL
and send extracted info to cmd_report.txt
"""

# Split into smaller task
# ------------------------
# Task - 1 : Execute the command and store output in a variable
# Task - 2 : create log_report.txt
#            and add heading line
# Task - 3 : Extract and write to files
# ------------------------

import subprocess

cmd_output = subprocess.check_output('cat ../log/server_log.txt', shell=True)
cmd_output = cmd_output.decode()
list_of_lines = cmd_output.split("\n")
print(list_of_lines)
print("-"*40)
# -------------------

print("# Task - 2 : create cmd_report.txt and add heading line")
print("#"*20)
#########################

# Step - 1 : Connect to file
# -----------------------
my_txt_file_handle = open('cmd_report.txt', 'w')


# Step - 2 : Write
# -----------------------
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle, flush=True)

print("cmd_report.txt created with header. please check")

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
     dateCollected = dateInString[dateInString.index('[')+2:dateInString.index(':')][0:11]
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
    
my_txt_file_handle.close()


