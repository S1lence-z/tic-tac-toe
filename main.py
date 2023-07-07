import tkinter as tk
from tkinter import messagebox
from help import Help
from mainMenu import MainMenu
from gameBoard import GameBoard
from endScreen import EndScreen
from appWindow import AppWindow

class TicTacToeGame:
    """
    A class representing the Tic Tac Toe game.

    Attributes:
        h (Help): An instance of the Help class.
        window (AppWindow): An instance of the AppWindow class.
        mainMenu (MainMenu): An instance of the MainMenu class.
        gameBoard (GameBoard): An instance of the GameBoard class.
        endScreen (EndScreen): An instance of the EndScreen class.
        chosen_board_size (str): The chosen size of the game board.
        chosen_game_mode (str): The chosen game mode.

    Methods:
        __init__(): Initializes the TicTacToeGame class.
        change_gameBoard_size(size: str) -> None: Changes the game board size.
        change_game_mode(mode: str) -> None: Changes the game mode.
        start_game() -> None: Starts the game.
        end_screen(label_text) -> None: Displays the end screen.
        restart_with_same_settings() -> None: Restarts the game with the same settings.
        exit_to_menu() -> None: Exits to the main menu.
    """

    def __init__(self):
        """
        Initializes the TicTacToeGame class.

        Creates instances of necessary classes and sets initial game variables.
        """
        self.h = Help()
        self.window = AppWindow(self.h)
        self.mainMenu = MainMenu(self.window, self.h, self)
        self.gameBoard = GameBoard(self.window, self.h, self)
        self.endScreen = EndScreen(self.window, self.h, self)
        self.mainMenu.show()
        self.gameBoard.hide()
        self.endScreen.hide()
        self.chosen_board_size = ""
        self.chosen_game_mode = ""

    def change_gameBoard_size(self, size: str) -> None:
        """
        Changes the game board size.

        Args:
            size (str): The new size of the game board.
        """
        self.chosen_board_size = size

    def change_game_mode(self, mode: str) -> None:
        """
        Changes the game mode and sets the current mode in the help class.

        Args:
            mode (str): The new game mode.
        """
        self.chosen_game_mode = mode
        self.h.set_game_mode(self.chosen_game_mode)

    def start_game(self) -> None:
        """
        Starts the game.

        Displays the game board with the chosen board size.
        Shows warning messages if game mode or board size is not chosen.
        """
        if (self.chosen_game_mode == ""):
            messagebox.showwarning("Warning!", "You have to choose the game mode!")
            return
        if (self.chosen_board_size == ""):
            messagebox.showwarning("Warning!", "You have to choose the game board size!")
            return
        self.endScreen.hide()
        self.mainMenu.hide()
        self.gameBoard.show(self.chosen_board_size)

    def end_screen(self, label_text) -> None:
        """
        Displays the end screen.

        Args:
            label_text: The text to be displayed on the end screen.
        """
        self.gameBoard.hide()
        self.mainMenu.hide()
        self.endScreen.show(label_text)

    def restart_with_same_settings(self) -> None:
        """
        Restarts the game with the same settings.

        Hides previous instances, creates new instances, and resets chosen variables.
        """
        self.gameBoard.destroy_widgets()
        self.endScreen.destroy_widgets()
        self.gameBoard = GameBoard(self.window, self.h, self)
        self.endScreen = EndScreen(self.window, self.h, self)
        self.start_game()

    def exit_to_menu(self) -> None:
        """
        Exits to the main menu.

        Hides previous instances, creates new instances, and resets chosen variables.
        """
        self.mainMenu.destroy_widgets()
        self.gameBoard.destroy_widgets()
        self.endScreen.destroy_widgets()
        self.mainMenu = MainMenu(self.window, self.h, self)
        self.gameBoard = GameBoard(self.window, self.h, self)
        self.endScreen = EndScreen(self.window, self.h, self)
        self.mainMenu.show()
        self.gameBoard.hide()
        self.endScreen.hide()
        self.chosen_board_size = ""
        self.chosen_game_mode = ""

if __name__ == "__main__":
    game = TicTacToeGame()
    game.window.mainloop()