#!/usr/bin/python3

from collections import OrderedDict

answer_choices = ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J"]


class Test:
	def __init__(self, name, choices):
		self.name = name
		self.choices = choices
		self.questions = OrderedDict()
		self.answer_choices = answer_choices[:choices]
		self.scored_students = {}

	def add_question(self):
		new_question = input('\nPlease type the next question: ')
		answers = []
		for i in range(self.choices):
			next_answer = input("Please enter the answer choice {}: ".format(self.answer_choices[i]))
			answers.append(next_answer)
		correct = ''
		while correct not in answer_choices:
			correct = input("Please enter the letter of the correct answer choice: ").upper()
		answers.append(correct)
		self.questions[new_question] = answers

	def administer(self):
		student_name = input("Please enter the student's name: ")
		if student_name in self.scored_students:
			print("That student has already taken this test. Their score was: {}".format(scored_students(student_name)))
		else:
			total_correct = 0
			for question, answers in self.questions.items():
				print("\n{}".format(question))
				for choice in answers[:len(answers) - 1]:
					print("{}: {}".format(answer_choices[answers.index(choice)], choice))
				answer = ''
				while answer not in self.answer_choices:
					answer = input("Please enter the letter of your answer choice: ").upper()
				if answer == answers[self.choices]:
					total_correct += 1
			score = total_correct / len(self.questions) * 100
			print("\nThat's the end of the test! Your score was {}%".format(score))
			self.scored_students[student_name] = score



