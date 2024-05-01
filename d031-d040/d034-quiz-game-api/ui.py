import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = '#375362'
GAP = 20
FONT = ('Arial', 20, 'italic')


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.brain = quiz_brain
        self.last_question = None

        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(pady=GAP, padx=GAP, bg=THEME_COLOR)

        self.score_label = tk.Label(
            text='Score: 0',
            fg='white',
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(
            width=300,
            height=250,
            bg='white',
            highlightthickness=0)
        self.question_label = self.canvas.create_text(
            150, 125,
            width=280,
            text='Some question here',
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=GAP)

        false_img = tk.PhotoImage(file='images/false.png')
        self.false_button = tk.Button(
            image=false_img,
            highlightthickness=0,
            command=self.answer_false)
        self.false_button.grid(row=2, column=0)

        true_img = tk.PhotoImage(file='images/true.png')
        self.true_button = tk.Button(
            image=true_img,
            highlightthickness=0,
            command=self.answer_true)
        self.true_button.grid(row=2, column=1)
        self.show_next_question()

        self.window.mainloop()

    def show_next_question(self):
        self.canvas.config(bg='white')

        if self.brain.has_more_questions():
            self.last_question = self.brain.next_question()
            self.canvas.itemconfig(
                self.question_label,
                text=self.last_question.prompt())

    def answer_question(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.score_label.config(text=f'Score: {self.brain.score}')
        self.window.after(1000, self.show_next_question)

    def answer_false(self):
        self.answer_question(self.brain.answer('false'))

    def answer_true(self):
        self.answer_question(self.brain.answer('true'))
