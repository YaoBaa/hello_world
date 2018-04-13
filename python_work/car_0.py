#coding=utf-8
class Car():
	#һ��ģ�������ļ򵥳���
	
	def __init__(self,make,model,year):
		#��ʼ������������
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		#���������������Ϣ
		long_name = str(self.year) + " " +self.make + " " + self.model
		return long_name.title()
		
	def read_odometer(self):
		#��ӡ��һ��ָ��������̵���Ϣ
		print("\nThis car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):#�ڶ��֣�ͨ���Ŵ��޸���ֵ
		#����̱��������Ϊָ����ֵ
		#��ֹ������ص�
		if mileage > self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("\nYou can`t roll back an odometer")
			
	def increment_odometer(self,miles):
		#����̱��������ָ����
		self.odometer_reading += miles
		
class Battery():
	#һ��ģ��綯����ƿ�ļ򵥳���
	def __init__(self,battery_size=70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		#��ӡһ��������ƿ��������Ϣ
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def increment_battery(self,battery):
		#���ӵ�ƿ����
		self.battery_size += battery
		print(str(self.battery_size))
		
	def upgrade_battery(self):
		#����ƿ������Ϊ85
		if self.battery_size != 85:
			self.battery_size = 85
		
	def get_range(self):
		#��ӡһ����Ϣ��ָ����ƿ���������
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
class ElectricCar(Car):
	def __init__(self,make,model,year):
		#��ʼ�����������
		super().__init__(make,model,year)
		
		#�ٳ�ʼ���綯��������������
		self.battery = Battery()
		
		
	def fill_gas_tank(self):
		#�븸�෽��ͬ������ʾ��д
		print("This car does no need a has tank.")
