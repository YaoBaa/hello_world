import unittest
from P192_city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
	def test_city_country(self):
		city_country = get_city_country('santiago','chile')
		self.assertEqual(city_country,'Santiago Chile')
		
		
	def test_city_country_population(self):
		city_country = get_city_country('santiago','chile',100000)
		self.assertEqual(city_country,'Santiago Chile - Population 100000')
		
unittest.main()
