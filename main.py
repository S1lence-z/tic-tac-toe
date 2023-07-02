import tkinter as tk
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard

class TicTacToeGame:
    def __init__(self):
        # necessary classes and variables
        self.h = Help()
        self.chosen_board_size = "3"
        self.chosen_game_mode = "PvP"
        # main tkinter window settings
        self.window = tk.Tk()
        self.window.minsize(600, 600)
        self.window.maxsize(600, 600)
        self.window.title("TicTacToe Game")
        self.window.configure(bg=self.h.frame_colour)
        # possible game states
        self.current_game_state = "mainMenu"
        
    def start(self):
        self.gameLoop()
        self.window.mainloop()

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

if __name__ == "__main__":
    game = TicTacToeGame()
    while (True):
        game.start()
        print(game.current_game_state)