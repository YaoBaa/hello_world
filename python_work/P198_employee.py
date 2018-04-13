class Employee():
	def __init__(self,first_name,last_name,annual):
		self.response = []
		self.first_name = first_name
		self.last_name = last_name
		self.annual = annual
		
	def give_raise(self,number=5000):
		self.annual += number
		return self.annual
		
	def store_employee(self):
		self.response.append(self.first_name)
		self.response.append(self.last_name)
		self.response.append(self.annual)
		return self.response
		
