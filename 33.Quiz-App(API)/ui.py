from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.old_score = 0
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.unknown_images = PhotoImage(file="images/false.png")
        self.known_images = PhotoImage(file="images/true.png")
        self.the_window()
        self.the_canvas()
        self.score()
        self.buttons()
        self.next_question()
        self.window.mainloop()

    def the_window(self):
        self.window.title("Quizz by AslaN")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    def the_canvas(self):
        self.canvas = Canvas(width=300, height=250)
        self.the_text = self.canvas.create_text(150, 125,
                                                text="Some Question Text",
                                                font=("Arial", 20, "italic"),
                                                fill="black", width=200)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def score(self):
        self.printing_score = Label(self.window, text="Score: 0", bg=THEME_COLOR, font=("Arial", 12, "italic"))
        self.printing_score.grid(row=0, column=1, columnspan=1)

    def update_score(self, score):
        self.printing_score.config(text=f"Score: {score}")

    def buttons(self):
        self.known_button = Button(image=self.known_images, highlightthickness=0, command=lambda: self.clicked("True"))
        self.known_button.grid(row=2, column=1)
        self.unknown_button = Button(image=self.unknown_images, highlightthickness=0,
                                     command=lambda: self.clicked("False"))
        self.unknown_button.grid(row=2, column=0)

    def clicked(self, answer):
        self.current_score = self.quiz_brain.check_answer(answer)
        self.update_le_canvas()
        self.update_score(self.current_score)
        if self.quiz_brain.still_has_questions():
            self.next_question()
        else:
            self.canvas.itemconfig(self.the_text,text = "You've reached the end of the quiz.")
            self.known_button.config(state='disabled')
            self.unknown_button.config(state='disabled')

    def update_le_canvas(self):
        new_score = self.current_score
        if self.old_score != new_score:
            self.canvas.config(bg="green", highlightthickness=1)
        else:
            self.canvas.config(bg="red", highlightthickness=1)
        self.window.after(200, self.reset_le_canvas)
        self.old_score = self.current_score

    def reset_le_canvas(self):
        self.canvas.config(bg="white", highlightthickness=0)

    def next_question(self):
        question = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.the_text, text=question)
