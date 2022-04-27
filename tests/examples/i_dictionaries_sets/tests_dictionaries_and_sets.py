import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_dictionary_create(self):
        phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
        expected_dictionary = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}

        self.assertEqual(phonebook, expected_dictionary)

    def test_dictionary_update_value(self):
        phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
        phonebook['Katie'] = '555-4444'
        self.assertEqual(phonebook['Katie'], '555-4444')

    def test_dictionary_add_new_key_value(self):
        phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
        phonebook['Joe'] = '555-5555'
        self.assertEqual(phonebook['Joe'], '555-5555')

    def test_dictionary_delete_key_value_pair(self):
        phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
        del phonebook['Katie']
        expected_dictionary = {'Chris':'555−1111', 'Joanne':'555−3333'}
        self.assertEqual(phonebook, expected_dictionary)

    def test_dictionary_clear_method(self):
        phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
        phonebook.clear()
        expected_dictionary = {}
        self.assertEqual(phonebook, expected_dictionary)

    def test_dictionary_get_item(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
        v = phonebook.get('Chris')
        self.assertEqual(v, '555-1111')
        v = phonebook.get('chris')
        self.assertEqual(v, None) #default value is None

    def test_dictionary_pop(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        expected_dictionary = {'Chris':'555-1111', 'Joanne':'555-3333'}
        v = phonebook.pop('Katie')
        self.assertEqual(v, '555-2222')
        self.assertEqual(phonebook, expected_dictionary)

    def test_set_remove_element(self):
        myset = set(['one', 'two', 'three'])
        with self.assertRaises(KeyError):
            myset.remove('twoo')

        myset.remove('two')
        expected_set= set(['one', 'three'])
        self.assertEqual(myset, expected_set)

    def test_set_discard_element(self):
        myset = set(['one', 'two', 'three'])
       
        myset.discard('twoo')
        expected_set= set(['one', 'two', 'three'])
        self.assertEqual(myset, expected_set)

        myset.discard('two')
        expected_set= set(['one', 'three'])
        self.assertEqual(myset, expected_set)

    def test_clear_set(self):
        myset = set(['one', 'two', 'three'])
        myset.clear()
        expected_set = set()
        self.assertEqual(myset, expected_set)

    def test_set_union(self):
        set1 = set(['a', 'b', 'c'])
        set2 = set(['a', 'd', 'e'])
        expected_set = set(['a', 'b', 'c', 'd', 'e'])

        self.assertEqual(expected_set, set1 | set2)

    def test_set_intersection(self):
        set1 = set(['a', 'b', 'c'])
        set2 = set(['a', 'd', 'e'])
        expected_set = set(['a'])

        self.assertEqual(expected_set, set1 & set2)

    def test_set_difference(self):
        set1 = set(['a', 'b', 'c'])
        set2 = set(['a', 'd', 'e'])
        expected_set = set(['b', 'c'])

        self.assertEqual(expected_set, set1 - set2)

    def test_set_sym_difference(self):
        set1 = set(['a', 'b', 'c'])
        set2 = set(['a', 'd', 'e'])

        expected_set = set(['b', 'c', 'd', 'e'])
        self.assertEqual(expected_set, set1 ^ set2)




    



