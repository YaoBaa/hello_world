prompt = '\nPlease input the burdening that you want: '
new_burdening = ""
burdenings = []
while new_burdening != 'quit':
	new_burdening = input(prompt)
	if new_burdening == 'quit':
		print("You have order:")
		for burdening in burdenings:
			print(burdening)
		break
	else:
		burdenings.append(new_burdening)
		print("We have add " + new_burdening + " to the pizza!")
		print("You have order:")
		for burdening in burdenings:
			print(burdening)
		
