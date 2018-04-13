#coding=utf-8
responses = {}
#设置一个标志，指出调查是否继续
polling_active = True
while polling_active == True:
	#提示输入被调查者的名字和回答
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")
	responses[name] = response
	
	repeat = input("Would you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False
		
#调查结束
print("\n ...... Poll Result ......")
for name,reponse in responses.items():
	print(name + "`s reponse is " + reponse)
