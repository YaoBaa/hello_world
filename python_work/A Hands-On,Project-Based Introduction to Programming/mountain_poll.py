#coding=utf-8
responses = {}
#����һ����־��ָ�������Ƿ����
polling_active = True
while polling_active == True:
	#��ʾ���뱻�����ߵ����ֺͻش�
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")
	responses[name] = response
	
	repeat = input("Would you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False
		
#�������
print("\n ...... Poll Result ......")
for name,reponse in responses.items():
	print(name + "`s reponse is " + reponse)
