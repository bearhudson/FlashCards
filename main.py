import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel
import pandas
import random


WHITE = "#ffffff"
BLACK = "#000000"
GREEN = "#B1DDC6"
FONT_NAME = "Ariel"


class FlashCards:

    def __init__(self):
        self.csv_file_data = {}
        self.csv_dictionary = {}
        self.french_word = ""
        self.english_word = ""
        self.csv_file_data = pandas.read_csv('data/french_words.csv')
        self.csv_dictionary = {row.French: row.English for (index, row) in self.csv_file_data.iterrows()}
        self.bg_card_front = PhotoImage(file="images/card_front.png")
        self.bg_card_back = PhotoImage(file="images/card_back.png")
        self.bg_card = canvas.create_image(400, 263, image=self.bg_card_front)
        canvas.grid(row=0, column=0, columnspan=2)
        self.title_word = canvas.create_text(400, 236, text="title", font=(FONT_NAME, 50, 'bold'))
        self.meaning_word = canvas.create_text(400, 336, text="meaning", fill=WHITE, font=(FONT_NAME, 40, 'italic'))
        self.load_cards()
        self.wrong_button_img = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0, command=self.wrong_card)
        self.wrong_button.grid(row=1, column=0)
        self.right_button_img = PhotoImage(file="images/right.png")
        self.right_button = Button(image=self.right_button_img, highlightthickness=0, command=self.right_card)
        self.right_button.grid(row=1, column=1)

    def load_cards(self):
        canvas.itemconfigure(self.bg_card, image=self.bg_card_front)
        self.french_word, self.english_word = random.choice(list(self.csv_dictionary.items()))
        canvas.itemconfigure(self.title_word, text=self.french_word, fill=BLACK)
        canvas.itemconfigure(self.meaning_word, text="meaning")

    def flip_card(self):
        canvas.itemconfigure(self.bg_card, image=self.bg_card_back)
        canvas.itemconfigure(self.title_word, fill=WHITE)
        canvas.itemconfigure(self.meaning_word, text=self.english_word)

    def right_card(self):
        self.next_card()

    def wrong_card(self):
        self.flip_card()

    def next_card(self):
        self.load_cards()


window = Tk()
window.title("Flash Cards")
window.config(padx=120, pady=100, bg=GREEN)
canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
flash_cards = FlashCards()
window.mainloop()
