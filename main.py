import tkinter as tk
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard

if __name__ == "__main__":
    h = Help()
    window = tk.Tk()
    window.minsize(600, 600)
    window.maxsize(600, 600)
    window.title("Tic-Tac-Toe Game")
    window.configure(bg=h.frame_colour)
    gui = MainMenu(window)
    # gui = GameBoard(window)
    window.mainloop()