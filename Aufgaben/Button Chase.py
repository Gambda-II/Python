import tkinter as tk
import random as random

score = 0
colors = ["red", "green", "yellow", "blue"]

def on_button_click():
    move_button_randomly()
    global score
    score = add_to_score(score, 10)

    label.config(text=score)
    random_index = random.randint(0,3)
    color = colors[random_index]
    button.config(bg=color)


def move_button_randomly():
    minValueCoordinates = 0.1
    maxValueCoordinates = 0.9

    posX = random.random() * (maxValueCoordinates - minValueCoordinates) + minValueCoordinates
    posY = random.random() * (maxValueCoordinates - minValueCoordinates) + minValueCoordinates

    button.place(relx=posX, rely=posY, anchor="center")

def add_to_score(score, value):
    score = score + value
    return score

root = tk.Tk()
root.geometry("600x600")
root.config(bg="black")

button = tk.Button(root, text="HEHE", command=on_button_click)
button_width = 60
button_height = 60
button.place(width=button_width, height=button_height, anchor="center", relx=0.5, rely=0.5)

label = tk.Label(root, text=score)
label.pack(pady=10)

root.mainloop()