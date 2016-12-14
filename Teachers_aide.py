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
		for question, answers in self.questions.items():
			print(question)
			for answer in answers[0, len(answers) - 2]:
				print("{}: {}}".format(answer_choices)


def create_test():
	name = input("Please give this test a name: ")
	choices = 0
	while choices not in range(1, 11):
		choices = int(input("How many multiple choice answers would you like each question to have? Please stay between 1 and 10: "))
	new_test = Test(name, choices)
	number_questions = int(input("How many questions would you like to put on your test? "))
	for i in range(number_questions):
		new_test.add_question()
	return new_test

create_test()

