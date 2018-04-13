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

class Admin(User):
	def __init__(self,first_name,last_name,age,height,weight):
		super().__init__(first_name,last_name,age,height,weight)
		self.admin = Privileges()

			
class Privileges():
	def __init__(self):
		self.privileges = ["can add post","can delete post","can ban user"]
				
	def show_privileges(self):
		print("The Admin`s privileges :")
		for privilege in self.privileges:
			print("\t" + privilege)
		
print('\n')
user_admin = Admin('hui','zhu',22,165,52)
user_admin.describe_user()
user_admin.admin.show_privileges()
