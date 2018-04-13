from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
	print(name.title() + "`s favorite language is " + language.title() + "." )
	

class Die():
	def __init__(self,number):
		self.number = number
		self.sides = 6
		
	def roll_die(self):
		i = 1
		while i <= 10: 
			i += 1
			self.sides = randint(1,self.number)
			print(self.sides)
			
die_1 = Die(20)
die_1.roll_die()


