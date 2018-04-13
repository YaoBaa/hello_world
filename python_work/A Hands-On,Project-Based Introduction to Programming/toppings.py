requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	print("Adding "+requested_topping)
print('Finished!'+'\n')

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print('Sorry,'+requested_topping+' is empty')
	else:
		print('Adding '+requested_topping)
print("Finished your pizza!"+'\n')

requested_toppings=[]
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Addind "+requested_topping)
	print('The pizza is finished!')
else:
	print('You want a plain one?'+'\n') 


available_toppings = ['mushrooms','olives','green peppers','pepperoni'\
,'pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding '+requested_topping)
	else:
		print('Sorry,we do not have '+requested_topping)
print('Finished making your pizza')
