import random

class Help:
    def __init__(self) -> None:
        # frame colour
        self.frame_colour = "light blue"
        # title text
        self.title_text_font = "Calibri"
        self.title_size = 30
        self.title_colour = "white"
        # default button state
        self.button_colour = "grey"
        self.button_text_font = "Arial"
        self.button_text_size = 20
        self.button_text_colour = "black"
        # inactive button state
        self.button_colour_inactive = "black"
        self.button_text_colour_inactive = "red"
        # clicked button
        self.button_colour_clicked = "red"
        self.button_text_colour_clicked = "black"
        # start button
        self.start_button_colour = "green"
        self.start_button_text_colour = "black"
        
        # variables for the game itself
        self.players = ["X", "O"]
        self.player = random.choice(self.players)
        self.board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.board4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]