#!/usr/bin/python3
import os

from collections import OrderedDict


#Possible answer choices for students: reasonable assumption made that teachers 
#will not want to have more than 10 answer choices per question
answer_choices = ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J"]


#Used from within Teachers_aide any time a teacher wants to create a new test
#or interact with an existing test
class Test:
	def __init__(self, name, choices):
		self.name = name
		self.choices = choices
		self.questions = OrderedDict()
		self.answer_choices = answer_choices[:choices]
		self.scored_students = {}
		self.average = 0

	def add_question(self):
		new_question = input('\nType the next question: ')
		answers = []
		for i in range(self.choices):
			next_answer = input("Enter the answer choice {}: ".format(self.answer_choices[i]))
			answers.append(next_answer)
		correct = ''
		while correct not in answer_choices:
			correct = input("Enter the letter of the correct answer choice: ").upper()
		answers.append(correct)
		self.questions[new_question] = answers

	def administer(self):
		#Clear the terminal so that a student cannot scroll backwards and see test answers
		clear = lambda:os.system('tput reset')
		clear()

		print("-------{}-------".format(self.name))
		student_name = input("Student name: ")
		if student_name in self.scored_students:
			print("That student has already taken this test. Their score was: {}".format(self.scored_students[student_name]))
		else:
			total_correct = 0
			for question, answers in self.questions.items():
				print("\n{}".format(question))
				for choice in answers[:len(answers) - 1]:
					print("{}: {}".format(answer_choices[answers.index(choice)], choice))
				answer = ''
				while answer not in self.answer_choices:
					answer = input("Your answer choice: ").upper()
				print(answer)
				if answer == answers[self.choices]:
					total_correct += 1
			score = round(total_correct / len(self.questions) * 100, 2)
			#Give student their score immediately
			print("\nThat's the end of the test! Your score was {}%".format(score))

			#Add the student and their score to the list of students who have taken the test
			self.scored_students[student_name] = score

			#And return a new average for all students who have taken the test
			self.average = round(((len(self.scored_students)-1)*self.average + score)/len(self.scored_students), 2)
			return [student_name, self.average]

	def show_results(self):
		print('\nShowing student results for {}:\n---------------------'.format(self.name))
		for student, score in self.scored_students.items():
			print("{}        {}%".format(student, score))
		print("------------\nAverage = {}%".format(self.average))



