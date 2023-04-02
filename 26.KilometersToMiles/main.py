from tkinter import *

window = Tk()
window.title("Kilometer To Mile Converter")
window.minsize(width=800, height=600)

my_label = Label(text="Welcome")
my_label.pack()

input = Entry()
input.pack()

def oops():
    name = input.get()
    my_label["text"] = "Welcome " + name +" ! "

button = Button(text="What's your Name ?", command=oops)
button.pack()

window.mainloop()
