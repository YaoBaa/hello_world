#coding=utf-8
with open('P169_note.txt') as file_object_1:
	contents = file_object_1.read()
	print(contents.rstrip())
	print('\n')

file_name_1 = r'F:\python_work\P169_note.txt'
file_name_2 = r'P169_note.txt'
with open(file_name_1) as file_object_2:
	contents = file_object_2.read()
	print(contents)
	
with open(file_name_2) as file_object_3:
	lines = file_object_3.readlines()
	
for line in lines:
	print(line.rstrip())
	
for line in lines:
	message = line
	message.replace('Pthon','Java')#¥ÌŒÛ”√∑®
	print(line.replace('Python','Java'))
