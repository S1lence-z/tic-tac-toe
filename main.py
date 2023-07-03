import tkinter as tk
from tkinter import messagebox
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard
from appWindow import AppWindow

class TicTacToeGame:
    def __init__(self):
        # necessary classes
        self.h = Help()
        self.window = AppWindow(self.h)
        self.mainMenu = MainMenu(self.window, self.h, self)
        self.mainMenu.show()
        self.gameBoard = GameBoard(self.window, self.h, self)
        # game variables
        self.chosen_board_size = ""
        self.chosen_game_mode = ""
    
    def change_gameBoard_size(self, size: str) -> None:
        self.chosen_board_size = size
    
    def change_game_mode(self, mode: str) -> None:
        self.chosen_game_mode = mode
        
    def start_game(self) -> None:
        if (self.chosen_game_mode == ""):
            messagebox.showwarning("Warning!", "You have to choose the game mode!")
            return
        if (self.chosen_board_size == ""):
            messagebox.showwarning("Warning!", "You have to choose the game board size!")
            return
        self.mainMenu.hide()
        self.gameBoard.show(self.chosen_board_size)
        return
    
    def end_screen(self) -> None:
        self.gameBoard.hide()
        self.mainMenu.show()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.window.mainloop()