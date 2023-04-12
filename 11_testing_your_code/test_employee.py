#Name: Aurelio Siordia
#Date: 11/04/23

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test employee.py"""
    
    def setUp(self):
        """Create an instance of class Employee"""
        self.my_employee = Employee('Alejandro', 'Villamontes', '2500')

    def test_give_default_raise(self):
        new_salary = self.my_employee.give_raise()
        self.assertEqual(new_salary, 7500)

    def test_give_custom_raise(self):
        new_salary = self.my_employee.give_raise(7000)
        self.assertEqual(new_salary, 9500)


if __name__ == '__main__':
    unittest.main()
        


