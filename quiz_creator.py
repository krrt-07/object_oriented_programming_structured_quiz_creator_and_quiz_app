# Import the parent class from main menu (base) file, and create a child class for quiz creator.
from quiz_main_menu_base import quiz_base
#for testing purposes.
import sys
sys.dont_write_bytecode = True

class quiz_creator(quiz_base):
    def run(self):
        # initialize the quiz number to 0.
        question_number = 0
        while True:
            print("Type (exit) to stop adding questions.")
            # ask questionand if the user wants to exit type "exit".
            question = input("Enter a question: ")
            if question.lower() == "exit":
                print("Exiting quiz creator.")
                break

            # add 1 to the question number if the user type a question.
            question_number += 1

            # ask the user to input the question.
            choices = {
                "A": input("Enter choice A: "),
                "B": input("Enter choice B: "),
                "C": input("Enter choice C: "),
                "D": input("Enter choice D: "),
            }

            # input the correct answer.
            correct = input("Enter the correct answer (A, B, C, D): ").upper()

            # save the question and answers to a text file.
            question_data = {
                "number": question_number,
                "question": question,
                "A": choices["A"],
                "B": choices["B"],
                "C": choices["C"],
                "D": choices["D"],
                "correct": correct
            }

            self.save_question(question_data)

# run function to start the quiz creator.
if __name__ == "__main__":
    creator = quiz_creator()
    creator.run()