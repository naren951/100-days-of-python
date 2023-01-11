from tkinter import *
from tkinter import messagebox
from password import generate_password
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def get_password():
    key = generate_password()
    pyperclip.copy(key)
    password_entry.insert(string=key, index=0)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website, username, password = website_entry.get(), username_entry.get(), password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message= "Don't leave any fields empty!")
    else:
        new_data = {
            website:{
                'username' : username,
                'password' : password 
            }
        }
        try:
            with open("data.json","r") as file:
                data = json.load(file)
                
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title="Oops", message= "Please enter the website to search!")
    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Oops", message= "No Data File Found!")
        else:
            try:
                details = data[website]
            except KeyError:
                messagebox.showwarning(title="Oops", message= "No details for this Website exists!")
            else:
                messagebox.showinfo(title=website, message= f"Email: {details['username']}\nPassword: {details['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row=0,column=1)

Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(row=1, column=1)

username_entry = Entry(width=35)
username_entry.insert(string="naren@mail.com",index=0)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

generate_password_btn = Button(text="Generate Password", width=11, command=get_password)
generate_password_btn.grid(row=3, column=2)

search_btn = Button(text="Search", command=search)
search_btn.config(width=11)
search_btn.grid(row=1, column=2)

add_button = Button(text="Add", command=add)
add_button.config(width=33)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()