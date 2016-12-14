#!/usr/bin/python3
import pickle

from getpass import getpass
from Test import Test


class TeacherProfile:
	def __init__(self, profile_name, password):
		self.profile_name = profile_name
		self.password = password 
		self.tests = {}
		self.averages = {}

	def create_test(self):
		name = input("\nNew Test\n------------------\nPlease give this test a name: ")
		choices = 0
		while choices not in range(2, 11):
			choices = int(input("How many multiple choice answers would you like each question to have? Please stay between 2 and 10: "))
		new_test = Test(name, choices)
		number_questions = int(input("How many questions would you like to put on your test? "))
		for i in range(number_questions):
			new_test.add_question()
		self.tests[name] = new_test
		self.averages[name] = new_test.average
		print("\n----Test created: saved as '{}'----".format(name))
		which_mode(self)

	def administer_test(self):
		test_name = ''
		password = ''
		while test_name not in self.tests:
			print("\nYour current saved tests are: ")
			for test in self.tests:
				print(test)
			test_name = input("\nWhich test would you like to administer? ")
		self.averages[test_name] = self.tests[test_name].administer()
		while password != self.password:
			password = getpass("\nPlease enter the teacher password to continue to the Test Manager: ")
		which_mode(self)

	def view_results(self):
		print("\nTest        Average\n--------------------")
		for name, test in self.tests.items():
			print("{}        {}".format(name, self.averages[name]))
			

	def quit(self):
		pass





def load_teacher_profile():
	profile_name = input("Please enter your teacher profile name: ")
	try:
		current_profile = pickle.load(open(profile_name, "rb"))
	except FileNotFoundError:
		yes_or_no = input("No teacher profile by that name exists. Would you like to create a new profile? ")
		if yes_or_no.lower()[0] == 'y':
			password = getpass("Please enter your desired password: ")
			current_profile = TeacherProfile(profile_name, password)
		else:
			load_teacher_profile()
	return current_profile

def which_mode(current_profile):
	mode = ''
	modes = {'1': current_profile.create_test, '2': current_profile.administer_test, '3': current_profile.view_results, 'q': current_profile.quit}
	while mode not in modes:
		mode = input("\n------------------\n1: To create a test, type '1'\n2: To administer a test, type '2'\n3: To view the results of a test, type '3'\nTo quit the Test Manager, type 'q'\n>>")
	modes[mode]()




if __name__ == '__main__':
	current_profile = load_teacher_profile()
	which_mode(current_profile)
	

