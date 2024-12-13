import tkinter
from math import floor
from tkinter import messagebox
from abc import ABC, abstractmethod

class Timer_Template(ABC):
    def __init__(self, ui):
        self.ui = ui
        self.REPS = 0
        self.my_timer = None
        self.WORK_MIN = 25
        self.SHORT_BREAK_MIN = 5
        self.LONG_BREAK_MIN = 20
        self.pause_pressed = False

    @abstractmethod
    def reset_timer(self):
        pass

    @abstractmethod
    def count_down(self, count):
        pass

    @abstractmethod
    def start_timer(self):
        pass

    @abstractmethod
    def pause_countdown(self):
        pass

    @abstractmethod
    def save_duration(self, form, global_var):
        pass

class PomodoroTimer(Timer_Template):

    # Reset do timer, função ligada ao botão reset
    def reset_timer(self):
        self.ui.start_button.config(state=tkinter.NORMAL)
        self.ui.window.after_cancel(self.my_timer)
        self.ui.timer_label.config(text="This is my Pomodoro Timer")
        self.ui.checkmark_label.config(text="")
        self.ui.canvas.itemconfig(self.ui.timer_text, text=f"{self.WORK_MIN}:00")
        self.REPS = 0

    # Função principal do contador
    def count_down(self, count):

        # Conversão de minutos e segundos
        count_min = floor(count / 60)
        count_sec = count % 60

        if count_sec == 0:
            count_sec = "00"
        elif count_sec < 10:
            count_sec = f"0{count_sec}"

        if count_min == 0:
            count_min = "00"
        elif count_min < 10:
            count_min = f"0{count_min}"

        if not self.pause_pressed:
            self.ui.canvas.itemconfig(self.ui.timer_text, text=f"{count_min}:{count_sec}")
            if count > 0:
                self.my_timer = self.ui.window.after(1000, self.count_down, count - 1)
            else:
                self.start_timer()
                mark = ""
                sessions = floor(self.REPS / 2)
                for rep in range(sessions):
                    mark += "🍅"
                self.ui.checkmark_label.config(text=mark)
        else:
            self.my_timer = self.ui.window.after(1000, self.count_down, count)

    # Modificar o texto de acordo com o pretendido
    def start_timer(self):
        self.ui.start_button.config(state=tkinter.DISABLED)
        if self.REPS % 2 == 0:
            self.ui.timer_label.config(text="STUDY MELO STUDY", fg=self.ui.GREEN)
            self.count_down(self.WORK_MIN * 60)
        elif self.REPS == 8:
            self.count_down(self.LONG_BREAK_MIN * 60)
            self.ui.timer_label.config(text="REST MELO REST", fg=self.ui.PINK)
        else:
            self.count_down(self.SHORT_BREAK_MIN * 60)
            self.ui.timer_label.config(text="REST MELO REST", fg=self.ui.PINK)
        self.REPS += 1

    def pause_countdown(self):
        if not self.pause_pressed:
            self.pause_pressed = True
            self.ui.pause_button.config(text="Unpause", bg="red")
        else:
            self.pause_pressed = False
            self.ui.pause_button.config(text="Pause", bg="white")

    def save_duration(self, form, global_var):
        new_duration = form.get()
        try:
            new_duration = int(new_duration)
            if global_var is self.WORK_MIN:
                self.WORK_MIN = new_duration
            elif global_var is self.SHORT_BREAK_MIN:
                self.SHORT_BREAK_MIN = new_duration
            elif global_var is self.LONG_BREAK_MIN:
                self.LONG_BREAK_MIN = new_duration
        except ValueError:
            # If not valid Integer
            messagebox.showerror(message="Invalid input. Please enter a valid integer")

