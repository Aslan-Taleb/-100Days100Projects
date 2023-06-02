from time import sleep
import time
from tkinter import Button, Canvas, Label, PhotoImage, Tk, messagebox
import tkinter
from bs4 import BeautifulSoup
from lxml import etree

import requests

FONT_NAME = "Courier"
BACKGROUND = "#000000"


class Screen:
    def __init__(self, highest_score):
        self.window = Tk()
        self.window.title("Typing Speed By AslaN")
        self.window.config(padx=80, pady=30, bg=BACKGROUND)
        self.window.minsize(150, 150)
        self.word_end = '1.0'
        self.box_text_play = None
        self.correct_words = 0
        self.word_search = ""
        self.start_time = None
        self.time_value = -1
        self.mistakes_value = 0
        self.wm_value = 0
        self.word_count = 0
        self.highest_wp = highest_score
        self.text_to_play()
        self.menu()
        self.window.mainloop()

    def menu(self):
        """
        This method sets up the menu screen of the typing game.
        """
        self.title_label = Label(text="Typing Speed", fg="#fff",
                                 font=(FONT_NAME, 25), bg=BACKGROUND)
        self.title_label.grid(column=0, row=0, pady=(0, 2))

        self.btn_start = Button(
            text="Start", font=(FONT_NAME, 15, "bold"), bg="#146C94", command=lambda: [self.game_setup(), self.title_label.destroy(), self.btn_start.destroy(), self.btn_instruction.destroy()])
        self.btn_start.grid(column=0, row=2, pady=10)

        self.btn_instruction = Button(
            text="Instruction", font=(FONT_NAME, 15, "bold"), bg="#146C94", command=lambda: [self.show_info(), self.btn_start.destroy(), self.btn_instruction.destroy()])
        self.btn_instruction.grid(column=0, row=3)

    def game_setup(self):
        # Create progress bar and start the timer
        self.bar()
        self.start_timer()

        # Create the text box and insert the text
        self.box_text = tkinter.Text(
            self.window, height=15, width=60, background=BACKGROUND, fg="white", wrap=tkinter.WORD)
        self.box_text.configure(font=(FONT_NAME, 20))
        self.box_text.insert(tkinter.END, self.text)
        self.box_text.grid(column=0, row=1, padx=12)

        # Define the 'correct' and 'incorrect' tags for highlighting the text
        self.box_text.tag_configure('correct', background='green')
        self.box_text.tag_configure('incorrect', background='red')
        self.box_text.tag_configure('gray', background='gray')
        self.box_text.tag_configure('black', background='black')

        # Create the restart button
        self.btn_restart = Button(
            text="Restart", highlightthickness=0, font=(FONT_NAME, 15, "bold"), bg="#19A7CE", command=lambda: [self.restart()])
        self.btn_restart.grid(row=2, column=1)

        # Create the text box for typing
        self.box_text_play = tkinter.Text(
            self.window, height=5, width=60, background=BACKGROUND, fg="white", wrap=tkinter.WORD)
        self.box_text_play.configure(font=(FONT_NAME, 15))
        self.box_text_play.grid(column=0, row=2, padx=12, pady=10)

        # Bind the <space> key event to the Text widget for typing
        self.box_text_play.bind("<space>", self.the_game)

    def the_game(self, event):
        # Get the word entered by the user
        word = self.box_text_play.get(
            "1.0", tkinter.END).replace(' ', '').replace('\n', '')

        # Clear the input box
        self.box_text_play.delete('1.0', 'end')

        # Get the next word to search for
        self.word_search = self.text[0]
        # Remove the next word from the list of remaining words
        del self.text[0]

        # Find the start of the next occurrence of the word to search for
        next_word_start = self.box_text.search(
            self.word_search, self.word_end, stopindex=tkinter.END)

        # Set the start of the current word to be the start of the next occurrence
        word_start = next_word_start

        # Set the end of the current word to be the end of the next occurrence
        self.word_end = f"{word_start}+{len(self.word_search)}c"

        if word == self.word_search:
            # Apply the 'correct' tag to the found word
            self.box_text.tag_remove('gray', word_start, self.word_end)
            self.box_text.tag_add('correct', word_start, self.word_end)
            self.correct_words += 1
        else:
            # Apply the 'incorrect' tag to the incorrect word
            self.update_mistakes()
            self.box_text.tag_remove('gray', word_start, self.word_end)
            self.box_text.tag_add('incorrect', word_start, self.word_end)

        self.update_wm()

        if len(self.text) == 0:
            # If all words have been found, reset the game
            self.text_to_play()
            self.box_text.delete('1.0', 'end')
            self.word_end = '1.0'
            self.box_text.insert(tkinter.END, self.text)
        else:
            # Increment the word count and continue the game
            self.word_count += 1

    def text_to_play(self):
        # Define the URL to get a random paragraph
        url = 'https://randomword.com/paragraph'
        try:
            # Get the paragraph from the URL
            with requests.get(url) as response:
                # Raise an exception for HTTP errors
                response.raise_for_status()
                # Create a BeautifulSoup object to parse the HTML
                soup = BeautifulSoup(response.text, "html.parser")
                # Extract the paragraph text from the HTML
                paragraph = soup.find(
                    id="random_word_definition").text.replace('\"', '')
                # Split the paragraph into individual words
                self.text = paragraph.split()
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
            # Handle any errors that occur during the request
            print(f"Error: {e}")

    def bar(self):
        # Create a label to display the time elapsed
        self.lab_time = Label(text=f"Time: {self.time_value}",
                              font=(FONT_NAME, 25), bg=BACKGROUND)
        self.lab_time.grid(row=0, column=0, pady=5, padx=(0, 1000))

        # Create a label to display the number of mistakes
        self.lab_mistakes = Label(text=f"Mistakes: {self.mistakes_value}",
                                  font=(FONT_NAME, 25), bg=BACKGROUND)
        self.lab_mistakes.grid(row=0, column=0, pady=5, padx=(1000, 0))

        # Create a label to display the words per minute (WPM) rate
        self.lab_wm = Label(text=f"W/M: {self.wm_value}",
                            font=(FONT_NAME, 25), bg=BACKGROUND)
        self.lab_wm.grid(row=0, column=0, pady=5, padx=(0, 10))

    def update_time(self, value):
        # If there is still time remaining, update the timer
        if self.time_value < 60:
            self.time_value = value + 1
            self.lab_time.config(text=f"Time: {self.time_value}")
            # Call the update_time method again after one second
            self.window.after(1000, self.update_time, self.time_value)
        else:
            # If time is up, save the score and display the results
            self.save_score()
            self.show_popup()
        if self.start_time is None:
            # If this is the first time update_time has been called, set the start_time
            self.start_time = time.monotonic()

    def start_timer(self):
        # Start the timer by calling update_time with an initial value of -1
        self.update_time(-1)

    def update_mistakes(self):
        # Increment the mistakes_value and update the label
        self.mistakes_value += 1
        self.lab_mistakes.config(text=f"Mistakes: {self.mistakes_value}")

    def update_wm(self):
        # Calculate the words per minute (WPM) rate based on the elapsed time and correct_words
        elapsed_time = time.monotonic() - self.start_time
        self.wm_value = int(self.correct_words / elapsed_time * 60)
        self.lab_wm.config(text=f"WPM: {self.wm_value}")

    def show_popup(self):
        try:
            accuracy = int((self.word_count - self.mistakes_value) /
                           self.word_count * 100)
        except ZeroDivisionError:
            accuracy = "0"
        finally:
            message = f"WPM: {self.wm_value}\nAccuracy: {accuracy}%\nMax WPM : {self.highest_wp}"
            messagebox.showinfo("Results", message)
            self.restart()

    def restart(self):
        self.window.destroy()
        with open("wpm.txt") as data:
            high_score = int(data.read())
        Screen(high_score)

    def save_score(self):
        """Saves the highest score into wpm.txt."""
        if self.wm_value > self.highest_wp:
            self.highest_wp = self.wm_value
            with open("wpm.txt", mode="w") as data:
                data.write(f"{self.highest_wp}")

    def show_info(self):
        """Shows instruction to the application. When closed shows starting screen again."""
        self.title_label.config(text="Welcome in the Typing Speed Test!")
        info_text = Label(font=(FONT_NAME, 15), bg="#000000", fg="#fafafa", anchor='w', justify="left",
                          text="At the start of the application, the user must press the 'Start' button to launch the game.\n"
                          "A timer starts to display in the top left corner of the screen. The paragraph to type appears below.\n"
                          "The user must type each word in the text box below the paragraph and \n"
                          "press the space bar to move to the next word. If the user types the word correctly \n"
                          "it will be highlighted in green, otherwise, it will be highlighted in red.\n"
                          "If the user makes a mistake typing a word, the number of mistakes increases and the incorrect word is highlighted in red. \n"
                          "The total number of words typed as well as the words per minute (WPM) rate are also displayed.\n"
                          "Once the user has typed all the words in the paragraph, a new paragraph is generated, and the game continues until the user presses\n"
                          "the 'Restart' button to start the game over from the beginning.\n"
                          "LEGEND: WPM - Words Per Minute.\n")
        info_text.grid(column=0, row=1, pady=20)
        good_luck = Label(font=(FONT_NAME, 18, "bold"), bg="#000000", fg="#fafafa",
                          text="GOOD LUCK!")
        good_luck.grid(column=0, row=2, pady=20, padx=15)
        back = Button(text="GO BACK", font=(FONT_NAME, 15, "bold"), bg="#146C94", fg="#fafafa",
                      command=lambda: [
            info_text.destroy(), back.destroy(), good_luck.destroy(), good_luck.destroy(), self.title_label.destroy(), self.menu()])
        back.grid(column=0, row=3)
