import tkinter as tk
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard
from appWindow import AppWindow

class TicTacToeGame:
    def __init__(self):
        # necessary classes and variables
        self.h = Help()
        self.window = AppWindow(self.h)
        self.chosen_board_size = "3"
        self.chosen_game_mode = "PvP"
        # possible game states
        # all_possible_game_states = { mainMenu, inGame, endGame }
        self.current_game_state = "mainMenu"
        self.start_game_status = False
        menu = MainMenu(self.window, self.h)
        game = GameBoard(self.window, self.h)

    def gameLoop(self) -> None:
        if self.current_game_state == "mainMenu":
            if (self.start_game_status):
                self.current_game_state = "inGame"
        
        elif self.current_game_state == "inGame":
            print("more")
        
        elif self.current_game_state == "endGame":
            print("Not implemented yet")
            
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.gameLoop()