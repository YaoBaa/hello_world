cars=['audi','bmw','subaru','toyota']
for car in cars:
	if car =='bmw':
		print(car.title())
	else:
		print(car.upper())
print('\n')

requested_topping = 'mushroom'
if requested_topping != 'mush':
	print('Not the same!')
	
if 'audi' in cars:
	print('yes')
else:
	print('no')
car='ms'
if car not in cars:
	print('not in cars')
else:
	print('in cars')
