from turtle import Turtle

FONT = ('Courier', 24, 'normal')
MAX_SCORE = 2


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        top = (self.screen.window_height() / 2) - 50
        offset = self.screen.window_width() / 4
        self.goto(-offset, top)
        self.write(self.l_score, font=FONT)
        self.goto(offset, top)
        self.write(self.r_score, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.show_score()

    def l_point(self):
        self.l_score += 1
        self.show_score()

    def is_game_over(self):
        game_over = self.r_score >= MAX_SCORE or self.l_score >= MAX_SCORE

        if game_over:
            self.home()
            self.write('Game Over!', align='center', font=FONT)

        return game_over
