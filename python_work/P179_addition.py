while True:
	print("Please enter two number!")
	print("Enter 'q' to end at any time.")
	try:
		first_numbers = input("The first number : ")
		if first_numbers == 'q':
			break
		first_number = int(first_numbers)
		
		last_numbers = int(input("The last number : "))
		if last_numbers == 'q':
			break
		last_number = int(last_numbers)
	except ValueError:
		print("Please enter the number" + "\n")
	else:
		answer = int(first_number) - int(last_number)
		print(str(answer) + "\n")
	
