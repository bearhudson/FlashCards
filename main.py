import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel

WHITE = "#ffffff"
GREEN = "#91c2af"
FONT_NAME = "Courier"


class FlashCards:

    def __init__(self, tk_root):
        self.bg_image = PhotoImage(file="images/card_front.png")
        canvas.create_image(400, 263, image=self.bg_image)
        canvas.grid(row=1, column=1)
        self.title = Label(text='Flash Cards', bg=WHITE, font=(FONT_NAME, 34, 'italic'))
        self.title.grid(row=1, column=1)
        self.word = Label(text='Word', bg=WHITE, font=(FONT_NAME, 24, 'bold'))
        self.word.grid(row=2, column=1)
        self.wrong_button_img = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0)
        self.wrong_button.grid(row=3, column=0)
        self.right_button_img = PhotoImage(file="images/right.png")
        self.right_button = Button(image=self.right_button_img, highlightthickness=0)
        self.right_button.grid(row=3, column=2)

    def flip_card(self):
        self.bg_image = PhotoImage(file="images/card_back.png")
        canvas.create_image(400, 263, image=self.bg_image)
        canvas.grid(row=1, column=1)


window = Tk()
window.title("Flash Cards")
window.config(padx=120, pady=100, bg=GREEN)
canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
flash_cards = FlashCards(window)
tkinter.messagebox.showinfo("Notice", "This doesn't actually work yet.")
window.mainloop()
