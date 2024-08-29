from turtle import Turtle

FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(0, (self.screen.window_height() / 2) - 40)
        self.print_score()

    def add_to_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(f'Score: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.home()
        self.write('Game Over!', align='center', font=FONT)
