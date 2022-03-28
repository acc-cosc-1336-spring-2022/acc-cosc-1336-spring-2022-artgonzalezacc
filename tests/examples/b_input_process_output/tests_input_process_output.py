import unittest #get object from python library

#test_config is directory/folder path src../.. import the function to test like test_config
from src.examples.b_input_proc_output.input_process_output import exponentiate_me, float_division, get_remainder, multiply_numbers, test_config
from src.examples.b_input_proc_output.input_process_output import add_numbers
from src.examples.b_input_proc_output.input_process_output import add_some_numbers
from src.examples.b_input_proc_output.input_process_output import multiply_numbers
from src.examples.b_input_proc_output.input_process_output import integer_division
from src.examples.b_input_proc_output.input_process_output import operator_precedence_1
from src.examples.b_input_proc_output.input_process_output import operator_precedence_2
from src.examples.b_input_proc_output.input_process_output import exponentiate_me
from src.examples.b_input_proc_output.input_process_output import get_remainder

#class that makes it easy for us to create test case banks
class Test_Config(unittest.TestCase):

    def test_configuration(self):#class functions
        #if we execute test_config it will Return True (is True == True)
        self.assertEqual(True, test_config())

    def test_add_numbers_1(self):
        self.assertEqual(10, add_numbers(5, 5))

    def test_add_numbers_2(self):
        self.assertEqual(11, add_numbers(5, 6))

    def test_add_some_numbers(self):
        self.assertEqual(10, add_some_numbers())

    def test_multiply_numbers_w_out_params(self):
        self.assertEqual(25, multiply_numbers()) 

    def test_multiply_numbers_w_out_params(self):
        self.assertEqual(25, multiply_numbers()) #evaluate a function/test

    def test_integer_division_1(self):#test case
        self.assertEqual(2, integer_division(5, 2))#assertion
        self.assertEqual(3, integer_division(6, 2))#assertion

    def test_float_division(self):
        self.assertEqual(2.5, float_division(5, 2))#assertion
        self.assertEqual(3.3333333333333335, float_division(10, 3))
        self.assertEqual(3, float_division(6, 2))#assertion

    def test_operator_precedence_1(self):#12+6/3
        self.assertEqual(14, operator_precedence_1(12, 6, 3))

    def test_operator_precedence_2(self):#test case function
        self.assertEqual(6, operator_precedence_2(12, 6, 3))

    def test_exponentiate_me(self):
        self.assertEqual(256, exponentiate_me(2, 8))
        self.assertEqual(128, exponentiate_me(2, 7))
        self.assertEqual(64, exponentiate_me(2, 6))
        self.assertEqual(32, exponentiate_me(2, 5))
        self.assertEqual(16, exponentiate_me(2, 4))
        self.assertEqual(8, exponentiate_me(2, 3))
        self.assertEqual(4, exponentiate_me(2, 2))
        self.assertEqual(2, exponentiate_me(2, 1))
        self.assertEqual(1, exponentiate_me(2, 0))

    def test_get_remainder(self):
        self.assertEqual(1, get_remainder(5,2))
