#coding=utf-8
filename = 'alice.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	msg = "We can`t found the file."
	print(msg)
else:
	words = contents.split()#�������ʣ���㣬�������б���ʽ���棬����ֵ��words���ո�ǰ��ֿ�����Ԫ��
	num_words = len(words)
	print(num_words)
