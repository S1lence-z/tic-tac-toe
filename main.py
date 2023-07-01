import tkinter as tk
from mainMenu import MainMenu
from gameBoard import TicTacToeBoard

if __name__ == "__main__":
    window = tk.Tk()
    window.minsize(500, 500)
    window.maxsize(500, 500)
    window.title("Tic-Tac-Toe Game")
    window.configure(bg="grey")
    # gui = MainMenu(window)
    gui = TicTacToeBoard(window)
    window.mainloop()