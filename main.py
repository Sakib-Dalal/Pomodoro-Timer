import tkinter
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightbackground=YELLOW)
tomato_png = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_png)
canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill=GREEN)
canvas.pack(expand=1)

window.mainloop()