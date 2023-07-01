import tkinter as tk
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard

if __name__ == "__main__":
    h = Help()
    window = tk.Tk()
    window.minsize(600, 600)
    window.maxsize(600, 600)
    window.title("TicTacToe Game")
    window.configure(bg=h.frame_colour)
    gui = MainMenu(window, Help())
    # gui = GameBoard(window, Help())
    window.mainloop()