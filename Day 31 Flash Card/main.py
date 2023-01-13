BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
ANSWER_FONT = ("Ariel", 60, "bold")
from tkinter import *
import pandas as pd
import random

try:
    french_words = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pd.read_csv("./data/french_words.csv")
finally:
    french_words = french_words.to_dict("record")

current_card = None


def is_known():
    french_words.remove(current_card)
    data = pd.DataFrame.from_dict(french_words)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_words)
    word = current_card["French"]
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(answer, text=f"{word}", fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    word = current_card["English"]
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(answer, text=f"{word}", fill="white")


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="test", font=LANG_FONT, fill="black")
answer = canvas.create_text(400, 263, text="test", font=ANSWER_FONT, fill="black")

canvas.grid(row=0, column=0, columnspan=2)


right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

right_btn = Button(
    image=right, highlightthickness=0, height=100, width=100, command=is_known
)
right_btn.grid(row=1, column=1)

wrong_btn = Button(
    image=wrong, highlightthickness=0, height=100, width=100, command=next_card
)
wrong_btn.grid(row=1, column=0)


next_card()
window.mainloop()
