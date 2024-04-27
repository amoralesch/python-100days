# U.S. States

# Can you name all 50 states in the U.S.A.?
#
# Learn more about working with files, and about _pandas_ library

from turtle import Screen, Turtle
import pandas


def new_label(text, x, y):
    t = Turtle()
    t.speed('fastest')
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(text)


WIDTH = 725
HEIGHT = 491

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgpic('blank_states.gif')

guessed_states = []
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

while len(guessed_states) < 50:
    guess = screen.textinput(
        f'{len(guessed_states)}/50 States Correct',
        "What's another state's name?").strip().title()

    if guess == 'Exit':
        break

    if guess in guessed_states:
        continue

    if guess in all_states:
        state_info = data[data.state == guess]
        new_label(guess, int(state_info.x.iat[0]), int(state_info.y.iat[0]))
        guessed_states.append(guess)

missing_states = []

for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)

pandas.DataFrame(missing_states).to_csv(
    'output.csv',
    index_label='Index',
    header=['Name'])
