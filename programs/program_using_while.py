"""
Requirement: Extract
IP
DATE
PICS
URL
From each IP address lines
"""

from operator import contains


#print("log_data : ")
#print("-"*20)
# ---------------------

log_data = '''
The following is a fragment from the server logs for JafSoft Limited. All the relative URLs are for the base URL http://www.jafsoft.com/.

First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
'''

#print(log_data)

#print("-"*40, end="\n\n")
# ---------------------

#print("type of log_data")
#print("-"*20)
# ---------------------------------

#print(type(log_data))

#print("#"*40, end="\n\n")
#################################

#print("Methods inside 'str' class ")
#print("-"*20)
# ---------------------------------

#print(dir(log_data))

#print("#"*40, end="\n\n")
#################################

#print("log_data in RAW form ")
#print("-"*20)
# ---------------------------------

#print(repr(log_data))

#print("#"*40, end="\n\n")
#################################

######Solution###########

newstr = log_data.split("\n")


#print("newstr\n\n",newstr)
index=0
while  index < len(newstr):
    if not newstr[index].startswith("123"):
     index +=1  
     continue
    else:
     #print("got it",newstr[index])
     ipaddress = newstr[index].split()[0]
     print("ipaddresscollected",ipaddress)
     dateInString = newstr[index].split()[3]
     #print("datestring",dateInString)
     dateCollected = dateInString[dateInString.index('[')+1:dateInString.index(':')][0:11]
     print("dateCollected",dateCollected)
     picString = newstr[index][newstr[index].index("GET")+3:newstr[index].index("HTTP/1.0")]
     #print("picString",picString)
     picCollected =picString[picString.rindex("/")+1:]
     print("picCollected",picCollected)
     urlString=newstr[index].split()[10]
     #print("urlString",urlString)
     urlCollected =urlString[urlString.index("\"")+1:urlString.rindex("\"")] 
     print("urlColleted",urlCollected)
     print("###############################")
     index +=1