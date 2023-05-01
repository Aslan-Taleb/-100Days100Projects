from tkinter import Button, Canvas, Label, PhotoImage, Tk
import tkinter
from bs4 import BeautifulSoup
from lxml import etree

import requests

FONT_NAME = "Courier"
BACKGROUND = "#000000"
class Screen:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed By AslaN")
        self.window.config(padx=80, pady=30, bg=BACKGROUND)
        self.window.geometry("300x160")
        self.box_text_play = None
        self.parcour = 0
        self.word_search = ""
        #self.window.minsize(600, 400)
        #self.window.maxsize(600, 400)
        self.text = self.make_text_list()
        self.menu()
   
        self.window.mainloop()
        
    def menu(self):
        self.title_label = Label(text="Typing Speed", fg="#fff",
                                 font=(FONT_NAME, 15), bg=BACKGROUND)
        self.title_label.grid(column=0, row=0)
        
        self.btn_start = Button(
            text="Start", highlightthickness=0, command=lambda: [self.game_setup(), self.title_label.destroy(), self.btn_start.destroy(), self.btn_instruction.destroy()])
        self.btn_start.grid(column=0, row=2, pady=10)
        
        self.btn_instruction = Button(
            text="Instruction", highlightthickness=0, command="")
        self.btn_instruction.grid(column=0, row=3)
        
        
    def game_setup(self):
        self.window.geometry("600x300")
        self.window.config(padx=0, pady=20)
        self.box_text = tkinter.Text(
            self.window, height=10, width=60, background=BACKGROUND, fg="white", wrap=tkinter.WORD)
        self.box_text.insert(tkinter.END, self.text)
        self.box_text.grid(column=0, row=1, padx=12)

        # Define the 'correct' and 'incorrect' tags
        self.box_text.tag_configure('correct', background=  'green')
        self.box_text.tag_configure('incorrect', background = 'red')
        self.box_text.tag_configure('gray', background='gray')
        self.box_text.tag_configure('black', background='black')

        self.btn_restart = Button(
            text="Restart", highlightthickness=0, command=self.game_setup)
        self.btn_restart.grid(row=2, column=1)

        self.box_text_play = tkinter.Text(
            self.window, height=5, width=60, background=BACKGROUND, fg="white", wrap=tkinter.WORD)
        self.box_text_play.grid(column=0, row=2, padx=12, pady=10)
        # Bind the <space> key event to the Text widget
        self.box_text_play.bind("<space>", self.the_game)












    def the_game(self, event):
        self.make_it_shine()
        word = self.box_text_play.get(
            "1.0", tkinter.END).replace(' ', '').replace('\n', '')
        self.box_text_play.delete('1.0', 'end')
        self.word_search = self.text[self.parcour]
        del self.text[self.parcour]
        print(f"{self.text}\n\n\n\n")
        if word == self.word_search:
            # Apply the 'correct' tag to the current word
            
            word_start = self.box_text.search(word, '1.0', tkinter.END)
            word_end = f"{word_start}+{len(word)}c"
            self.box_text.tag_add(
                'correct', word_start, word_end)
        else:
            # Apply the 'incorrect' tag to the current word
            word_start = self.box_text.search(
                self.word_search, '1.0', tkinter.END)
            word_end = f"{word_start}+{len(self.word_search)}c"
            self.box_text.tag_add(
                'incorrect', word_start, word_end)
        self.box_text.tag_remove("gray", word_start, word_end)
        self.parcour += 1
        if self.parcour >= len(self.text):
            print("Game over")
   









        
    def make_text_list(self):
        text_to_play = self.text_to_play()
        return text_to_play.split()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def make_it_shine(self):
        index = self.parcour+1
        word = self.text[index]
        word_start = self.box_text.search(word, '1.0', tkinter.END)
        word_end = f"{word_start}+{len(word)}c"
        self.box_text.tag_add(
            'gray', word_start, word_end)












 

    def text_to_play(self):
        response = requests.get(
            'https://randomword.com/paragraph')
        # Check if request was successful
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None
        page = response.text
        soup = BeautifulSoup(page, "html.parser")
        paragraph = soup.find(id="random_word_definition").text
        return paragraph
        
        
        
        
        
        
        
    def tkt(self):
        self.lab_time = Label(text="Time",
                                font=(FONT_NAME, 10), bg=BACKGROUND)
        self.lab_time.grid(row=0,column=0, pady=10)
        
        
        
        self.lab_mistakes = Label(text="Mistakes",
                                font=(FONT_NAME, 10), bg=BACKGROUND)
        self.lab_mistakes.grid(row=0,column=1)
        
        
        
        self.lab_mistakes = Label(text="W/M",
                                    font=(FONT_NAME, 10), bg=BACKGROUND)
        self.lab_mistakes.grid(column=2, row=0)
        

        
        

def main():
    screen = Screen()


main()
            
