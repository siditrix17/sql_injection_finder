import os
import urllib2 
from googlesearch import search
import ssl




query=raw_input('enter the query to search:')
lis=[]
for url in search(query, tld='es', lang='es', stop=20):
     #print(url)
     lis.append(url)


for k in range(0,19):
 print lis[k]
 context = ssl._create_unverified_context()
 response = urllib2.urlopen(lis[k]+"'")
 page_source = response.read()
 if "error" in page_source:
   print"----------------*****************************----------------"
   print "SQL InJECtable!!!"
   print '___ _____________'
   f=open('sites.txt','w')
   f.write(lis[k])
 else:
     print "Not vulnerable.."





#print 'writing into file'
#f=open("sites.txt",'w')
#f.write(lis)
   
