from tkinter import *
from tkinter import messagebox
import pyperclip
from password import generatePassword
from json import *


def generate_password():
    password_entry.delete(0, END)
    password = generatePassword()
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    var_website = website_entry.get().replace(" ", "")
    email = email_entry.get().replace(" ", "")
    var_password = password_entry.get().replace(" ", "")
    new_data = {
        var_website: {
            "email": email,
            "password": var_password,
        }
    }
    if var_website == "" or var_password == "":
        messagebox.showinfo(title="Oops",
                            message="Please fill out all required fields before submitting the form.")
    else:
        ok = messagebox.askokcancel(title="Are you sure about that?",
                                    message=f"Thank you for adding a new account!\nWebsite: {var_website}\nEmail: "
                                            f"{email}\nPassword: {var_password}\nNote: Your password has been copied "
                                            f"to your clipboard. To paste, press Ctrl+V.")

        if ok:
            try:
                with open("data.json", "r") as file:
                    # reading
                    json_data = load(file)
                    # writing
                    json_data.update(new_data)
            except:
                with open("data.json", "w") as file:
                    # updating
                    dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    # updating
                    dump(json_data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    var_website = website_entry.get().replace(" ", "")
    if var_website == "":
        messagebox.showinfo(title="Oops",
                            message="Please fill out Website Field.")
    else:
        try:
            with open("data.json", "r") as file:
                # reading
                json_data = load(file)
        except:
            messagebox.showinfo(title="Oops",
                                message="No Data file found")
        else:
            try:
                user_email = json_data[var_website]["email"]
                user_password = json_data[var_website]["password"]
            except KeyError:
                messagebox.showinfo(title="Website Not Found",
                                    message=f"The website '{var_website}' was not found. Please check your spelling "
                                            f"and try again.")
            else:
                messagebox.showinfo(title=f"{var_website}",
                                    message=f"User : {user_email}\nPassword : {user_password}")
                pyperclip.copy(user_password)


# Créer la fenêtre principale
window = Tk()
window.title("Password Manager by AslaN")
window.config(padx=50, pady=50, bg="white")

#logo
canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# champs d'entrée
website_label = Label(text="Website:", bg="white", fg="#2196F3", font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0, pady=(20, 10))

email_label = Label(text="Email/Username:", bg="white", fg="#2196F3", font=("Arial", 12, "bold"))
email_label.grid(row=2, column=0, pady=10)

password_label = Label(text="Password:", bg="white", fg="#2196F3", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0, pady=10)

website_entry = Entry(width=35, bg="#F5F5F5", font=("Arial", 12), borderwidth=0, highlightthickness=1,
                      highlightcolor="#c2c2c2")
website_entry.grid(row=1, column=1, pady=(20, 10), columnspan=2)
website_entry.focus()

email_entry = Entry(width=35, bg="#F5F5F5", font=("Arial", 12), borderwidth=0, highlightthickness=1,
                    highlightcolor="#c2c2c2")
email_entry.grid(row=2, column=1, pady=10, columnspan=2)
email_entry.insert(0, "aslantalebselim@gmail.com")

password_entry = Entry(width=35, bg="#F5F5F5", font=("Arial", 12), borderwidth=0, highlightthickness=1,
                       highlightcolor="#c2c2c2", show="*")
password_entry.grid(row=3, column=1, pady=10, columnspan=2)

#boutons
generate_password_button = Button(text="Generate Password", bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                                  command=generate_password, borderwidth=0, highlightthickness=1,
                                  highlightcolor="#c2c2c2")
generate_password_button.grid(row=3, column=3, pady=10, padx=10)

add_button = Button(text="Add", width=30, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), command=save,
                    borderwidth=0, highlightthickness=1, highlightcolor="#c2c2c2")
add_button.grid(row=4, column=1, pady=(20, 0), columnspan=2)

search_password_button = Button(text="Search", bg="#2196F3", fg="white", font=("Arial", 12, "bold"), borderwidth=0,
                                highlightthickness=1, highlightcolor="#c2c2c2", command=search)
search_password_button.grid(row=1, column=3, pady=10)

# Lancer la boucle principale
window.mainloop()
