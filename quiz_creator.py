# Import the parent class from main menu (base) file, and create a child class for quiz creator.
from quiz_main_menu_base import quiz_base

class quiz_creator(quiz_base):
    def run(self):
        question_number = 0
        while True:
            print("Type (exit) to stop adding questions.")
            question = input("Enter a question: ")
            if question.lower() == "exit":
                print("Exiting quiz creator.")
                break

        # ask for the possible answers in (A, B, C, D)
        choice_a = input("Enter a possible answer, A: ")
        choice_b = input("Enter a possible answer, B: ")
        choice_c = input("Enter a possible answer, C: ")
        choice_d = input("Enter a possible answer, D: ")

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