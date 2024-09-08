from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# -------------------------- SEARCH IN WEBSITE NAMES ---------------------------- #
def search_website():
    website_name = website_entry.get()
    try:
        with open("data.json", 'r') as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found!")
    else:
        if website_name in data_dict:
            messagebox.showinfo(title=website_name,
                                message=f"Website: {website_name}\nPassword: {data_dict[website_name]['password']}")
            pyperclip.copy(data_dict[website_name]['password'])
            return
        elif len(website_name) == 0:
            messagebox.showerror(title="Error", message="No Entry")
        else:
            messagebox.showerror(title="Error", message="Website Log In Info Not Found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    generated_password = "".join(password_list)
    # delete the last entry
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        web_name: {
            "email": email,
            "password": password}
    }

    if len(web_name) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Error", message="not enough character")
    else:
        try:
            with open(file="data.json", mode='r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open(file="data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open(file="data.json", mode='w') as data_file:
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        # email_entry.delete(0,END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(width=160, height=160, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(80, 80, image=lock_image)  # create lock image
canvas.grid(column=1, row=0)

# TODO labels
# label website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# label Email userName
email_userName_label = Label(text="Email/Username:")
email_userName_label.grid(column=0, row=2)
# label Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# TODO Entries
# EntryBox website
website_entry = Entry(width=27)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky='w')
# Entry Box Email
email_entry = Entry(width=46)
email_entry.insert(END, "pooryaardestani@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')
# Entry Box password
password_entry = Entry(width=27)
password_entry.grid(column=1, row=3, sticky='w')

# TODO Buttons
# Button Generate password
generate_password_button = Button(text="Generate password", command=generate_password, width=15)
generate_password_button.grid(column=2, row=3, sticky='w')
# Button Add
add_button = Button(text="ADD", width=39, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')
# Button Search
search_button = Button(text="Search", command=search_website, width=15)
search_button.grid(column=2, row=1, sticky='w')

window.mainloop()
