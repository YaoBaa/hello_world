import json

filename = 'fav_number.json'


def get_stored_number():
	try:
		with open(filename) as f_obj:
			number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return number
	
def get_new_number():
	with open(filename,'w') as f_obj:
		number = input("Please enter your favorite number :")
		json.dump(number,f_obj)
	return number
	
def greet_user():
	number = get_stored_number()
	if number:
		print("Your favorite number is :" + str(number))
	else:
		number = get_new_number()
		print("We`ll remember your favorite number!")
		
greet_user()
