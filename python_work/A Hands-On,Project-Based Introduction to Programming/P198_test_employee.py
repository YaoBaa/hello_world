import unittest
from P198_employee import Employee

class EmployeeTestCase(unittest.TestCase):
	
	def setUp(self):
		self.my_employee = Employee('yaoyao','li',120000)
	
	def test_give_default(self):
		annual = self.my_employee.give_raise()
		self.assertEqual(annual,125000)
		
	def test_give_custom_raise(self):
		annual = self.my_employee.give_raise(10000)
		self.assertEqual(annual,130000)
		
unittest.main()
