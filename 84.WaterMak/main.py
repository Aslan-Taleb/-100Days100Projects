from tkinter import *
from tkinter.filedialog import askopenfilenames

from PIL import ImageTk, Image, ImageDraw, ImageFont

FONT_APP = "system-ui"
images = []
images_not_resized = []
index = 0
b_save = -1


def add_files(canvas):
    global images, images_not_resized
    x, y = 50, 10  # initial coordinates
    file_path = askopenfilenames(initialdir="/",
                                 title="Select file",
                                 filetypes=[("jpeg", ".jpg .jpeg"), ("png", ".png"),
                                            ("bitmap", "bmp"),
                                            ("gif", ".gif")])
    for picture in file_path:
        if x >= 1200:
            y += 120
            x = 50
        img = Image.open(picture)
        resized_img = img.resize((120, 82))
        tk_img = ImageTk.PhotoImage(resized_img)
        canvas.create_image(x, y, image=tk_img, anchor='nw')
        images.append(tk_img)
        images_not_resized.append(img)
        x += 150
    canvas.images = images
    return True


def clear_canvas(canvas):
    canvas.delete("all")
    global images, images_not_resized, index
    images = []
    images_not_resized = []
    index = 0


def add_text(canvas):
    global index
    if images_not_resized:
        image = images_not_resized[index - 1]
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("arial.ttf", 36)
        text_color = (255, 255, 255)  # white
        # Define text to be added and its position
        text = "Hello, world!"
        text_position = (50, 50)  # (x, y)
        # Add text to image
        draw.text(text_position, text, font=font, fill=text_color)
        canvas.delete("all")
        canvas.create_image(0, 10, image=image, anchor='nw')
        tk_img = ImageTk.PhotoImage(image)
        canvas.images[index - 1] = tk_img


def file_to_change(canvas):
    global index
    if images_not_resized:
        try:
            image = ImageTk.PhotoImage(images_not_resized[index])
        except IndexError:
            phase_three(canvas)
        else:
            canvas.delete("all")
            canvas.create_image(0, 10, image=image, anchor='nw')
            tk_img = ImageTk.PhotoImage(image)
            canvas.images[index] = tk_img
            index += 1
            return True
    return False


def second_navbar(canvas):
    global b_save
    b_add.config(text="Add Text", command=lambda: add_text(canvas))
    b_clear.config(text="Add Logo", command="")
    b_save = Button(text="Save", highlightthickness=2, font=FONT_APP, fg='white', width=10, height=1,
                    bg="#2c2c2c", highlightbackground="white",
                    command="")
    b_save.grid(column=4, row=0, pady=(10, 0), padx=(18, 250))
    b_new_next = b_next.config(text="Next Picture >", command=lambda: file_to_change(canvas))
    file_to_change(canvas)


def reset():
    global images, images_not_resized, index, b_save
    images = []
    images_not_resized = []
    index = 0
    canvas.delete("all")
    b_save.grid_remove()

    b_add.config(text="Add Files", command=lambda: add_files(canvas))
    b_clear.config(text="Clear", command=lambda: clear_canvas(canvas))
    b_next.config(text="Next Step >", command=lambda: second_navbar(canvas))


def phase_three(canvas):
    clear_canvas(canvas)
    b_new_next = b_next.config(text="More Pictures ?", command=reset, width=15, padx=0)


window = Tk()
window.title("")
window.geometry("1280x960")
window.resizable(False, False)
window.configure(bg='#222222')

canvas = Canvas(height=896, width=1280, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=6)

frame = Frame(window, bg="#2c2c2c", width=1280, height=64, bd=0, highlightthickness=0)
frame.grid(row=0, column=0, columnspan=6)

b_exit = Button(text="Close App", highlightthickness=2, font=FONT_APP, fg='white', width=10, height=1,
                bg="#2c2c2c", highlightbackground="white",
                command="exit")
b_exit.grid(column=0, row=0, padx=(0, 400), pady=(10, 0))

b_add = Button(text="Add Files", highlightthickness=2, font=FONT_APP, fg='white', width=10, height=1,
               bg="#2c2c2c", highlightbackground="white",
               command=lambda: add_files(canvas))
b_add.grid(column=2, row=0, pady=(10, 0))

b_clear = Button(text="Clear", highlightthickness=2, font=FONT_APP, fg='white', width=10, height=1,
                 bg="#2c2c2c", highlightbackground="white",
                 command=lambda: clear_canvas(canvas))
b_clear.grid(column=3, row=0, pady=(10, 0))

b_next = Button(text="Next Step >", highlightthickness=2, font=FONT_APP, fg='white', width=12, height=1,
                bg="#1A6DFF", highlightbackground="white",
                command=lambda: second_navbar(canvas))
b_next.grid(column=4, row=0, pady=(10, 0), padx=(400, 0))

window.mainloop()
