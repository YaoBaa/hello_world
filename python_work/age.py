ages = list(range(10,100,30))
ages = [1,10,40,90]
ages = (2,16,20,80)
for age in ages:
	print("ages="+str(age))
	if age < 4:
		print("price is 0")
	elif age < 18:
		print("price is 18")
	elif age < 65:
		print("price is 65")
	else:
		print("price is 00")
