#coding=utf-8
file_path = r'F:\python_work\test\car.py'
with open(file_path) as file_object:
#with open('test\car.py') as file_object:
	contents = file_object.read()#read�����ļ�ĩβʱ����һ�����ַ�������ӡ�������ǿ���
	print(contents)
	#print(contents.rstrip())#rstripɾ���ַ���ĩβ�հ�



with open('test\car.py') as file_object:#���ж�ȡ
	for line in file_object:
		print(line.rstrip())

with open(file_path) as file_object:#file_objectֻ����with�������ʹ��
	lines = file_object.readlines()#readlines()���ļ��ж�ȡÿһ�У����洢��һ���б���
	
for line in lines:
	print(line.rstrip())
