import unittest

from human_resources import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    show_document_info, show_all_docs_info, add_new_doc


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('setUp - work')

    def tearDown(self):
        print('tearDown - work')

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass - work')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass - work')

    def test_check_document_existance(self):
        array = [{'type': 'A', 'number': '2', 'name': 'B'},
                 {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertTrue(check_document_existance('5', array))
        self.assertFalse(check_document_existance('1', array))

    def test_1_get_doc_owner_name(self):
        array = [{'type': 'A', 'number': '2', 'name': 'B'},
                 {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertEqual(get_doc_owner_name('5', array), 'C')

    def test_2_get_doc_owner_name(self):
        array = [{'type': 'A', 'number': '2', 'name': 'B'},
                 {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertIsNone(get_doc_owner_name('1', array))

    def test_1_get_all_doc_owners_names(self):
        array = [{'type': 'A', 'number': '2', 'name': 'B'},
                 {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertEqual(get_all_doc_owners_names(array), {'B', 'C'})

    def test_2_get_all_doc_owners_names(self):
        array = [{'type': 'A', 'number': '2', 'name': 'B'},
                 {'type': 'C', 'number': '5', 'error': 'C'}]
        self.assertFalse(get_all_doc_owners_names(array))

    def test_remove_doc_from_shelf(self):
        dictionary = {'1': ['a', 'b', 'c'],
                      '2': ['d', 'e', 'f']}
        remove_doc_from_shelf('e', dictionary)
        self.assertNotIn('e', dictionary['2'])

    def test_1_add_new_shelf(self):
        dictionary = {'1': ['a', 'b', 'c'],
                      '2': ['d', 'e', 'f']}
        self.assertEqual(add_new_shelf('3', dictionary), ('3', True))

    def test_2_add_new_shelf(self):
        dictionary = {'1': ['a', 'b', 'c'],
                      '2': ['d', 'e', 'f']}
        self.assertEqual(add_new_shelf('2', dictionary), ('2', False))

    def test_3_add_new_shelf(self):
        dictionary = {'1': ['a', 'b', 'c'],
                      '2': ['d', 'e', 'f']}
        add_new_shelf('3', dictionary)
        self.assertEqual(len(dictionary), 3)

    def test_4_add_new_shelf(self):
        dictionary = {'1': ['a', 'b', 'c'],
                      '2': ['d', 'e', 'f']}
        add_new_shelf('2', dictionary)
        self.assertEqual(len(dictionary), 2)

    def test_1_append_doc_to_shelf(self):
        dictionary = {'1': ['a', 'b', 'c'],
                      '2': ['d', 'e', 'f']}
        self.assertEqual(append_doc_to_shelf('s', '2', dictionary), ['d', 'e', 'f', 's'])

    def test_2_append_doc_to_shelf(self):
        dictionary = {'1': ['a', 'b', 'c'],
                      '2': ['d', 'e', 'f']}
        self.assertEqual(append_doc_to_shelf('s', '3', dictionary), ['s'])

    def test_1_delete_doc(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'C'}]
        delete_doc('5', documents, directories)
        self.assertNotIn({'type': 'C', 'number': '5', 'name': 'C'}, documents)

    def test_2_delete_doc(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'C'}]
        delete_doc('5', documents, directories)
        self.assertNotIn('5', directories['2'])

    def test_3_delete_doc(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertEqual(delete_doc('5', documents, directories), ('5', True))

    def test_4_delete_doc(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertEqual(delete_doc('1', documents, directories), ('1', False))

    def test_1_get_doc_shelf(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertEqual(get_doc_shelf('5', documents, directories), '2')

    def test_2_get_doc_shelf(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'C'}]
        self.assertFalse(get_doc_shelf('1', documents, directories))

    def test_1_move_doc_to_shelf(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        move_doc_to_shelf('5', '3', directories)
        self.assertIn('5', directories['3'])

    def test_2_move_doc_to_shelf(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        move_doc_to_shelf('5', '1', directories)
        self.assertIn('5', directories['1'])

    def test_3_move_doc_to_shelf(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        move_doc_to_shelf('5', '1', directories)
        self.assertNotIn('5', directories['2'])

    def test_4_move_doc_to_shelf(self):
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        el_1 = '8'
        el_2 = '3'
        text = f'Документ номер "{el_1}" был перемещен на полку номер "{el_2}"'
        self.assertEqual(move_doc_to_shelf(el_1, el_2, directories), text)

    def test_1_show_document_info(self):
        data = {'type': 'A', 'number': '2', 'name': 'B'}
        text = f'{data["type"]} "{data["number"]}" "{data["name"]}"'
        self.assertEqual(show_document_info(data), text)

    def test_1_show_all_docs_info(self):
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'D'}]
        self.assertIn('A "2" "B"', show_all_docs_info(documents))
        self.assertIn('C "5" "D"', show_all_docs_info(documents))

    def test_1_add_new_doc(self):
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'D'}]
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        add_new_doc('7', 'E', 'F', '2', documents, directories)
        self.assertIn({'type': 'E', 'number': '7', 'name': 'F'}, documents)

    def test_2_add_new_doc(self):
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'D'}]
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        add_new_doc('7', 'E', 'F', '2', documents, directories)
        self.assertIn('7', directories['2'])

    def test_3_add_new_doc(self):
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'D'}]
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        add_new_doc('7', 'E', 'F', '3', documents, directories)
        self.assertIn('7', directories['3'])

    def test_4_add_new_doc(self):
        documents = [{'type': 'A', 'number': '2', 'name': 'B'},
                     {'type': 'C', 'number': '5', 'name': 'D'}]
        directories = {'1': ['1', '2', '3'],
                       '2': ['4', '5', '6']}
        self.assertEqual(add_new_doc('7', 'E', 'F', '2', documents, directories), '2')


if __name__ == '__main__':
    unittest.main()
