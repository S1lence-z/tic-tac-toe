import random

class Help:
    def __init__(self) -> None:
        # variable for tkinter design
        self.font1 = "Arial"
        self.font1_size = 12
        self.title_size = 20
        self.button_colour = "green"
        self.button_colour_clicked = "red"
        self.button_colour_inactive = "black"
        self.text_button_colour = "blue"
        self.frame_colour = "light blue"
        self.title_colour = "white"

        # variables for the game itself
        self.players = ["X", "O"]
        self.player = random.choice(self.players)
        self.board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.board4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]