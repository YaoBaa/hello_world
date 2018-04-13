#coding=utf-8
def count_words(filename):
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		msg = "We can`t found the file."
		#print(msg)
		pass#�����κδ���ֱ������
	else:
		words = contents.split()#�������ʣ���㣬�������б���ʽ���棬����ֵ��words���ո�ǰ��ֿ�����Ԫ��
		num_words = len(words)
		print("The file " + filename + " has " + str(num_words) + " words.")

filenames = ['alice.txt','guest.txt','P169_note.txt','car.py']
for filename in filenames:
	count_words(filename)
