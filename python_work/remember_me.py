#coding=utf-8
import json

filename = 'username.json'
def get_stored_username():#��ȡ�ѱ����ļ��е��û���
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():#��ȡ�û�������û���
	username = input("What is your name?")
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
		return username
		
def greet_user():
	username = get_stored_username()
	if username:
		new_user = input("Are you " + username.title() + "(enter y/n)?")
		if new_user == 'y':
			print("Welcome back," + username.title() + "!" )
		else:
			username = get_new_username()
			print("We`ll remember you when you back, " + username + "." )
	else:
		username = get_new_username()
		print("We`ll remember you when you back, " + username + "." )
		
greet_user()
