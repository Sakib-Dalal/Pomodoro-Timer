import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
# colors link: https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Title.config(text="Timer")
    global reps
    reps = 0
    check_mark["text"] = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    global reps
    reps += 1
    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_second)
        Title["text"] = "Long Break"
        Title["fg"] = RED
    elif reps % 2 == 0:
        count_down(short_break_second)
        Title["text"] = "Short Break"
        Title["fg"] = PINK
    else:
        count_down(work_second)
        Title["text"] = "Work"
        Title["fg"] = GREEN



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_mark["text"] = marks

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


Title = tkinter.Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
Title.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightbackground=YELLOW)
tomato_png = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_png)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)


# Start
start_button = tkinter.Button(text="Start", font=(FONT_NAME, 16, "bold"), bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Reset
reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 16, "bold"), bg=YELLOW, fg=RED, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check mark
check_mark = tkinter.Label(bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()