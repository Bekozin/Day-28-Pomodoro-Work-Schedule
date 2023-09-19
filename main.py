import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timing():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)

    elif reps % 2 == 0:
        countdown(short_break_sec)

    else:
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Work Schedule")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timing)
start_button.grid(column=0, row=2)

reser_button = Button(text="Reset", highlightthickness=0)
reser_button.grid(column=2, row=2)

check_marks = Label(text=" ✔ ", bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
