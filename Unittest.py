import unittest
from unittest.mock import patch 
from random import randint
from collections import OrderedDict

from Teachers_aide import Test, answer_choices, create_test

class TestMethodTests(unittest.TestCase):

	def create_fake_test(self):
		number_of_choices = randint(2,10)
		number_of_questions = randint(1,100)
		test_input = ['test name', number_of_choices, number_of_questions]
		actual_questions = OrderedDict()
		for i in range(number_of_questions):
			correct_answer = answer_choices[randint(0, number_of_choices-1)]
			test_input += ['question'+str(i)] + ['choice'] * number_of_choices + [correct_answer]
			actual_questions['question'+str(i)] = ['choice'] * number_of_choices + [correct_answer]
		return [test_input, actual_questions, number_of_choices]

	def test_create_test(self):
		fake_test = self.create_fake_test()
		test_input = fake_test[0]
		actual_questions = fake_test[1]
		with patch('builtins.input', side_effect = test_input):
			test_test = create_test()
		self.assertEqual(actual_questions, test_test.questions)

#This seems dumb: I'm just going to be writing the same code over again...
	'''def test_administer_test(self):
		questions = self.create_fake_test()[1]
		student_answers = []
		for _ in len(questions):
			student_answers += answer_choices[randint]'''


if __name__ == '__main__':
    unittest.main()