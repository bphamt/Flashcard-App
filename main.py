from tkinter import *
import pandas
import csv
import random

BACKGROUND_COLOR = "#B1DDC6"
FLIP = 0

# Convert CSV into List
try:
    french_word_csv = pandas.read_csv("./data/words_to_learn.csv")
except:
    french_word_csv = pandas.read_csv("./data/french_words.csv")

french_word_list = french_word_csv.values.tolist()

# Random NUM
RANDOM_NUM = random.randrange(len(french_word_list))

# Wrong, Save data to words_to_learn.csv
def wrong():
    global FLIP

    french_word_list.pop(RANDOM_NUM)

    with open("./data/words_to_learn.csv", "w", newline='', encoding='utf-8') as file:
        write = csv.writer(file)
        file.write("French,English\n")
        write.writerows(french_word_list)

    new_word()


# Flip card
def card_flip(event=None):
    global FLIP

    if FLIP != 0:
        bottom_label.config(fg="#FFFFFF", bg="#91c2af")
        top_label.config(fg="#FFFFFF", bg="#91c2af", text="English")
        flip_button.config(bg="#91c2af", activebackground="#91c2af")
        canvas.itemconfig(canvas_image, image=new_logo_img)
        bottom_label.config(text=f"{french_word_list[RANDOM_NUM][1]}")
        FLIP += 1
    else:
        bottom_label.config(fg="#000000", bg="#FFFFFF")
        top_label.config(fg="#000000", bg="#FFFFFF", text="French")
        flip_button.config(bg="#FFFFFF", activebackground="#FFFFFF")
        canvas.itemconfig(canvas_image, image=logo_img)
        bottom_label.config(text=f"{french_word_list[RANDOM_NUM][0]}")
        FLIP -= 1


# New word
def new_word():
    global RANDOM_NUM
    global FLIP, flip_timer

    FLIP = 0

    window.after_cancel(flip_timer)

    bottom_label.config(fg="#000000", bg="#FFFFFF")
    top_label.config(fg="#000000", bg="#FFFFFF", text="French")
    flip_button.config(bg="#FFFFFF")
    canvas.itemconfig(canvas_image, image=logo_img)
    RANDOM_NUM = random.randrange(len(french_word_list))

    bottom_label.config(text=f"{french_word_list[RANDOM_NUM][0]}")

    flip_timer = window.after(6000, func=card_flip)

    card_flip()

# Window UI


window = Tk()
window.title("Flashcard App")
window.minsize(width=800, height=580)
window.config(padx=40, bg=BACKGROUND_COLOR)
window.resizable(False, False)
window.bind("<space>", card_flip)

flip_timer = window.after(3000, func=card_flip)

# Card-Front IMG
canvas = Canvas(width=800, height=580, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="./images/card_front.png")
new_logo_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 300, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

# Top_text
top_label = Label(text="French", font=("Ariel", 40, "italic"), bg="#FFFFFF")
top_label.place(x=400, y=150, anchor="center")

# Bottom_text
bottom_label = Label(text=f"{french_word_list[RANDOM_NUM][0]}", font=("Ariel", 60, "bold"), bg="#FFFFFF")
bottom_label.place(x=400, y=280, anchor="center")

# X Button
x_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_image, command=wrong, highlightthickness=0, borderwidth=0)
x_button.grid(column=0, row=1)

# Y Button
y_image = PhotoImage(file="./images/right.png")
y_button = Button(image=y_image, command=new_word, highlightthickness=0, borderwidth=0)
y_button.grid(column=1, row=1, pady=25)

# Flip Button
flip_image = PhotoImage(file="./images/flip.png")
flip_button = Button(image=flip_image, command=card_flip, highlightthickness=0, borderwidth=0, bg="#FFFFFF",
                     activebackground="#FFFFFF")
flip_button.place(x=400, y=440, anchor="center")


window.mainloop()
