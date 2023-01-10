from tkinter import *
from tkinter import messagebox
from password import generate_password
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def get_password():
    key = generate_password()
    pyperclip.copy(key)
    password.insert(string=key, index=0)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    op = f"{website.get()} | {username.get()} | {password.get()}\n"
    if website.get() == "" or username.get() == "" or password.get() == "":
        messagebox.showwarning(title="Oops", message= "Don't leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=website.get(), message=f"These are the details entered: \nEmail: {username.get()}\nPassword: {password.get()}")
    
    if is_ok:
        with open("data.txt","a") as file:
            file.write(op)
        website.delete(0,END)
        password.delete(0,END)


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

website = Entry(width=35)
website.focus()
website.grid(row=1, column=1, columnspan=2)

username = Entry(width=35)
username.insert(string="naren@mail.com",index=0)
username.grid(row=2, column=1, columnspan=2)

password = Entry(width=20)
password.grid(row=3, column=1)

generate_password_btn = Button(text="Generate Password", width=10, command=get_password)
generate_password_btn.grid(row=3, column=2)

add_button = Button(text="Add", command=add)
add_button.config(width=32)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()