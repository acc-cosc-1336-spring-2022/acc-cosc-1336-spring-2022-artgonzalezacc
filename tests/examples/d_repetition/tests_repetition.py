import unittest

from src.examples.d_repetition.repetition import get_sum, get_sum_for, sum_of_squares, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares(self):
        self.assertEqual(14, sum_of_squares(3))

    def test_get_sum(self):
        self.assertEqual(6, get_sum(3))

    def test_get_sum_for(self):
        self.assertEqual(6, get_sum_for(3))

