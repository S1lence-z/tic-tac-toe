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
        self.current_game_state = "mainMenu"
        # all_possible_game_states = { mainMenu, inGame, endGame }

    def gameLoop(self) -> None:
        if self.current_game_state == "mainMenu":
            menu = MainMenu(self.window, self.h)
            if menu.start_game_status:
                self.current_game_state = "inGame"
                self.window.quit()
        
        elif self.current_game_state == "inGame":
            game = GameBoard(self.window, self.h)
        
        elif self.current_game_state == "endGame":
            print("Not implemented yet")
            
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.gameLoop()