import tkinter as tk
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard

class TicTacToeGame:
    # necessary classes and variables
    h = Help()
    chosen_board_size = "3"
    chosen_game_mode = "PvP"
    # main tkinter window settings
    window = tk.Tk()
    window.minsize(600, 600)
    window.maxsize(600, 600)
    window.title("TicTacToe Game")
    window.configure(bg=h.frame_colour)
    # possible game states
    possible_game_states = {
        "mainMenu",
        "inGame",
        "endGame"
    }
    current_game_state = "mainMenu"
    
    def gameLoop(self) -> None:
        match self.current_game_state:
            case "mainMenu":
                MainMenu(self.window, self.h)
            case "inGame":
                GameBoard(self.window, self.h)
            case "endGame":
                print("Not implemented yet")
        
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.gameLoop()