#coding=utf-8
filename = 'alice.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	msg = "We can`t found the file."
	print(msg)
else:
	words = contents.split()#将个单词，标点，数字以列表形式保存，并赋值给words，空格前后分开两个元素
	num_words = len(words)
	print(num_words)
