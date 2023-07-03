import tkinter as tk
from tkinter import messagebox
from help import Help

class GameBoard:
    def __init__(self, board, help: Help, game_controller):
        # necessary classes and class variables
        self.h = help
        self.game_controller = game_controller
        self.board = board
        # specific playe variables
        self.player = help.player
        self.current_player = self.player
        # game board label
        self.title_frame = tk.Frame(board, pady=10, bg=help.frame_colour)
        self.player_turn_label = tk.Label(self.title_frame, padx=10, pady=10, text=self.current_player + " turn", font=(help.button_text_font, help.title_size), bg=help.title_colour)
        self.board_widgets = []
        
    def end_game(self) -> None:
        self.game_controller.end_screen()

    def create_board3(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")

        for row in range(3):
            for column in range(3):
                widget = tk.Button(board_frame, text="", width=20, height=10)
                widget.grid(row=row, column=column)
                widget.configure(command=lambda clicked_button=widget: self.player_action(clicked_button))
                self.board_widgets.append(widget)

    def create_board4(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")

        for row in range(4):
            for column in range(4):
                widget = tk.Button(board_frame, text="", width=18, height=7)
                widget.grid(row=row, column=column)
                self.board_widgets.append(widget)

    def show(self, chosen_board) -> None:
        self.title_frame.pack()
        self.player_turn_label.pack(side="top")
        # create chosen board
        if (chosen_board == "3"):
            self.create_board3(self.board)
        elif (chosen_board == "4"):
            self.create_board4(self.board)

    def hide(self):
        self.title_frame.pack_forget()
        self.player_turn_label.pack_forget()
        for widget in self.board_widgets:
            widget.grid_forget()
            
    def player_switch(self) -> None:
        if (self.current_player == "X"):
            self.current_player = "O"
        else:
            self.current_player = "X"
            
    def player_action(self, clicked_button: tk.Button) -> None:
        # check if this tile is not already taken
        if (clicked_button.cget("text") == ""):
            clicked_button.configure(text=self.current_player)
            self.player_switch()
        else:
            messagebox.showwarning("Warning!", "This tile is already taken!")
