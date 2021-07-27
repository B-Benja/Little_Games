import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WINDOW_HEIGHT = 250
WINDOW_WIDTH = 300
FONT = ("Arial", 15, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = tk.Label(text="Score: 0", fg="white", font=FONT, bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = tk.Canvas(height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bg="white")
        self.quiz_content = self.canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="Question Text",
                                                    fill=THEME_COLOR, font=FONT, width=WINDOW_WIDTH)
        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)

        correct_img = tk.PhotoImage(file="images/true.png")
        self.correct_button = tk.Button(image=correct_img, highlightthickness=0, command=self.answer_true)
        self.correct_button.grid(column=0, row=3)
        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def answer_true(self):
        correct_answer = self.quiz.check_answer("True")
        self.give_feedback(correct_answer)

    def answer_false(self):
        correct_answer = self.quiz.check_answer("False")
        self.give_feedback(correct_answer)

    def get_next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_questions():
            output = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_content, text=output)
        else:
            self.canvas.itemconfig(self.quiz_content, text=f"You got {self.quiz.score} out of {len(self.quiz.question_list)} Questions correct")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, correct_answer):
        if correct_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




