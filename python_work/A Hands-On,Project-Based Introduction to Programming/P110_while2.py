while True:
	age = input("Please input your age: ")
	age = int(age)
	if age < 3:
		print('0')
	elif age >= 3 and age <= 12:
		print('10')
	elif age > 12 and age <= 100:
		print('15')
	else:
		break

while age != 12:
	print(age)
