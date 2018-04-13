
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open!")
		
		
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ['knx','yjx','mg','yl']
		
	def flavors_print(self):
		for flavors in self.flavors:
			print(flavors)
	
		
restaurant_1 = Restaurant('hb','lo')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

icecreamestand_1 = IceCreamStand('zh','lo')
icecreamestand_1.describe_restaurant()
icecreamestand_1.open_restaurant()
icecreamestand_1.flavors_print()


