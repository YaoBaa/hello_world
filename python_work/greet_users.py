#coding=utf-8
#���б��е�ÿλ�û��������򵥵��ʺ�
def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
		
usernames = ['anna','xueqing','hebao']
greet_users(usernames)
