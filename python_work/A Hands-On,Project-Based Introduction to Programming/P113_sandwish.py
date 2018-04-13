sandwish_orders = ['pastrami','fish','pastrami','tuna','pastrami','meet']
sandwish_finished = []

print("We have sold out the 'pastrami'\n")
while 'pastrami' in sandwish_orders:
	sandwish_orders.remove('pastrami')

while sandwish_orders:
	for sandwish_order in sandwish_orders:
		sandwish_orders.remove(sandwish_order)
		sandwish_finished.append(sandwish_order)
		print("I made your " + sandwish_order + ".")
print(sandwish_orders)
print(sandwish_finished)
print("\nI have finish the sandwish.")



visits = {}
active = True
while active:
	places = []
	name = input("\nPlease tell us your name: ")
	place =  ""
	while place != 'end':
		place = input("Which place do you like(input end to end the places): ")
		places.append(place)
	visits[name] = places
	end = input("Is there anyone else(yes/no): ")
	if end == 'no':
		print("\nThat is the answer!")
		for names,place_wants in visits.items():
			print("names:")
			for place_want in place_wants:
				print("\t" + place_want)
		break
	
