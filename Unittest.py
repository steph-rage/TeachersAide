import unittest
from unittest.mock import patch 
from random import randint

from Teachers_aide import Test, answer_choices, create_test

class TestCreateTest(unittest.TestCase):

	def test_create_test(self):
		number_of_choices = randint(2,10)
		number_of_questions = randint(1,100)
		test_input = ['test name', number_of_choices, number_of_questions]
		actual_questions = {}
		for _ in range(number_of_questions):
			correct_answer = answer_choices[randint(0, number_of_choices-1)]
			test_input += ['question'] + ['choice'] * number_of_choices + [correct_answer]
			actual_questions['question'] = ['choice'] * number_of_choices + [correct_answer]
		with patch('builtins.input', side_effect = test_input):
			test_test = create_test()
		self.assertEqual(actual_questions, test_test.questions)

if __name__ == '__main__':
    unittest.main()