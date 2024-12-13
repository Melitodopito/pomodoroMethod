from tkinter import Tk
from UI import PomodoroUI

# Criação Main window
window = Tk()
window.title("My Tomato Method")
window.minsize(400, 400)
window.maxsize(800, 600)
window.config(pady=50, padx=100, bg="#f7f5dd")


My_Pomodoro = PomodoroUI(window)
window.mainloop()

