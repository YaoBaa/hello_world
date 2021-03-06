#coding=utf-8
class Car():
	#一次模拟汽车的简单尝试
	
	def __init__(self,make,model,year):
		#初始化汽车的属性
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		#返回整洁的描述信息
		long_name = str(self.year) + " " +self.make + " " + self.model
		return long_name.title()
		
	def read_odometer(self):
		#打印出一条指出汽车里程的消息
		print("\nThis car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):#第二种，通过放大修改数值
		#将里程表读数设置为指定的值
		#禁止里程数回调
		if mileage > self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("\nYou can`t roll back an odometer")
			
	def increment_odometer(self,miles):
		#将里程表读数增加指定量
		self.odometer_reading += miles
		
	def fill_gas_tank(self):
		print("This car has a has tank.")
		
class Battery():
	#一次模拟电动车电瓶的简单尝试
	def __init__(self,battery_size=70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		#打印一条描述电瓶容量的消息
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def increment_battery(self,battery):
		#增加电瓶容量
		self.battery_size += battery
		print(str(self.battery_size))
		
	def upgrade_battery(self):
		#将电瓶容量改为85
		if self.battery_size != 85:
			self.battery_size = 85
		
	def get_range(self):
		#打印一条消息，指出电瓶的续航里程
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
class ElectricCar(Car):
	def __init__(self,make,model,year):
		#初始化父类的属性
		super().__init__(make,model,year)
		
		#再初始化电动汽车的特殊属性
		self.battery = Battery()
		
		
	def fill_gas_tank(self):
		#与父类方法同名，表示重写
		print("This car does no need a has tank.")
		

my_tesla = ElectricCar('tesla','model s','2018')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
print('\n')

test_electric_car = ElectricCar('test','test','2020')
test_electric_car.battery.describe_battery()
test_electric_car.battery.get_range()
test_electric_car.battery.upgrade_battery()
test_electric_car.battery.get_range()
test_electric_car.battery.increment_battery(50)
test_electric_car.battery.upgrade_battery()
test_electric_car.battery.get_range()
