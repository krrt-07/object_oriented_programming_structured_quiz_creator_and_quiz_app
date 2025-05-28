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

    # load questions from text file, open the file in read mode.
    def load_questions(self):
        with open(self.filename, "r") as file:
            content = file.read().strip().split("\n\n")

        questions = []
        for block in content:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                continue

            try:
                question = lines[0].split(": ", 1)[1]
                choices = {
                    "A": lines[1][3:],
                    "B": lines[2][3:],
                    "C": lines[3][3:],
                    "D": lines[4][3:]
                }
                correct = lines[5].split(": ")[1].strip().upper()

                questions.append({
                    "question": question,
                    "choices": choices,
                    "correct": correct
                })
            except:
                continue

        return questions