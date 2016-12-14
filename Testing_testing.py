from unittest.mock import patch 
from random import randint

from Teachers_aide import TeacherProfile, load_teacher_profile, which_mode
from Test import Test, answer_choices


def fake_test_input(i):
	number_of_choices = randint(2,10)
	number_of_questions = randint(1,100)
	test_input = ['test '+str(i), number_of_choices, number_of_questions]
	for i in range(number_of_questions):
		correct_answer = answer_choices[randint(0, number_of_choices-1)]
		test_input += ['question'+str(i)] + ['choice'] * number_of_choices + [correct_answer]
	test_input += ['q']
	return test_input

def fake_student_input(profile, test, i):
	current_test = profile.tests[test].questions
	number_of_choices = len(current_test['question 1'] -1 )
	number_of_questions = len(current_test)
	student_answers = ["student " + str(i)]
	for _ in number_of_questions:
		student_answers += [answer_choices[randint(1, number_of_choices)]]
	return student_answers



teacher_input = ["Ms. Rage", "y", "password"]
with patch('builtins.input', side_effect = teacher_input):
	fake_profile = load_teacher_profile()
test_creation_input = []
student_test_input = []
for i in range(1,10):
	test_creation_input += [1] + fake_test_input(i)
with patch('builtins.input', side_effect = test_creation_input):
		which_mode(fake_profile)
for test in range(1, 10):
	for student in range(1, 30):
		student_test_input += ['2'] + ["test "+str(test)] + fake_student_input(fake_profile, "test "+str(test), student)