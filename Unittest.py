import unittest
from unittest.mock import patch 
from Teachers_aide import Test

class TestCreateTest(unittest.TestCase):

	def test_can_create_question(self):
		test_test = Test("test_name", 4)
		with patch('builtins.input', side_effect = ['question 1', 'choice 1', 'choice 2', 'choice 3', 'choice 4', 'A']):
			test_test.add_question()
		self.assertEqual(test_test.questions, {'question 1': ['choice 1', 'choice 2', 'choice 3', 'choice 4', 'A']})

if __name__ == '__main__':
    unittest.main()