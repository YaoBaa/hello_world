#coding=utf-8
filename = 'programming.txt'

with open(filename,'w') as file_object:#'r'读取，'w'写入，'a'附加
	file_object.write("I love programming.\n")

with open(filename,'a') as file_object:#'r'读取，'w'写入，'a'附加
	file_object.write("I do not love programming.\n")



while True:
	print("Please enter your name")
	print("(Enter q to quit)")
	name = input("Name :")
	message = "Welcome," + name.title() + ".\n"
	if name == 'q':
		break
	else:
		with open ('guest_book.txt','a') as file_object:
			file_object.write(message)
	
	print(message)
