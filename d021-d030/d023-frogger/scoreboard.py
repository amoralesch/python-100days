from turtle import Turtle

FONT = ('Courier', 24, 'normal')
GAP = 30


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color('black')

        x_home = -(self.screen.window_width() / 2) + GAP
        y_home = (self.screen.window_height() / 2) - GAP

        self.level = 0
        self.goto(x_home, y_home)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_score()

    def game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=FONT)
