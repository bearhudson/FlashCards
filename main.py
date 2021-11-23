import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel

WHITE = "#ffffff"
GREEN = "#91c2af"
FONT_NAME = "Ariel"


class FlashCards:

    def __init__(self):
        self.bg_image = PhotoImage(file="images/card_front.png")
        canvas.create_image(400, 263, image=self.bg_image)
        canvas.grid(row=0, column=0, columnspan=2)
        canvas.create_text(400, 236, text="title", font=(FONT_NAME, 50, 'bold'))
        canvas.create_text(400, 336, text="meaning", font=(FONT_NAME, 40, 'italic'))
        self.wrong_button_img = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0)
        self.wrong_button.grid(row=1, column=0)
        self.right_button_img = PhotoImage(file="images/right.png")
        self.right_button = Button(image=self.right_button_img, highlightthickness=0)
        self.right_button.grid(row=1, column=1)

    def flip_card(self):
        self.bg_image = PhotoImage(file="images/card_back.png")
        canvas.create_image(400, 263, image=self.bg_image)


window = Tk()
window.title("Flash Cards")
window.config(padx=120, pady=100, bg=GREEN)
canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
flash_cards = FlashCards()
tkinter.messagebox.showinfo("Notice", "This doesn't actually work yet.")
window.mainloop()
