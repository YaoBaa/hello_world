#coding=utf-8
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()#删除转行符.strip()删除左边空格
	
print(pi_string[:50].rstrip())
print(len(pi_string))
number = float(pi_string) + len(pi_string)#读取文本是,python读取的都是字符串
print(str(number))

birthday = input("My birthday: ")
if birthday in pi_string:
	print("yes")
else:
	print("no")
