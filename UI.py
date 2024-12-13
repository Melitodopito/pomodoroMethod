from tkinter import *
from timer import PomodoroTimer
from abc import ABC, abstractmethod


class UI_Template(ABC):
    def __init__(self, window):
        self.window = window
        self.PINK = "#e2979c"
        self.RED = "#e7305b"
        self.GREEN = "#9bdeac"
        self.YELLOW = "#f7f5dd"
        self.FONT_NAME = "Courier"
        self.my_timer = PomodoroTimer(self)
        self.create_ui()

    @abstractmethod
    def create_ui(self):
        pass

    @abstractmethod
    def change_durations(self):
        pass

    @abstractmethod
    def close_window(self, secondary_window):
        pass


class PomodoroUI(UI_Template):

    # Criação do UI em si
    def create_ui(self):
        # Canvas
        self.canvas = Canvas(width=400, height=350, bg=self.YELLOW, highlightthickness=0)
        self.tomato = PhotoImage(file="tomatoes.png")
        self.canvas.create_image(180, 150, image=self.tomato)
        self.timer_text = self.canvas.create_text((190, 150), text=f"{self.my_timer.WORK_MIN}:00", fill="white",
                                                  font=(self.FONT_NAME, 34, "bold"))
        self.canvas.grid(column=1, row=1)

        # Labels
        self.timer_label = Label(text="This is my Pomodoro Timer")
        self.timer_label.config(fg=self.GREEN, bg=self.YELLOW, font=(self.FONT_NAME, 20, "bold"))
        self.timer_label.grid(row=0, column=1)

        self.checkmark_label = Label()
        self.checkmark_label.grid(column=0, row=3)

        # Buttons
        self.start_button = Button(text="Start", command=self.my_timer.start_timer, width=5, height=2, borderwidth=4,
                                   activebackground="red", bg="white", font=(self.FONT_NAME, 18, "bold"))
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(text="Reset", command=self.my_timer.reset_timer, bg="white", width=5, height=2,
                                   borderwidth=4, activebackground="red", font=(self.FONT_NAME, 18, "bold"))
        self.reset_button.grid(column=2, row=2)

        self.pause_button = Button(text="Pause", command=self.my_timer.pause_countdown, bg="white", width=10, height=2,
                                   borderwidth=4, activebackground="red", font=(self.FONT_NAME, 18, "bold"))
        self.pause_button.grid(column=1, row=3)

        self.change_button = Button(text="Change focus or pause duration", command=self.change_durations, bg="white",
                                    width=30, height=2, borderwidth=4, activebackground="red",
                                    font=(self.FONT_NAME, 12, "bold"))
        self.change_button.grid(column=1, row=2, columnspan=1)

    def change_durations(self):
        self.window.attributes('-disabled', 1)
        # Criação nova janela
        durations_window = Tk()
        durations_window.title("Change Durations")
        durations_window.minsize(500, 300)
        durations_window.maxsize(900, 400)
        durations_window.config(pady=50, padx=100, bg="#f7f5dd")

        # Forms
        work_duration_form = Entry(durations_window)
        work_duration_form.config(width=40, bg="white")
        work_duration_form.grid(column=0, row=1)

        rest_duration_form = Entry(durations_window)
        rest_duration_form.config(width=40, bg="white")
        rest_duration_form.grid(column=1, row=1)

        long_rest_duration_form = Entry(durations_window)
        long_rest_duration_form.config(width=40, bg="white")
        long_rest_duration_form.grid(column=2, row=1)

        # Labels
        work_duration_label = Label(durations_window, text="Change work duration to: (min)")
        work_duration_label.config(bg="White")
        work_duration_label.grid(column=0, row=0)

        rest_duration_label = Label(durations_window, text="Change rest duration to: (min)")
        rest_duration_label.config(bg="White")
        rest_duration_label.grid(column=1, row=0)

        long_rest_duration_label = Label(durations_window, text="Change long rest duration to: (min)")
        long_rest_duration_label.config(bg="White")
        long_rest_duration_label.grid(column=2, row=0)

        # Buttons

        work_duration_button = Button(durations_window, command=lambda: self.my_timer.save_duration(work_duration_form,
                                                                                                    self.my_timer.WORK_MIN),
                                      text="Save Duration")
        work_duration_button.config(bg="White")
        work_duration_button.grid(column=0, row=2)

        rest_duration_button = Button(durations_window, command=lambda: self.my_timer.save_duration(rest_duration_form,
                                                                                                    self.my_timer.SHORT_BREAK_MIN),
                                      text="Save Duration")
        rest_duration_button.config(bg="White")
        rest_duration_button.grid(column=1, row=2)

        long_rest_duration_button = Button(durations_window,
                                           command=lambda: self.my_timer.save_duration(long_rest_duration_form,
                                                                                       self.my_timer.LONG_BREAK_MIN),
                                           text="Save Duration")
        long_rest_duration_button.config(bg="White")
        long_rest_duration_button.grid(column=2, row=2)

        close_window_button = Button(durations_window, command=lambda: self.close_window(durations_window),
                                     text="Back to Pomodoro App")
        close_window_button.config(bg="White")
        close_window_button.grid(column=1, row=3)

    def close_window(self, secondary_window):
        self.window.attributes('-disabled', 0)
        secondary_window.destroy()
