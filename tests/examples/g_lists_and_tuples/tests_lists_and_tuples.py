import unittest

from src.examples.g_lists_and_tuples.lists import append_item_to_list, find_item_in_list, get_2d_list_item, get_gross_pay, get_multiplication_table, return_list, sum_list_items, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_list_index(self):
        even_numbers = [2,4,6,8,10]
        self.assertEqual(even_numbers[0],2)
        self.assertEqual(even_numbers[2],6)

    def test_list_index_strings(self):
        prog_lang = ["Java", "C++", "C#", "Python"]
        self.assertEqual(prog_lang[1], "C++")
        self.assertEqual(prog_lang[3], "Python")

    def test_list_dif_data_types(self):
        my_address =[123, "Main Street", 78660, True, 50.99, [1,2,3]]
        self.assertEqual(my_address[1], "Main Street")

    def test_create_list_w_range(self):
        nums = list(range(5))
        expected_list = [0,1,2,3,4]
        self.assertEqual(nums, expected_list)

    def test_create_list_of_odd_numbers(self):
        nums = list(range(1, 10, 2))
        expected_list = [1,3,5,7,9]
        self.assertEqual(nums, expected_list)

    def test_create_list_w_repetion_operator(self):
        nums = [0] * 5
        expected_list = [0,0,0,0,0]
        self.assertEqual(nums, expected_list)

    def test_concat_lists(self):
        list1 = [1,2,3,4]
        list2 = [5,6,7,8]
        list3 = list1 + list2
        expected_list = [1,2,3,4,5,6,7,8]
        self.assertEqual(list3, expected_list)

    def test_concat_string_list(self):
        prog_lang = ["C++", "C#"]
        prog_lang +=  ["Python", "Java"]
        expected_list = ["C++", "C#", "Python", "Java"]
        self.assertEqual(prog_lang, expected_list)

    def test_list_slicing_days(self):
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        expected_list = ['Tuesday', 'Wednesday', 'Thursday']
        mid_days = days[2:5]
        self.assertEqual(expected_list, mid_days)

    def test_list_slice_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list1 = numbers[1:10:2]
        expected_list = [2,4,6,8, 10]
        self.assertEqual(list1, expected_list)

    def test_find_item_in_list(self):
        list1 = ["C++", "C#", "Python", "Java"]
        self.assertEqual(True, find_item_in_list("C++", list1))
        self.assertEqual(False, find_item_in_list("Ada", list1))

    def test_append_item_to_list(self):
        list1 = []
        append_item_to_list("C++", list1)
        append_item_to_list("Python", list1)
        expected_list = ["C++", "Python"]
        self.assertEqual(expected_list, list1)

    def test_copy_one_list(self):
        list1 = ["C++", "C#", "Java"]
        list2 = list1
        list2[0] = "Ada"
        self.assertEqual(False, list1[0] == "C++")
        self.assertEqual(True, list1[0] == "Ada")

    def test_copy_one_list_w_iteration(self):
        list1 = ["C++", "C#", "Java"]
        list2 = [] + list1

        #for item in list1:
         #   list2.append(item)

        list2[0] = "Ada"
        self.assertEqual(True, list1[0] == "C++")
        self.assertEqual(True, list2[0] == "Ada")

    def test_get_gross_pay(self):
        self.assertEqual(400, get_gross_pay(40, 10))
        self.assertEqual(800, get_gross_pay(40, 20))

    def test_sum_list_items(self):
        list1 = [2,4,6,8,10]

        self.assertEqual(30, sum_list_items(list1))

    def test_return_list(self):
        list1 = return_list()
        expected_list = [2,4,6,8,10]
        self.assertEqual(expected_list, list1)

    def test_get_2d_list_item(self):
        list_2d = [["C++", "C#"], ["Java", "Javascript"], ["C", "Simula"]]
        expected_list0 = ["C++", "C#"]
        self.assertEqual(expected_list0, get_2d_list_item(0, list_2d))

    def test_2d_list_indexing(self):
        list_2d = [["C++", "C#"], ["Java", "Javascript"], ["C", "Simula"]]
        self.assertEqual("C#", list_2d[0][1])
        self.assertEqual("Simula", list_2d[2][1])

    def test_get_multiplication_table(self):
        expected_list = [[1,2,3],[2,4,6],[3,6,9]]
        self.assertEqual(expected_list, get_multiplication_table(4))
        



        







