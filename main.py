import tkinter as tk
from help import Help
from mainMenu import MainMenu
from gameBoard import TicTacToeBoard

if __name__ == "__main__":
    h = Help()
    window = tk.Tk()
    window.minsize(650, 650)
    window.maxsize(650, 650)
    window.title("Tic-Tac-Toe Game")
    window.configure(bg=h.frame_colour)
    # gui = MainMenu(window)
    gui = TicTacToeBoard(window)
    window.mainloop()