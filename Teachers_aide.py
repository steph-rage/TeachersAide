#!/usr/bin/python3

answer_choices = ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J"]

class Test:
	def __init__(self, name, choices):
		self.name = name
		self.choices = choices
		self.questions = {}
		self.answer_choices = answer_choices[:choices]

	def add_question(self):
		new_question = input('Please type the next question: ')
		answers = []
		for i in range(self.choices):
			next_answer = input("Please enter the answer choice {}: ".format(self.answer_choices[i]))
			answers.append(next_answer)
		correct = ''
		while correct not in answer_choices:
			correct = input("Please enter the letter of the correct answer choice: ").upper()
		answers.append(correct)
		self.questions[new_question] = answers

	def administer_test(self):
		total_correct = 0
		for question, answers in self.questions.items():
			print(question)
			for choice in answers[:len(answers) - 1]:
				print("{}: {}".format(answer_choices[answers.index(choice)], choice))
			answer = ''
			while answer not in self.answer_choices:
				answer = input("Please enter the letter of your answer choice: ").upper()
			if answer == answers[self.choices]:
				total_correct += 1
		score = total_correct / len(self.questions)
		print(score)



def create_test():
	name = input("Please give this test a name: ")
	choices = 0
	while choices not in range(2, 11):
		choices = int(input("How many multiple choice answers would you like each question to have? Please stay between 2 and 10: "))
	new_test = Test(name, choices)
	number_questions = int(input("How many questions would you like to put on your test? "))
	for i in range(number_questions):
		new_test.add_question()
	return new_test

if __name__ == '__main__':
	my_test = create_test()
	my_test.administer_test()

