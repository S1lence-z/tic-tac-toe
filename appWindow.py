import tkinter as tk
from help import Help

class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        h = Help()
        # main tkinter window settings
        self.minsize(600, 600)
        self.maxsize(600, 600)
        self.title("TicTacToe Game")
        self.configure(bg=h.frame_colour)