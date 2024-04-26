# Password Manager - Advance

# Update the project from day 29 to use JSON as the storing format,
# and add search functionality.
#
# Learn about exceptions, and how to catch them.

import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import json

PADDING = 50
LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
DB_FILE = 'output/output.json'


def save_passwords(data):
    with open(DB_FILE, 'w') as data_file:
        json.dump(data, data_file, indent=2)


def load_passwords():
    try:
        with open(DB_FILE) as data_file:
            return json.load(data_file)
    except FileNotFoundError:
        with open(DB_FILE, 'w') as data_file:
            json.dump({}, data_file)
            return {}


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title='Error',
            message='Cannot save with missing fields, please review.')
        return

    new_record = {
        website: {
            'email': email,
            'password': password
        }
    }

    existing_data = load_passwords()
    existing_data.update(new_record)
    save_passwords(existing_data)

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


def search_password():
    website = website_entry.get()
    data = load_passwords()

    if website not in data:
        messagebox.showerror(title='Error', message=f'No entry found for {website}.')
    else:
        email = data[website]['email']
        password = data[website]['password']
        msg = f'Email: {email}\nPassword: {password}'
        messagebox.showinfo(title=f'{website}', message=msg)


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
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)
email_entry = tk.Entry(width=38)
email_entry.insert(0, 'admin@company.tld')
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = tk.Button(text='Search', width=13, command=search_password)
search_button.grid(row=1, column=2)
generate_button = tk.Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)
save_button = tk.Button(text='Save', width=36, command=save)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
