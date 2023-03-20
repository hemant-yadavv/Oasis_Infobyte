import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, master, duration):
        self.master = master
        self.duration = duration
        self.remaining = duration
        self.paused = False
        self.create_widgets()

    def create_widgets(self):
        self.timer_label = tk.Label(self.master, text="")
        self.timer_label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def start_timer(self):
        self.paused = False
        self.countdown()

    def pause_timer(self):
        self.paused = True

    def reset_timer(self):
        self.paused = True
        self.remaining = self.duration
        self.update_label()

    def countdown(self):
        if not self.paused and self.remaining >= 0:
            mins, secs = divmod(self.remaining, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_label.config(text=timer)
            self.remaining -= 1
            self.master.after(1000, self.countdown)

    def update_label(self):
        mins, secs = divmod(self.remaining, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        self.timer_label.config(text=timer)

# create GUI window
root = tk.Tk()
root.title("Countdown Timer")

# initialize timer duration
duration = int(input("Enter the time in seconds: "))

# create countdown timer object
countdown_timer = CountdownTimer(root, duration)

# start GUI event loop
root.mainloop()
