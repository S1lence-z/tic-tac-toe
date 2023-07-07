import random

class Help:
    """
    Helper class for managing game settings and messages.
    """
    def __init__(self) -> None:
        """
        Initializes the Help object with default settings and game variables.
        """
        # frame colour
        self.frame_colour = "light blue"
        
        # title text
        self.title_text_font = "Calibri"
        self.title_size = 30
        self.title_colour = "white"
        
        # default button state
        self.button_colour = "grey"
        self.button_text_font = "Arial"
        self.button_text_size = 30
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
        self.player_symbols = ["X", "O"]
        self.player1 = random.choice(self.player_symbols)
        self.player2 = self.set_second_player(self.player1)
        self.winning_player = ""
        self.board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.board4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        
        # end screen messages (presets)
        self.game_tie_message = "It is a tie!"
        self.player_won_message = ""
        
    def set_second_player(self, first_player) -> str:
        """
        Sets the second player based on the first player.

        Args:
            first_player (str): The symbol of the first player.

        Returns:
            str: The symbol of the second player.
        """
        if (first_player == self.player_symbols[0]):
            return self.player_symbols[1]
        else:
            return self.player_symbols[0]

    def set_winning_player(self, player_symbol) -> None:
        """
        Updates the final player who won the game.

        Args:
            player_symbol (str): The symbol of the player who won the game.
        """
        self.winning_player = player_symbol
        self.player_won_message = f"Player {self.winning_player} has won!"