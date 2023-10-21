from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
loops = 0
timer_stop = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer_stop)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    global loops
    loops = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global loops
    loops += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if loops == 1 or loops == 3 or loops == 5 or loops == 7:
        count_down(work_min)
        timer.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    elif loops == 2 or loops == 4 or loops == 6:
        count_down(short_break_min)
        timer.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 30, "bold"))
    elif loops == 8:
        count_down(long_break_min)
        timer.config(text="Long Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 30, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_stop
        timer_stop = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_mark = ""
        for _ in range(math.floor(loops/2)):
            check_mark += "✔"
        tick.config(text=check_mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

tick = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
tick.grid(column=1, row=3)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
