# Quiz base class for quiz creator the parent class.
class quiz_base:
    def __init__(self, filename="user_quiz.txt"):
        self.filename = filename

    def save_question(self, question_data):
        with open(self.filename, "a") as file:
            file.write(f"Question #{question_data['number']}: {question_data['question']}\n")
            file.write(f"A. {question_data['A']}\n")
            file.write(f"B. {question_data['B']}\n")
            file.write(f"C. {question_data['C']}\n")
            file.write(f"D. {question_data['D']}\n")
            file.write(f"Correct Answer: {question_data['correct']}\n")
            file.write("\n")