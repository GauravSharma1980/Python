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
# Task - 2 : create log_report.txt and log_report.csv
#            and add heading line
# Task - 3 : Extract and write to files
# ------------------------

print("# Task - 1 : Execute the command and store output in a variable")
print("-"*20)
# -------------------

import subprocess

my_cmd = 'type ..\log\server_log.txt'
cmd_output = subprocess.check_output(my_cmd, shell=True)
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

print("# Task - 3 : Extract and write to files")
print("#"*20)
#########################

for each_line in list_of_lines:
    if each_line.startswith('123'):

        sp = each_line.split() # split by space

        ip = sp[0]

        raw_dt = sp[3]  # '[26/Apr/2000:00:23:48'
        first_colon_index = raw_dt.index(":")
        dt = raw_dt[1:first_colon_index]

        raw_img = sp[6]  # '/pics/wpaper.gif'
        if raw_img.startswith('/pics'):
            img = raw_img.lstrip('/pics/')
        else:
            img = "No Image"

        url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
        url = url[1:-1]

        print(ip, dt,img, url, sep="\t", file=my_txt_file_handle, flush=True)

my_txt_file_handle.close()

print("cmd_report.txt created, please check")

print("-"*40, end="\n\n")
# -----------------------
