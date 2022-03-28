import unittest

from src.examples.h_strings.strings import concat_strings, slice_string, string_sub_string, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual("john doe", concat_strings("john ", "doe"))

    def test_slice_strings(self):
        self.assertEqual("Lynn", slice_string("Patty Lynn Smith"))

    def test_get_first_name(self):
        name = "Patty Lynn Smith"
        self.assertEqual("Patty", name[:5])

    def test_get_last_name(self):
        name = "Patty Lynn Smith"
        self.assertEqual("Smith", name[11:])

    def test_slice_w_step_value(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertEqual("ACEGIKMOQSUWY", letters[0:26:2])

    def test_string_sub_string(self):
        str = "Four score and seven years ago"
        sub_string = "seven"
        self.assertEqual(True, string_sub_string(str, sub_string))
        self.assertNotEqual(True, string_sub_string(str, "eight"))
        self.assertEqual(False, string_sub_string(str, "eight"))

    def test_string_methods(self):
        str = "1200"
        self.assertEqual(True, str.isdigit())
        str = "abc"
        self.assertEqual(True, str.isalpha())
        str = "abc"
        self.assertEqual(True, str.isalnum())

    def test_string_modification_methods(self):
        str = "joe"
        self.assertEqual("JOE", str.upper())
        str = "JOE"
        self.assertEqual("joe", str.lower())
        str = "john doe"
        self.assertEqual("john smith", str.replace("doe", "smith"))

    def test_string_repetition(self):
        str = 'w' * 5
        self.assertEqual(str, "wwwww")

    

