#coding=utf-8
def make_pizza(size,*toppings):#*toppingһ���βΣ��ɽ��ܶ��ʵ��
						  #*��python����һ����Ϊtopping��Ԫ��
	print("\nMaking a " + size + " pizza with the following topping: ")
	for topping in toppings:
		print(" - " + topping)

