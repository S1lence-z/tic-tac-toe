import tkinter as tk
from help import Help

class AppWindow(tk.Tk):
    """
    Represents the main application window for the TicTacToe game.
    
    Attributes:
        h (Help): An instance of the Help class that provides configuration settings.
    """
    
    def __init__(self, h: Help) -> None:
        """
        Initializes the AppWindow instance.
        
        Args:
            h (Help): An instance of the Help class that provides configuration settings.
        """
        super().__init__()
        # main tkinter window settings
        self.minsize(600, 600)
        self.maxsize(600, 600)
        self.title("TicTacToe Game")
        self.configure(bg=h.frame_colour)