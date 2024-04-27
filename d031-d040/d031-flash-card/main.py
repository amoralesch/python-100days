# Flash Cards

# Create an _Anki_ clone, present a word to the user, after a small
# timeout, show the translation. The user can then indicate if they
# knew the word or not. Words that are not known are stored in a
# separate file for later study. Can be customized to use questions
# instead of words
#
# More practice with `tkinter` and `pandas`.

import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"

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
canvas.create_text(
    400, 150,
    text='Title',
    font=('Ariel', 40, 'italic'),
    fill='black')
canvas.create_text(
    400, 263,
    text='word',
    font=('Ariel', 60, 'bold'),
    fill='black')
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = tk.Button(
    image=wrong_img,
    bg=BACKGROUND_COLOR,
    highlightthickness=0)
wrong_button.grid(row=1, column=0)

correct_button = tk.Button(
    image=correct_img,
    bg=BACKGROUND_COLOR,
    highlightthickness=0)
correct_button.grid(row=1, column=1)

window.mainloop()
