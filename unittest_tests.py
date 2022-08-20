import unittest
from unittest.mock import patch
import main


class TestArchive(unittest.TestCase):

    @patch('builtins.input', return_value="2207 876234")
    def test_search_people(self, mock_input):
        result = main.search_people()
        expected_result = "Василий Гупкин"
        self.assertEqual(result, expected_result)

    @patch('builtins.input', return_value='10006')
    def test_find_sheil(self, mock_input):
        result = main.find_sheil()
        expected_result = 'Документ находится на полке № 2'
        self.assertEqual(result, expected_result)

    @patch('builtins.input', return_value='3')
    def test_add_document_true(self, mock_input):
        type, number, name = "passport", "115912", 'Джек Неровных'
        result = main.add_document(type, number, name,)
        expected_result = True
        self.assertEqual(result, expected_result)
        self.assertIn({"type": type, "number": number, "name": name}, main.documents)
        main.documents.remove({"type": type, "number": number, "name": name})
        main.directories[mock_input()].pop()

    @patch('builtins.input', return_value='4')
    def test_add_document_false(self, mock_input):
        type, number, name = "passport", "115912", 'Джек Неровных'
        result = main.add_document(type, number, name)
        expected_result = False

        self.assertEqual(result, expected_result)
        self.assertNotIn({"type": type, "number": number, "name": name}, main.documents)

    @patch('builtins.input', return_value='5')
    def test_add_sheil_true(self, mock_input):
        result = main.add_sheil()
        expected_result = True

        self.assertEqual(result, expected_result)
        self.assertIn('5', main.directories)
        main.directories.pop('5')

    @ patch('builtins.input', return_value='1')
    def test_add_sheil_false(self, mock_input):
        result = main.add_sheil()
        expected_result = False

        self.assertEqual(result, expected_result)
        self.assertIn('1', main.directories)

    @patch('builtins.input', return_value="2207 876234")
    def test_delete_document(self, mock_input):
        shail = main.find_sheil().split('№ ')[-1]
        result = main.delete_document()
        expected_result = True

        self.assertEqual(result, expected_result)
        self.assertNotIn({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, main.documents)

        main.directories[shail].append(mock_input())
        main.documents.append({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"})