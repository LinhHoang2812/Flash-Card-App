BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

random_word = {}

data = {}


#--------------------- CREATE NEW FLASHCARD------------------#

try:
    german_df = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:

    german_df = pandas.read_csv("data/german_words.csv")
    data = german_df.to_dict(orient="records")
else:

    data = german_df.to_dict(orient="records")

def create_card():

    global random_word, data, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data)
    canvas.itemconfig(image,image=card_front)
    canvas.itemconfig(title,text="German",fill="black")
    canvas.itemconfig(word,text=random_word["German"],fill="black")
    flip_timer = window.after(3000,func =flip_card)

def update_card():
    global random_word, data
    data.remove(random_word)
    df = pandas.DataFrame(data)
    df.to_csv("data/words_to_learn.csv",index=FALSE)
    create_card()




def flip_card():
    global random_word
    canvas.itemconfig(image,image=card_back)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=random_word["English"],fill="white")



#---------------------UI SET UP -----------------------#

window = Tk()
window.title("Fashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func =flip_card)

card_back= PhotoImage(file="images/card_back.png")
card_front= PhotoImage(file="images/card_front.png")
canvas= Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
image = canvas.create_image(400,263,image=card_front)
title= canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word= canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
create_card()


right_image= PhotoImage(file="images/right.png")
right_button= Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=update_card)
right_button.grid(column=1,row=1)

wrong_image= PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=create_card)
wrong_button.grid(column=0,row=1)












window.mainloop()








