# Import the parent class from main menu (base) file, and create a child class for quiz creator.
from quiz_main_menu_base import quiz_base

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
        correct_answer = input("Enter the correct answer(A, B, C, D): ")

    # add the question, possible answers, and the correct answer in a txt file.
        file.write(f"Question #{question_number}: {user_questions}\n")
        file.write(f"A. {choice_a}\n")
        file.write(f"B. {choice_b}\n")
        file.write(f"C. {choice_c}\n")
        file.write(f"D. {choice_d}\n")
        file.write(f"Correct Answer: {correct_answer}\n")
        file.write("\n") # add space to seperate the Questions.