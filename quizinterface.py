from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quizler App")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score", fg="white", highlightthickness=0, bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        image1 = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=image1, highlightthickness=0, command= self.true_pressed)
        self.correct_button.grid(row=2, column=0)

        image2 = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=image2, highlightthickness=0, command= self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(125, 150, width=240,
                                                     text="some question", fill=THEME_COLOR,
                                                     font=("Arial" ,20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():

            self.score.config(text=f"score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="ypu have reached the last question")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        self.canvas.config(bg="white")

    def true_pressed(self):
       # is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.windows.after(1000, self.get_next_question)


