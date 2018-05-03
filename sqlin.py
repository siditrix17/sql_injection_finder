import os
import urllib2 
from googlesearch import search
import ssl

print'''  ---this script scans multiple google websites according to provided dork and returns if they are vulnerable or not by checking their error messages'''


print '''Different google docks that can be used to scan for websites are :
      1)  php?id=1                    7) php?id=1  pakistan
      2)  php?id=2                    8) php?id=1 hospital
      3)  php?id=5                    9) php?id=100   
      4)  php?id=1 india             10) php?id=1 school
      5)  php?id=3 hotel             11) php?id=1 china
      6)  php?id=10 college          12) php?id=1 login '''

print ''' These are some useful google dorks that can be applied. Nonetheless,user specific dorks are also accepted. Just make sure they are specific types for simple sql injection using dork'''
dork_list=['php?id=1','php?id=2','php?id=5','php?id=1 india','php?id=3 hotel','php?id=10 college','php?id=1 pakistan','php?id=1 hospital','php?id=100','php?id=1 school','php?id=1 china','php?id=1 login']
option=raw_input('Provide custom list(c) or use above dork(a):')
if option =="c":
  query=raw_input('Enter your custom dork:')
elif option =="a":
  value=int(raw_input('Enter respective dork number from above:'))
  query=dork_list[value-1]

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
   
