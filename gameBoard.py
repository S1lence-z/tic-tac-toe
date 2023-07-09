import tkinter as tk
from tkinter import messagebox
from help import Help
from minimaxAlg import minimax

class GameBoard:
    """
    Represents the game board of the TicTacToe game.
    
    Attributes:
        h (Help): An instance of the Help class that provides configuration settings.
        board: The tkinter root object.
        game_controller: The game controller object that controls the game flow.
        board_frame: The frame that holds the game board.
        player: The current player.
        current_player: The player who has the current turn.
        title_frame: The frame that holds the title label.
        player_turn_label: The label that displays the current player's turn.
        board_widgets: The list of buttons representing the game board.
    """
    
    def __init__(self, root, help: Help, game_controller) -> None:
        """
        Initializes the GameBoard instance.
        
        Args:
            root: The tkinter root object.
            help (Help): An instance of the Help class that provides configuration settings.
            game_controller: The game controller object that controls the game flow.
        """
        self.h = help
        self.board = root
        self.game_controller = game_controller
        self.board_frame = self.create_board_frame(self.board)
        self.current_player = self.h.player1
        self.title_frame = tk.Frame(root, pady=5, bg=help.frame_colour)
        self.player_turn_label = tk.Label(self.title_frame, padx=10, pady=10, text=self.current_player + "'s turn", font=(help.button_text_font, help.title_size), bg=help.title_colour)
        self.board_widgets = []
        
    def end_game(self) -> None:
        """
        Ends the game and displays the end screen.
        """
        self.game_controller.end_screen()
        
    def create_board_frame(self, root) -> tk.Frame:
        """
        Creates and returns the game board frame.
        
        Args:
            root: The tkinter root object.
            
        Returns:
            The created game board frame.
        """
        board_frame = tk.Frame(root, bg=self.h.frame_colour)
        board_frame.place(relx=0.5, rely=.56, anchor="center")
        return board_frame

    def create_board3(self, board_frame) -> None:
        """
        Creates the 3x3 game board.
        
        Args:
            board_frame: The frame where the game board will be placed.
        """
        for row in range(3):
            for column in range(3):
                widget = tk.Button(board_frame, text="", width=6, height=3, font=(self.h.button_text_font, self.h.button_text_size))
                widget.grid(row=row, column=column)
                widget.configure(command=lambda clicked_button=widget: self.game_button_action(clicked_button))
                self.board_widgets.append(widget)

    def create_board5(self, board_frame) -> None:
        """
        Creates the 5x5 game board.
        
        Args:
            board_frame: The frame where the game board will be placed.
        """
        for row in range(5):
            for column in range(5):
                widget = tk.Button(board_frame, text="", width=3, height=1, font=(self.h.button_text_font, self.h.button_text_size))
                widget.grid(row=row, column=column)
                widget.configure(command=lambda clicked_button=widget: self.game_button_action(clicked_button))
                self.board_widgets.append(widget)

    def show(self, chosen_board_size) -> None:
        """
        Displays the game board with the specified board size.
        
        Args:
            chosen_board_size: The chosen board size (3 or 5).
        """
        self.title_frame.pack()
        self.player_turn_label.pack(side="top")
        if (chosen_board_size == "3"):
            self.create_board3(self.board_frame)
        elif (chosen_board_size == "5"):
            self.create_board5(self.board_frame)

    def hide(self) -> None:
        """
        Hides the game board.
        """
        self.title_frame.pack_forget()
        self.player_turn_label.pack_forget()
        self.board_frame.pack_forget()
        for widget in self.board_widgets:
            widget.grid_forget()
            
    def destroy_widgets(self) -> None:
        """
        Destroys all the widgets in the game board.
        """
        self.title_frame.destroy()
        self.player_turn_label.destroy()
        self.board_frame.destroy()
        for widget in self.board_widgets:
            widget.destroy()
            
    def switch_player(self) -> None:
        """
        Switches the current player.
        """
        if (self.current_player == self.h.player1):
            self.current_player = self.h.player2
        else:
            self.current_player = self.h.player1
            
    def pvp_action(self, clicked_button: tk.Button) -> bool:
        """
        Performs the player's action when a button on the game board is clicked.
        
        Args:
            clicked_button: The button that was clicked.
            
        Returns:
            True if the action was performed successfully, False otherwise.
        """
        if clicked_button.cget("text") == "":
            clicked_button.configure(text=self.current_player)
            return True
        else:
            messagebox.showwarning("Warning!", "This tile is already taken!")
            return False
            
    def pve_action(self) -> None:
        """
        Performs the computer's action using the Minimax algorithm.
        """
        best_score = float("-inf")
        best_move = None
        widgets_copy = [widget.cget("text") for widget in self.board_widgets]
        
        for i in range(len(widgets_copy)):
            if widgets_copy[i] == "":
                widgets_copy[i] = self.h.player2
                score = minimax(self, widgets_copy, 0, False, float("-inf"), float("inf"))
                widgets_copy[i] = ""
                
                if score > best_score:
                    best_score = score
                    best_move = self.board_widgets[i]
                    
        if best_move:
            best_move.configure(text=self.h.player2)
            
    def game_button_action(self, clicked_button) -> None:
        """
        Handles the game button action when a button on the game board is clicked.
        
        Args:
            clicked_button: The button that was clicked.
        """
        if (self.h.current_game_mode == "PvP"):
            may_continue = self.pvp_action(clicked_button)
            if may_continue:
                self.check_end_game()
                self.switch_player()
                self.change_current_player_label()
        else:
            if (self.current_player == self.h.player1):
                may_continue = self.pvp_action(clicked_button)
                if may_continue:
                    if self.check_end_game():
                        return
                    self.switch_player()
                    self.change_current_player_label()
                    self.pve_action()
                    self.check_end_game()
                    self.switch_player()
                    self.change_current_player_label()

    def change_current_player_label(self) -> None:
        """
        Changes the current player which is displayed on the player label.
        """
        self.player_turn_label.configure(text=self.current_player + "'s turn")
        
    def check_end_game(self) -> bool:
        """
        Checks if the game has ended in any way and adjusts the end screen accordingly.
        
        Returns:
            True if the game has ended, False otherwise.
        """
        if (self.check_winner(self.board_widgets, self.game_controller.chosen_board_size)):
            self.h.winning_player = self.h.set_winning_player(self.current_player)
            self.game_controller.end_screen(self.h.player_won_message)
            return True
        elif (self.check_draw()):
            self.game_controller.end_screen(self.h.game_tie_message)
            return True
        
        return False
            
    def check_draw(self) -> bool:
        """
        Checks if the game has resulted in a draw.
        
        Returns:
            True if the game is a draw, False otherwise.
        """
        for widget in self.board_widgets:
            if widget.cget("text") == "":
                return False
        return True

    def check_winner(self, board_widgets, board_size) -> bool:
        """
        Checks if there is a winner in the game.
        
        Args:
            board_size: The size of the game board (3 or 5).
            
        Returns:
            True if there is a winner, False otherwise.
        """
        if board_size == "3":
            # Horizontal check
            for row in range(3):
                if (board_widgets[row * 3]["text"] == 
                    board_widgets[row * 3 + 1]["text"] == 
                    board_widgets[row * 3 + 2]["text"] != ""
                    ):
                    return True
            # Vertical check
            for column in range(3):
                if (board_widgets[column]["text"] == 
                    board_widgets[column + 3]["text"] == 
                    board_widgets[column + 6]["text"] != ""
                    ):
                    return True
            # Diagonal check
            if (board_widgets[0]["text"] == 
                board_widgets[4]["text"] == 
                board_widgets[8]["text"] != ""
                ):
                return True
            if (board_widgets[2]["text"] == 
                board_widgets[4]["text"] == 
                board_widgets[6]["text"] != ""
                ):
                return True
            return False
        
        elif board_size == "5":
            winning_positions = [
                # Horizontal
                [0, 1, 2, 3],
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [6, 7, 8, 9],
                [10, 11, 12, 13],
                [11, 12, 13, 14],
                [15, 16, 17, 18],
                [16, 17, 18, 19],
                # Vertical
                [0, 5, 10, 15],
                [5, 10, 15, 20],
                [1, 6, 11, 16],
                [6, 11, 16, 21],
                [2, 7, 12, 17],
                [7, 12, 17, 22],
                [3, 8, 13, 18],
                [8, 13, 18, 23],
                [4, 9, 14, 19],
                [9, 14, 19, 24],
                # Diagonal (top-left to bottom-right)
                [0, 6, 12, 18],
                [6, 12, 18, 24],
                [1, 7, 13, 19],
                [5, 11, 17, 23],
                [4, 8, 12, 16],
                [8, 12, 16, 20],
                [3, 7, 11, 15],
                [9, 13, 17, 21]
            ]

        for positions in winning_positions:
            symbols = [board_widgets[pos]["text"] for pos in positions]
            if all(symbol != "" and symbol == symbols[0] for symbol in symbols):
                return True

        return False