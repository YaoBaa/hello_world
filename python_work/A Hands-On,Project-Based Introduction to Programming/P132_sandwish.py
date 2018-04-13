#coding=utf-8
def make_sandwish(*toppings):
	toppingss = []
	for topping in toppings:
		toppingss.append(topping)
	print("\nWe will make a sandwish with the follow toppings: ")
	for topping in toppingss:
		print(topping)
make_sandwish('fish')
make_sandwish('meat','fish','apple')
make_sandwish('a','b','c','d','e')
print('\n')

def build_profile(first_name,last_name,**user_info):
	#**让python创建一个名为user_info空字典
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	
	for key,value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('yaoyao','li',location='jingzhou',ke='hb',bm=2)

print(user_profile)


def cars_info(color,logo,**car_info):
	cars = {}
	cars['color'] = color
	cars['logo'] = logo
	for key,value in car_info.items():
		cars[key] = value
	return(cars)
car = cars_info('red','bmw',a='A',b='B',c='C',d='D')
print(car)
	
