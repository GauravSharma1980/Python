

def fileOperation(logFileName):

  my_file_handle = open( logFileName,'r') #../log/server_log.txt'

  for instr in my_file_handle.readlines:
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
     

print("log_report.txt and log_report.csv created, please check")
print("-"*40, end="\n\n")
# -----------------------