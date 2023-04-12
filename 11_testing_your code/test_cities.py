#Name: Aurelio Siordia
#Date: 11/04/23

import unittest
from city_functions import city_country

#11-1 City, Country
class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_function.py'.'"""
    
    def test_city_country(self):
        """Sort name of city and country"""
        my_city_country = city_country('santiago', 'chile')
        self.assertEqual(my_city_country, 'Santiago, Chile')


#11-2 Population        
    def test_city_country_population(self):
        """Sort name of city, country & population""" 
        my_city_country_pop = city_country('santiago', 'chile', '507296')
        self.assertEqual(my_city_country_pop, 'Santiago, Chile - population 507296')


if __name__ == '__main__':
    unittest.main()