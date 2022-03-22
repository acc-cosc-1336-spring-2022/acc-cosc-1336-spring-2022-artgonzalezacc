import unittest

from src.examples.c_decisions.decisions import is_even, is_letter_consonant, logical_op_precedence, num_is_not_in_range_or, number_is_in_range_and, nums_is_not_in_range_and, test_config
from src.examples.c_decisions.decisions import is_even
from src.examples.c_decisions.decisions import get_letter_grade

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_not_truth_table(self):
        self.assertEqual(not True, False)
        self.assertEqual(not False, True)

    def test_and_truth_table(self):
        self.assertEqual(True and True, True)
        self.assertEqual(True and False, False)
        self.assertEqual(False and True, False)
        self.assertEqual(False and False, False)

    def test_or_truth_table(self):
        self.assertEqual(True or True, True)
        self.assertEqual(True or False, True)
        self.assertEqual(False or True, True)
        self.assertEqual(False or False, False)

    def test_is_even(self):
        self.assertEqual(True, is_even(4))
        self.assertEqual(False, is_even(5))

    def test_character_comparison(self):
        self.assertEqual('a' == 'A', False)
        self.assertEqual('a' > 'A', True)

    def test_get_letter_grade(self):
        self.assertEqual('Invalid Number', get_letter_grade(1000))
        self.assertEqual('A', get_letter_grade(90))
        self.assertEqual('B', get_letter_grade(85))
        self.assertEqual('C', get_letter_grade(75))
        self.assertEqual('D', get_letter_grade(65))
        self.assertEqual('F', get_letter_grade(55))
        self.assertEqual('F', get_letter_grade(35))
        self.assertEqual('Invalid Number', get_letter_grade(-10))

    def test_logical_op_precedence(self):
        self.assertEqual(True, logical_op_precedence(True, False, True))
        self.assertEqual(False, logical_op_precedence(False, False, False))

    def test_number_is_in_range(self):
        self.assertEqual(True, number_is_in_range_and(20, 100, 50))
        self.assertEqual(True, number_is_in_range_and(20, 100, 20))
        self.assertEqual(True, number_is_in_range_and(20, 100, 100))
        self.assertEqual(False, number_is_in_range_and(20, 100, 101))

    def test_number_is_not_in_range(self):
        self.assertEqual(True, nums_is_not_in_range_and(20, 100, 101))
        self.assertEqual(False, nums_is_not_in_range_and(20, 100, 50))

    def test_number_is_not_in_range_or(self):
        self.assertEqual(True, num_is_not_in_range_or(20, 100, 101))
        self.assertEqual(False, num_is_not_in_range_or(20, 100, 50))

    def test_is_letter_consonant(self):
        self.assertEqual(False, is_letter_consonant('a'))
        self.assertEqual(True, is_letter_consonant('z'))


