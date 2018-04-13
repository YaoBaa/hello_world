#coding=utf-8
def make_pizza(size,*toppings):#*topping一个形参，可接受多个实参
						  #*让python创建一个名为topping的元组
	print("\nMaking a " + size + " pizza with the following topping: ")
	for topping in toppings:
		print(" - " + topping)

