#coding=utf-8
file_path = r'F:\python_work\test\car.py'
with open(file_path) as file_object:
#with open('test\car.py') as file_object:
	contents = file_object.read()#read到达文件末尾时返回一个空字符串，打印出来会是空行
	print(contents)
	#print(contents.rstrip())#rstrip删除字符串末尾空白



with open('test\car.py') as file_object:#逐行读取
	for line in file_object:
		print(line.rstrip())

with open(file_path) as file_object:#file_object只能在with代码块中使用
	lines = file_object.readlines()#readlines()从文件中读取每一行，并存储在一个列表中
	
for line in lines:
	print(line.rstrip())
