#!/usr/bin/env python
#----------------
#----------------
print ''''
Cms Scanner Version 1.0

#1-Reverse Wordpress
#2-Reverse Joomla
#3-Get the users of the server


 
 +-----------------------------+
 |#Author: Gh0st_3xp101t       +
 +#Greetz:|X-Line|Udemy|+
 +#Version:1.0                 +
 +-----------------------------+
 
 Usage:www.website.com
 Example:www.google.com
'''
import urllib2,  sys , time
from re import findall
import httplib
from socket import*
class text:
    copy = '\033[94m'
    criminal = '\033[91m'
    search = '\033[93m'
    thank = '\033[90m'
    

    def disable(self):
        self.copy = ''
        self.ss = ''
        self.search = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

ip = raw_input('Website:')
server = gethostbyname(ip)

ur1 = urllib2.urlopen("http://webdetail.org/ip/"+server).read()
found = findall("'><b>(.*?)</b></a></td><td>",ur1)  
ser = findall("<title>(.*?)</title>",ur1)
user = findall("</td><td>(.*?)</td></tr><tr><td",ur1)
print "Server:%s"%(ser)
admin = open('Users.txt','w+')
word =open('Wordpress.txt','w+')
joomla = open('Joomla.txt','w+')


for i in range(len(found)):
	site = found[i]
	try:
		conn = httplib.HTTPConnection(site)
		conn.request('POST','/wp-login.php')
		res = conn.getresponse()
		if res.status == 200:
			word.write("\n"+"http://"+site+"/wp-login.php")
			print text.search+"Wordpress:",site+"/wp-login.php"
		else:
			print 'site:',site
	except(gaierror) as ex:
		print 'Error:%s'%ex
	except(httplib.BadStatusLine) as ex2:
		print 'Error:%s'%ex2
	except(error) as ex3:
		print 'Error:%s'%ex3
	except KeyboardInterrupt:
		print "FuCk Lammerz"
for i in range(len(found)):
	site = found[i]
	try:
		conn = httplib.HTTPConnection(site)
		conn.request('GET','/administrator/index.php')
		res = conn.getresponse()
		if res.status == 200:
			joomla.write("\n"+"http://"+site)
			print text.search+"joomla:",site
		else:
			print 'site:',site
	except(gaierror) as ex:
		print 'Error:%s'%ex
	except(httplib.BadStatusLine) as ex2:
		print 'Error:%s'%ex2
	except(error) as ex3:
		print 'Error:%s'%ex3
		
for s in range (len(found)):
	l = "http://"+found[s]
	rr = findall("http://(.*?).com",l)
	for f in range(len(rr)):
		admin.write('\n'+rr[f])
		print rr[f]
for s in range (len(found)):
	htt = "http://"+found[s]
	r = findall("http://(.*?).net",htt)			
	for ll in range(len(r)):
			admin.write('\n'+r[ll])
			print r[ll]
for s in range (len(found)):
	http = "http://"+found[s]
	rrr = findall("http://(.*?).org",http)			
	for lll in range(len(rrr)):
			admin.write('\n'+rrr[lll])
			print rrr[lll]
for s in range (len(found)):
	http = "http://"+found[s]
	rrrr = findall("http://(.*?).info",http)			
	for llll in range(len(rrrr)):
			admin.write('\n'+rrrr[llll])
			print rrrr[llll]
print ("\n")
print ("Done ..")
print ('Website: https://github.com/Gh0st3xp101t')