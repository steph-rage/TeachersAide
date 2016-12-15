from unittest.mock import patch 
from random import randint

from Teachers_aide import TeacherProfile, load_teacher_profile, which_mode
from Test import Test, answer_choices


#Create input to answer the console questions when creating a fake test
def fake_test_input(i):
	test_name = 'Test '+str(i)
	number_of_choices = 4
	number_of_questions = 10
	test_input = [test_name, number_of_choices, number_of_questions]
	for i in range(number_of_questions):
		correct_answer = answer_choices[randint(0, number_of_choices-1)]
		test_input += ['question'+str(i)] + ['choice'] * number_of_choices + [correct_answer]
	return test_input

#Create input for a fake student to answer a test
def fake_student_input(profile, i):
	number_of_choices = 4
	number_of_questions = 10
	student_answers = ["Student " + str(i)]
	for _ in range(number_of_questions):
		student_answers += [answer_choices[randint(0, number_of_choices-1)]]
	return student_answers


#Make a fake teacher profile
teacher_input = ["Ms. Rage", "y", "password"]
with patch('builtins.input', side_effect = teacher_input):
	fake_profile = load_teacher_profile()

#Put together input strings to test all 3 modes
test_creation_input = []
student_test_input = []
test_view_input = ['3', '1', '3', '2', 'Test ' + str(randint(1,10)), '3', '3', 'Student ' + str(randint(1,10)), 'q']
for i in range(1,10):
	test_creation_input += ['1'] + fake_test_input(i)

for test in range(1, 10):
	for student in range(1, 10):
		student_test_input += ['2'] + ["Test "+str(test)] + fake_student_input(fake_profile, student) + ['password']

total_testing_input = test_creation_input + student_test_input + test_view_input 

with patch('builtins.input', side_effect = total_testing_input):
		which_mode(fake_profile)


