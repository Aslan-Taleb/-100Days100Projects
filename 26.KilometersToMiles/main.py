from tkinter import *


def from_km_to_miles(km):
    if km.isdigit():
        float_km = float(km)
    else:
        float_km = 0.0
    miles = float_km * 0.621371
    return miles


def button_clicked():
    km = input.get()
    result = round(from_km_to_miles(km), 2)
    my_label_2.config(text=result)


window = Tk()
window.title("Km to Mile Converter")
window.minsize(width=150, height=100)
window.config(padx=10, pady=10)

# Label
my_label = Label(text="is equal to")
my_label.grid(column=0, row=2)

my_label_2 = Label(text="0")
my_label_2.grid(column=2, row=2)

my_label_3 = Label(text="Km")
my_label_3.grid(column=3, row=1)

my_label_4 = Label(text="Miles")
my_label_4.grid(column=3, row=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=1)

window.mainloop()
