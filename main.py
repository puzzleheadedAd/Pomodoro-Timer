from tkinter import *
# CONSTANTS ##############
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 60, "bold")
FONT_TOP_LABEL = ("Courier", 50, "bold")
FONT_BUTTONS = ("Courier", 18, "bold")
FONT_CHECKMARK = ("Courier", 24, "bold")
WORK_MIN = 25
WORK_S = WORK_MIN*60
SHORT_BREAK_MIN = 5
SHORT_BREAK_S = SHORT_BREAK_MIN*60
LONG_BREAK_MIN = 30
LONG_BREAK_S = LONG_BREAK_MIN*60
reps_in = 0
chosen_timer = ""
countdown_mechanic = None
###############
# Reset timer
def reset_timer():
    global countdown_mechanic
    global reps_in
    label_checkmarks.config(text="")
    label_pomodoro_timer.config(text="Pomodoro timer")
    window.after_cancel(countdown_mechanic)
    canvas.itemconfig(timer_text, text="25:00")
    reps_in = 0

# Timer mechanism
def start_timer():
    global reps_in
    global chosen_timer
    reps_in += 1
    if reps_in % 8 == 0:
        chosen_timer = LONG_BREAK_S
        label_pomodoro_timer.config(text="Nap time!", fg=RED)
    elif reps_in % 2 != 0:
        chosen_timer = WORK_S
        label_pomodoro_timer.config(text="Time to work!", fg=GREEN)
    elif reps_in % 2 == 0:
        chosen_timer = SHORT_BREAK_S
        label_pomodoro_timer.config(text="Get some rest", fg=PINK)
    take_away_one_s(chosen_timer)

# Countdown mechanics
def take_away_one_s(amount_of_time):
    global countdown_mechanic
    remaining_minutes = amount_of_time // 60
    remaining_seconds = amount_of_time % 60
    formatted_time = f"{remaining_minutes:02d}:{remaining_seconds:02d}"
    canvas.itemconfig(timer_text, text=formatted_time)
    if amount_of_time > 0:
        countdown_mechanic = window.after(1000, take_away_one_s, amount_of_time - 1)
    elif amount_of_time == 0:
        start_timer()
        if reps_in % 2 == 0:
            reps_in_half = int(reps_in / 2)
            label_checkmarks.config(text="✔"*reps_in_half)


# User Interface Setup
# # # window # # #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=50, pady=25, bg=YELLOW)


# # # window # # #
canvas = Canvas(width=624, height=650, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(312, 325, image=tomato_image)
timer_text = canvas.create_text(312, 350, text="00:00", font=FONT, fill="white")
canvas.grid(column=1, row=1)

label_pomodoro_timer = Label(text="Pomodoro timer", fg=GREEN, bg=YELLOW, font=FONT_TOP_LABEL)
label_pomodoro_timer.grid(column=1, row=0)


button_start = Button(text="Start", font=FONT_BUTTONS, bg=GREEN, command=start_timer)
button_start.grid(column=0, row=2, sticky="E")

button_reset = Button(text="Reset", font=FONT_BUTTONS, bg=PINK, command=reset_timer)
button_reset.grid(column=2, row=2, sticky="W")

label_checkmarks = Label(text="", font=FONT_CHECKMARK, bg=YELLOW, fg=GREEN)
label_checkmarks.grid(column=1, row=3)



window.mainloop()
