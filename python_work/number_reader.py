#coding=utf-8
import json

filename = 'numbers.json'
with open(filename) as f_obj:
	#numbers = f_obj.read()
	numbers = json.load(f_obj)
	print(numbers)
