import tkinter as tk
from tkinter import messagebox
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard
from endScreen import EndScreen
from appWindow import AppWindow

class TicTacToeGame:
    def __init__(self):
        # necessary classes
        self.h = Help()
        self.window = AppWindow(self.h)
        self.mainMenu = MainMenu(self.window, self.h, self)
        self.gameBoard = GameBoard(self.window, self.h, self)
        self.endScreen = EndScreen(self.window, self.h, self)
        self.mainMenu.show()
        self.gameBoard.hide()
        self.endScreen.hide()
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
        self.endScreen.hide()
        self.mainMenu.hide()
        self.gameBoard.show(self.chosen_board_size)
        return
    
    def end_screen(self, label_text) -> None:
        self.gameBoard.hide()
        self.mainMenu.hide()
        self.endScreen.show(label_text)
        
    def restart_with_same_settings(self) -> None:
        # hide previous instances
        self.gameBoard.destroy_widgets()
        self.endScreen.destroy_widgets()
        # create new instances and reset chosen variables
        self.gameBoard = GameBoard(self.window, self.h, self)
        self.endScreen = EndScreen(self.window, self.h, self)
        # default show settings
        self.start_game()
        
    def exit_to_menu(self) -> None:
        # hide previous instances
        self.mainMenu.destroy_widgets()
        self.gameBoard.destroy_widgets()
        self.endScreen.destroy_widgets()
        # create new instances and reset chosen variables
        self.mainMenu = MainMenu(self.window, self.h, self)
        self.gameBoard = GameBoard(self.window, self.h, self)
        self.endScreen = EndScreen(self.window, self.h, self)
        # default show settings
        self.mainMenu.show()
        self.gameBoard.hide()
        self.endScreen.hide()
        self.chosen_board_size = ""
        self.chosen_game_mode = ""

if __name__ == "__main__":
    game = TicTacToeGame()
    game.window.mainloop()