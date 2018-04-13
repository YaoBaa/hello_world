import json

filename = 'fav_number.json'
with open(filename) as f_obj:
	number = json.load(f_obj)
	print(number)
