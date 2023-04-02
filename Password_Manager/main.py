from tkinter import *
from tkinter import messagebox
from password import *
import pyperclip


def generationPassword():
    password_entry.delete(0, END)
    password = generatePassword()
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ----------------------------------------------------------------#
def save():
    var_website = website_entry.get().replace(" ", "")
    email = email_entry.get().replace(" ", "")
    var_password = password_entry.get().replace(" ", "")
    if var_website == "" or var_password == "":
        messagebox.showinfo(title="Oops",
                            message="Please fill out all required fields before submitting the form.")
    else:
        ok = messagebox.askokcancel(title="Are you sure about that ?",
                                    message=f"Thank you for adding a new account!\nWebsite: {var_website}\nEmail: {email}\nPassword: {var_password}\nNote: Your password has been copied to your clipboard. To paste, press Ctrl+V.")
        if ok:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{var_website} | {email} | {var_password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------------------------------------------------#

window = Tk()
window.title("Password Manager by AslaN")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white", fg="#2196F3", font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0, pady=(10, 0))
website_label.focus()
email_label = Label(text="Email/Username:", bg="white", fg="#2196F3", font=("Arial", 12, "bold"))
email_label.grid(row=2, column=0, pady=(10, 0))
password_label = Label(text="Password:", bg="white", fg="#2196F3", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0, pady=(10, 0))

# Entries
website_entry = Entry(width=35, bg="#F5F5F5", font=("Arial", 12))
website_entry.grid(row=1, column=1, columnspan=2, pady=(10, 0))
var_website = website_entry.get()
website_entry.focus()

email_entry = Entry(width=35, bg="#F5F5F5", font=("Arial", 12))
email_entry.grid(row=2, column=1, columnspan=2, pady=(10, 0))

email_entry.insert(0, "aslantalebselim@gmail.com")

password_entry = Entry(width=21, bg="#F5F5F5", font=("Arial", 12),show = "*")
password_entry.grid(row=3, column=1, pady=(10, 0))

# Buttons
generate_password_button = Button(text="Generate Password", bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                                  command=generationPassword)
generate_password_button.grid(row=3, column=2, pady=(10, 0))
add_button = Button(text="Add", width=36, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=(20, 0))

window.mainloop()
