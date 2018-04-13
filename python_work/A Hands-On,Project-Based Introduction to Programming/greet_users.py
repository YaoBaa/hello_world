#coding=utf-8
#向列表中的每位用户都发出简单的问候
def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
		
usernames = ['anna','xueqing','hebao']
greet_users(usernames)
