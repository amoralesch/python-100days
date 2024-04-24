# Pomodoro App

# Create an app to help execute the Pomodoro Technique:
# Work uninterrupted by 25 minutes, then rest for 5 minutes,
# repeat 4 times, last rest is for 20 minutes.
#
# Work with `tkinter`, create multiple elements, add events
# and logic.

import tkinter as tk
import math

BREAK_BG = "#e2979c"
REST_BG = "#e7305b"
FOREGROUND = "#9bdeac"
BACKGROUND = "#f7f5dd"
FONT_NAME = "Courier"
PADDING = 100
WORKING_TIMER = 10000  # 25 * 60 * 1000 # milliseconds
BREAK_TIMER = 2000  # 5 * 60 * 1000 # milliseconds
REST_TIMER = 5000  # 20 * 60 * 1000 # milliseconds

timeout_handler: str | None = None


def reset_pomodoro():
    if timeout_handler is not None:
        window.after_cancel(timeout_handler)
        canvas.itemconfig(timer_id, text="--:--")
        title_label.config(text="Timer")
        marks_label.config(text="")


def format_time(milliseconds):
    min = math.floor(milliseconds / 1000 / 60)
    secs = math.floor((milliseconds - min * 1000 * 60) / 1000)

    if secs < 10:
        secs = f'0{secs}'

    label = f'{min}:{secs}'

    return label


def move_timer(stage, time):
    global timeout_handler
    label = format_time(time)
    canvas.itemconfig(timer_id, text=label)
    time -= 1000

    if time < 0:
        stage += 1
        marks = '✓' * math.floor(stage / 2)
        marks_label.config(text=marks)

        if stage % 2 == 1:
            time = WORKING_TIMER
            title_label.config(text='WORK', fg=FOREGROUND)
        elif stage % 8 == 0:
            time = REST_TIMER
            title_label.config(text='REST', fg=REST_BG)
        else:
            time = BREAK_TIMER
            title_label.config(text='BREAK', fg=BREAK_BG)

    timeout_handler = window.after(1000, move_timer, stage, time)


def start_timer():
    stage = 1
    title_label.config(text='WORK', fg=FOREGROUND)
    move_timer(stage, WORKING_TIMER)


window = tk.Tk()
window.title('Pomodoro Tracker')
window.config(pady=PADDING, padx=PADDING, bg=BACKGROUND)

title_label = tk.Label(
    text='Timer',
    fg=FOREGROUND,
    bg=BACKGROUND,
    font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

bg_image = tk.PhotoImage(file='tomato.png')
canvas = tk.Canvas(
    width=200,
    height=224,
    bg=BACKGROUND,
    highlightthickness=0)
canvas.create_image(100, 112, image=bg_image)
timer_id = canvas.create_text(
    100,
    130,
    fill='white',
    text='--:--',
    font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = tk.Button(
    text='Start',
    bg=BACKGROUND,
    font=FONT_NAME,
    command=start_timer,
    highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tk.Button(
    text='Reset',
    bg=BACKGROUND,
    font=FONT_NAME,
    command=reset_pomodoro,
    highlightthickness=0)
reset_button.grid(row=2, column=2)

marks_label = tk.Label(
    text='',
    fg=FOREGROUND,
    bg=BACKGROUND,
    font=FONT_NAME)
marks_label.grid(row=3, column=1)

window.mainloop()
