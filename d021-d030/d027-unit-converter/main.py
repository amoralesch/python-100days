# Unit Converter

# Create a small GUI to help convert from miles to kilometers
#
# Learn about tkinter, and how to create forms

import tkinter as tk


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def calculate():
    text = input_field.get()

    if is_number(text):
        miles = float(input_field.get())
        kms = f'{(miles * 1.609344):.2f}'
    else:
        kms = 'ERR'

    km_value.config(text=kms)


WIDTH = 150
HEIGHT = 100
PADDING = 25

window = tk.Tk()

window.title("Miles to Kilometers Converter")
window.minsize(WIDTH, HEIGHT)
window.config(padx=PADDING, pady=PADDING)

input_field = tk.Entry(width=10)
input_field.grid(column=1, row=0)

miles_label = tk.Label(text='miles')
miles_label.grid(column=2, row=0)

info = tk.Label(text='is equal to')
info.grid(column=0, row=1)

km_value = tk.Label(text='0')
km_value.grid(column=1, row=1)

km_label = tk.Label(text='kms')
km_label.grid(column=2, row=1)

button = tk.Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

window.mainloop()
