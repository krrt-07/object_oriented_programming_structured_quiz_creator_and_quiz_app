# make the Quiz App.
# make it randomize the questions.
import tkinter as tk
import random
from quiz_main_menu_base import quiz_base

class quiz_app(quiz_base):
    def __init__(self, master):
        super().__init__()  # Inherit filename
        self.master = master
        self.master.title("Quiz App")
        self.master.geometry("500x400")
        self.master.resizable(False, False)

        self.quiz_questions = self.load_questions()
        random.shuffle(self.quiz_questions)
        self.current_index = 0
        self.score = 0

        self.question_label = tk.Label(master, font=("Arial", 16), wraplength=480)
        self.question_label.pack(pady=20)

        self.choice_buttons = {}
        for choice in ["A", "B", "C", "D"]:
            btn = tk.Button(master, font=("Arial", 12), width=40,
                            command=lambda c=choice: self.check_answer(c))
            btn.pack(pady=5)
            self.choice_buttons[choice] = btn

        self.feedback = tk.Label(master, font=("Arial", 14))
        self.feedback.pack(pady=10)

        self.next_button = tk.Button(master, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.show_question()

    def show_question(self):
        if self.current_index < len(self.quiz_questions):
            q = self.quiz_questions[self.current_index]
            self.question_label.config(text=f"Q: {q['question']}")
            for key in q["choices"]:
                self.choice_buttons[key].config(text=f"{key}. {q['choices'][key]}", state=tk.NORMAL)
            self.feedback.config(text="")
            self.next_button.config(state=tk.DISABLED)
        else:
            self.question_label.config(text="🎉 Quiz Finished!")
            for btn in self.choice_buttons.values():
                btn.config(state=tk.DISABLED)
            self.feedback.config(text=f"Final Score: {self.score}/{len(self.quiz_questions)}")
            self.next_button.config(state=tk.DISABLED)

    def check_answer(self, selected):
        q = self.quiz_questions[self.current_index]
        for btn in self.choice_buttons.values():
            btn.config(state=tk.DISABLED)

        if selected == q["correct"]:
            self.score += 1
            self.feedback.config(text="✅ Tama!", fg="green")
        else:
            self.feedback.config(text=f"❌ Mali. Tamang sagot: {q['correct']}", fg="red")

        self.score_label.config(text=f"Score: {self.score}")
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_index += 1
        self.show_question()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = quiz_app(root)
    root.mainloop()