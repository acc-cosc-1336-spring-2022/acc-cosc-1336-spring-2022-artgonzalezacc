import unittest

from src.examples.f_files_exception.exceptions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_invalid_number_simulate_input(self):
        num = 5
        with self.assertRaises(ValueError):
            num = float('five')
        
        self.assertEqual(5.0, num)

        

