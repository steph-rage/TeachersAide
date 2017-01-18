# Teacher's Aide 

Given the assignment:

	Write a single command line tool for teachers, which can be used to create, give, and view the results of tests.  It should be possible to switch between those three modes without exiting the program; however, switching from Mode 2 to either of the other modes should require a password.  You may hardcode the password.


	Mode 1: Creating a test

	The teacher needs to create and save tests.  A test is a list of questions, each of which has a list of possible answers, along with an indication of which answer is correct.  Develop an interactive interface that allows the teacher to do this.


	Mode 2: Taking a test

	The school’s budget is very limited; they only have one computer.  The teacher needs to be able to select a saved test, enter a student’s name, and then have the student sit down and take the test.  Do not allow the same student to take the same test twice.

	At the end of the test, the student should be shown the percentage of questions that they answered correctly.


	Mode 3: Viewing results

	The teacher needs to be able to:

	- choose a test, and see a list of all the students who took the test and the grade they each got on the test, along with the average score for the test
	- see a list of tests along with the average score students got on each test
	- choose a student, and see a list of all the tests they’ve taken and the grade they got on each test, along with their overall grade (weighting all tests equally) 


## Getting Started

This program is a command line interface which a teacher can use to create, assign, and see the results of multiple choice tests. 

### Prerequisites

Download the requirements.txt file and run

		pip install -r requirements.txt

### Running

After installing the program, you can run the file using Python 3. 

The program will prompt you to answer questions, first creating a profile and then creating tests. Once your test(s) have been created, you can assign it(them) to a student who will be immediately graded on finishing the test. You can also view the results any of three different ways. Just type in the commands for what you want to see. 

## Running the Tests

To run the automated tester, run the Testing_testing.py program using Python 3. It will generate a fake profile and randomly generate/then take 10 tests. Then it will show you the results from these tests in three different ways. 