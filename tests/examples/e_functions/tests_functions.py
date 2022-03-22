import unittest

from src.examples.e_functions.value_return_functions import get_random_number, local_variable, return_first_last_name, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_local_variable(self):
        self.assertEqual(10, local_variable(10))

    def test_local_variable_scope(self):
        val0 = 0
        val = local_variable(val0)
        self.assertEqual(0, val0)
        self.assertEqual(0, val)
    
    def test_get_random_number(self):
        rand = get_random_number(1,100)
        flag = rand >= 1 and rand <= 100
        self.assertEqual(flag, True)

    def test_return_two_function_values(self):
        first,last = return_first_last_name()
        self.assertEqual("john", first)
        self.assertEqual("doe", last)
        
        

