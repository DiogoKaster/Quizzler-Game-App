from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=290, text="Hello", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_q)
        self.false_button.grid(row=2, column=1)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_q)
        self.true_button.grid(row=2, column=0)

        self.label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            new_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_question)
        else:
            self.canvas.itemconfig(self.question_text, text="No more question available")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_q(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_q(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_question)
