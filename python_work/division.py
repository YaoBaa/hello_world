print("Give me two numbers,and I`ll divide them.")
print("(Enter 'q' to quit.)")

while True:
	first_number = input("The first number: ")
	if first_number == 'q':
		break
	last_number = input("The last number: ")
	if last_number == 'q':
		break
	try:
		answer = float(first_number)/float(last_number)
	except ZeroDivisionError:
		print("You can`t divide by 0!")
	else:
		print(answer)
