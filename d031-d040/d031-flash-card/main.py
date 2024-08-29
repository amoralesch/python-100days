# Flash Cards

# Create an _Anki_ clone, present a word to the user, after a small
# timeout, show the translation. The user can then indicate if they
# knew the word or not. Words that are not known are stored in a
# separate file for later study. Can be customized to use questions
# instead of words
#
# More practice with `tkinter` and `pandas`.

import tkinter as tk
import random
import pandas


def get_data():
    try:
        data_load = pandas.read_csv(KNOWN_WORDS)
    except FileNotFoundError:
        data_load = pandas.read_csv(DEFAULT_WORDS)

    return data_load.to_dict(orient='records')


def show_answer(selection):
    global timer_handler
    language = 'English'
    word = selection[language]
    timer_handler = None

    canvas.itemconfig(image_handler, image=back_img)
    canvas.itemconfig(title_label, text=language, fill='white')
    canvas.itemconfig(word_label, text=word, fill='white')


def show_new_word():
    global timer_handler
    global selected_record
    selected_record = random.choice(data)

    language = 'French'
    word = selected_record[language]

    canvas.itemconfig(image_handler, image=front_img)
    canvas.itemconfig(title_label, text=language, fill='black')
    canvas.itemconfig(word_label, text=word, fill='black')

    if timer_handler is not None:
        window.after_cancel(timer_handler)

    timer_handler = window.after(TIME_OUT, show_answer, selected_record)


def word_known():
    data.remove(selected_record)

    df = pandas.DataFrame(data)
    df.to_csv(KNOWN_WORDS, index=False)

    show_new_word()


DEFAULT_WORDS = 'data/french_words.csv'
BACKGROUND_COLOR = "#B1DDC6"
TIME_OUT = 3000
KNOWN_WORDS = 'data/output.csv'

data = get_data()
timer_handler = None
selected_record: dict | None = None

window = tk.Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

front_img = tk.PhotoImage(file='images/card_front.png')
back_img = tk.PhotoImage(file='images/card_back.png')
correct_img = tk.PhotoImage(file='images/right.png')
wrong_img = tk.PhotoImage(file='images/wrong.png')

canvas = tk.Canvas()
canvas.config(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0)
image_handler = canvas.create_image(400, 263, image=front_img)
title_label = canvas.create_text(
    400, 150,
    text='Title',
    font=('Ariel', 40, 'italic'),
    fill='black')
word_label = canvas.create_text(
    400, 263,
    text='word',
    font=('Ariel', 60, 'bold'),
    fill='black')
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = tk.Button(
    image=wrong_img,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=show_new_word)
wrong_button.grid(row=1, column=0)

correct_button = tk.Button(
    image=correct_img,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=word_known)
correct_button.grid(row=1, column=1)

show_new_word()

window.mainloop()
