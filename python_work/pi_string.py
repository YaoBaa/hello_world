#coding=utf-8
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()#ɾ��ת�з�.strip()ɾ����߿ո�
	
print(pi_string[:50].rstrip())
print(len(pi_string))
number = float(pi_string) + len(pi_string)#��ȡ�ı���,python��ȡ�Ķ����ַ���
print(str(number))

birthday = input("My birthday: ")
if birthday in pi_string:
	print("yes")
else:
	print("no")
