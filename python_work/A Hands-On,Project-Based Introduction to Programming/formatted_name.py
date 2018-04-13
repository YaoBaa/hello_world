#coding=utf-8
def get_formatted_name(first_name,last_name,middle_name=""):
	#返回整洁的姓名"""
	if middle_name:
		full_name = "\n" + first_name + " " + last_name + " " + middle_name
	else:
		full_name = "\n" + first_name + " " + last_name
	return full_name.title()
	
#musician = get_formatted_name('yaoyao','li')
#print(musician)

#musician = get_formatted_name('1','2','3')
#print(musician)

#这是一个无限循环
while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break
	
	l_name = input("Last name: ")
	if l_name == 'q':
		break
		
	formatted_name = get_formatted_name(f_name,l_name)
	print("Hello," + formatted_name + "!")
