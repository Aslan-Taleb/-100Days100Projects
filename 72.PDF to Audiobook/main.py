import pyttsx3 as tts
from PyPDF2 import PdfReader
import docx2txt
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

# reading word file
def read_word_files(f_name):
    return docx2txt.process(f_name)

# reading pdf file
def read_pdf_files(f_name):
    file_obj = PdfReader(f_name)
    return "".join([file_obj.pages[i].extract_text() for i in range(len(file_obj.pages))])

# reading simple text file
def read_text_files(f_name):
    with open(f_name) as file:
        return file.read()

def upload_files_from_computer():
    filetypes = [('Choose File', '*.pdf *.docx *.doc *.txt')]
    file_name = askopenfilename(filetypes=filetypes)
    user_file_entry.insert(0, file_name)

def convert_text_to_audio():
    if not user_file_entry.get():
        return
    file_name = user_file_entry.get()
    if file_name[-3:].lower() == "pdf":
        file_text = read_pdf_files(file_name)
    elif file_name[-3:].lower() == "txt":
        file_text = read_text_files(file_name)
    elif file_name[-4:].lower() == "docx":
        file_text = read_word_files(file_name)
    else:
        messagebox.showerror(title="Wrong File name", message="Please enter a valid file name")
        return
    file_name = file_name.split('/')[-1]
    convert_text_to_audio_using_pyttsx3_tts(file_text, file_name)
    messagebox.showinfo(title="Successful", message=f"Your text file \"{file_name}\" has been convert to Audio!!")
    user_file_entry.delete(0, END)
    user_file_entry.focus()
    window.iconify()

def convert_text_to_audio_using_pyttsx3_tts(file_text, file_name):
    engine = tts.init()
    engine.save_to_file(file_text, f"audio_files/{file_name.split('.')[0]}.mp3")
    engine.runAndWait()

############# GUI ###############
window = Tk()
window.title("From PDF to Audio by AslaN")
window.geometry("623x420")
window.resizable(False, False)
canvas = Canvas(window, width=623, height=420)
canvas.place(x=0, y=0)
user_file_entry = Entry(width=38, font=("Arial", 14))
user_file_entry.place(x=100, y=197)
user_file_entry.focus()

label = Label(window, text="Too tired to read? Use my Script!", font=("Arial", 20))

label.place(x=110, y=20)
tutorial_text = """
Instructions:
1. Click on the 'Browse' button to select a PDF, DOCX, DOC, or TXT file.
2. Once the file is selected, the file path will appear in the text box.
3. Click on the 'Convert' button to convert the file to audio.
4. The audio file will be saved in the 'audio_files' directory.
"""
tutorial_label = Label(window, text=tutorial_text, font=("Arial", 12), justify=LEFT)
tutorial_label.place(x=40, y=70)
upload_photo_button = Button(window, text="Browse", width=10,  height=1, font=("Arial", 18, "bold"),
                             background="#343a40", activeforeground="blue", foreground="white",
                             command=upload_files_from_computer)
upload_photo_button.place(x=100, y=240)

convert_button = Button(window, text="Convert", width=10, height=1, font=("Arial", 18, "bold"),
                        background="#343a40",
                        activebackground="red", activeforeground="white", foreground="white",
                        command=convert_text_to_audio)
convert_button.place(x=363, y=240)
window.bind('<Return>', convert_text_to_audio())

window.mainloop()