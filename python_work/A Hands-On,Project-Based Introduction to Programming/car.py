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
		
		
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#�����޸Ĳ����ķ�����self.odometer_readingΪ��
my_new_car.odometer_reading = 22#��һ�֣�ֱ���޸���ֵ
my_new_car.read_odometer()

my_new_car.update_odometer(23)#�ڶ���
my_new_car.read_odometer()

my_new_car.update_odometer(20)#ʵ��������޷��ص�

#�����֣�ͨ�����������Խ��е���
print('\n')
my_used_car = Car("bmw","X6",2018)
print(my_used_car.get_descriptive_name())

my_new_car.update_odometer(20000)
my_new_car.read_odometer()

my_new_car.increment_odometer(6812)
my_new_car.read_odometer()
