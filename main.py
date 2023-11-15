from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#8BC79A"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_function():
    global reps, check, timer
    reps = 0
    check = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_function():
    global reps
    reps += 1

    window.lift()

    work_sec = WORK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60

    if reps % 2 == 0:
        countdown(s_break_sec)
        title_label.config(text="Break", fg=GREEN)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global check

    count_min = math.floor(count / 60)
    count_sec = str(count % 60)
    if len(count_sec) < 2:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        window.attributes('-topmost', 0)
        start_function()
        if reps % 2 == 0:
            playsound(r"C:\Users\stepa\OneDrive\Dokumenty\Coding\Python\Udemy\day_28 Pomodoro\retro.wav")
            window.attributes('-topmost', 1)
            check = check + "✔"
            n_runs.config(text=check)
        else:
            playsound(r"C:\Users\stepa\OneDrive\Dokumenty\Coding\Python\Udemy\day_28 Pomodoro\start.wav")
            pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_function)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_function)
reset_button.grid(row=2, column=2)

n_runs = Label(bg=YELLOW, fg=GREEN)
n_runs.grid(row=3, column=1)

window.mainloop()

