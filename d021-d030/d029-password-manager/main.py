# Password Manager

# Create a basic app to generate and store passwords locally.
# This is just an exercise, passwords are stored in plain text.
# DO NOT USE this app for storing your info.
#
# Practice more about `tkinter`, pop-up messages, column span, and
# new library called _pyperclip_.

import tkinter as tk
from tkinter import messagebox
import pyperclip
import random

PADDING = 50
LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '*', '(', ')', '+']


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(
            title='Error',
            message='Cannot save with missing fields, please review.')
        return

    should_save = messagebox.askokcancel(
        title='Save record?',
        message=f'Do you want to save information for {website}?')

    if should_save:
        with open('output.tsv', 'a') as data_file:
            data_file.write(f'{website}\t{email}\t{password}\n')

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


def generate_password():
    letters = [random.choice(LETTERS) for _ in range(random.randint(4, 8))]
    numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
    symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]

    password_list = letters + numbers + symbols
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


window = tk.Tk()
window.config(padx=PADDING, pady=PADDING)
window.title('Password Manager')

# Logo
logo = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = tk.Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = tk.Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = tk.Entry(width=38)
email_entry.insert(0, 'admin@company.tld')
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = tk.Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)
save_button = tk.Button(text='Save', width=36, command=save)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
