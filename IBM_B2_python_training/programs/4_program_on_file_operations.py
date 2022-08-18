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

print("# Task - 3 : Extract and write to files")
print("#"*20)
#########################

# copied from program_2
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
        print(ip, dt, img, url, sep=",", file=my_csv_file_handle, flush=True)

my_txt_file_handle.close()
my_csv_file_handle.close()

print("log_report.txt and log_report.csv created, please check")

print("-"*40, end="\n\n")
# -----------------------
