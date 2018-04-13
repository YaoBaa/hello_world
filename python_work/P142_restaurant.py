class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open!")
		
restaurant_1 = Restaurant('hb','lo')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()


class User():
	def __init__(self,first_name,last_name,age,height,weight):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.height = height
		self.weight = weight
		
	def describe_user(self):
		print("\tfirst name: " + self.first_name.title())
		print("\tlast name: " + self.last_name.title())
		print("\tage: " + str(self.age))
		print("\theight: " + str(self.height))
		print("\tweight: " + str(self.weight))
		
	def greet_user(self):
		print("\nHello," + self.first_name.title() + " " 
			+ self.last_name.title())
			
user_1 = User('yaoyao','li',22,170,62)
user_1.describe_user()
user_1.greet_user()
