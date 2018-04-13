class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)
		print("The number is :" + str(self.number_served))
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open!")
		
	def set_number_served(self,number):
		self.number_served = number
		print("We set number :" + str(self.number_served))
		
	def increment_number_served(self,increment_number):
		self.number_served += increment_number
		print("Add " + str(increment_number) + " to the number." + 
			"\nWe get :" + str(self.number_served))
		
restaurant_1 = Restaurant('hb','lo')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.set_number_served(20)
restaurant_1.describe_restaurant()
restaurant_1.increment_number_served(80)
restaurant_1.describe_restaurant()
print("\n")




class User():
	def __init__(self,first_name,last_name,age,height,weight):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.height = height
		self.weight = weight
		self.login_attempts = 1
		
	def describe_user(self):
		print("\tfirst name: " + self.first_name.title())
		print("\tlast name: " + self.last_name.title())
		print("\tage: " + str(self.age))
		print("\theight: " + str(self.height))
		print("\tweight: " + str(self.weight))
		
	def greet_user(self):
		print("\nHello," + self.first_name.title() + " " 
			+ self.last_name.title())
	
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		print("Login_attempts :" +str(self.login_attempts))
		self.login_attempts = 0
		print("Login_attempts :" +str(self.login_attempts))
			
user_1 = User('yaoyao','li',22,170,62)
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
