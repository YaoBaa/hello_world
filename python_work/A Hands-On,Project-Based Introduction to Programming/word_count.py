#coding=utf-8
def count_words(filename):
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		msg = "We can`t found the file."
		#print(msg)
		pass#不做任何处理，直接跳过
	else:
		words = contents.split()#将个单词，标点，数字以列表形式保存，并赋值给words，空格前后分开两个元素
		num_words = len(words)
		print("The file " + filename + " has " + str(num_words) + " words.")

filenames = ['alice.txt','guest.txt','P169_note.txt','car.py']
for filename in filenames:
	count_words(filename)
