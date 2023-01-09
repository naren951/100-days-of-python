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
stop = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(stop)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    tick.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        timer_text.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        timer_text.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        timer_text.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    sec = count%60
    if sec<10:
        sec = f"0{sec}"
    time = f"{math.floor(count/60)}:{sec}"
    canvas.itemconfig(timer, text=time)
    if count > 0:
        global stop
        stop = window.after(1000, count_down, count-1)
    else:
        start_timer()
        tick.config(text="✔"*math.floor(reps/2))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_text = Label(text="Timer", font=(FONT_NAME, 60, "bold",), fg=GREEN,bg=YELLOW)
timer_text.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(row=2,column=0)
reset_btn = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(row=2,column=2)

tick = Label(text="",fg=GREEN, bg=YELLOW)
tick.grid(row=3,column=1)

window.mainloop()