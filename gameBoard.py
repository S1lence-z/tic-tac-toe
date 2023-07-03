import tkinter as tk
from tkinter import messagebox
from help import Help

class GameBoard:
    def __init__(self, root, help: Help, game_controller):
        # necessary classes and class variables
        self.h = help
        self.board = root
        self.game_controller = game_controller
        self.board_frame = self.create_board_frame(self.board)
        # specific playe variables
        self.player = help.player
        self.current_player = self.player
        # game board label
        self.title_frame = tk.Frame(root, pady=5, bg=help.frame_colour)
        self.player_turn_label = tk.Label(self.title_frame, padx=10, pady=10, text=self.current_player + "'s turn", font=(help.button_text_font, help.title_size), bg=help.title_colour)
        self.board_widgets = []
        
    def end_game(self) -> None:
        self.game_controller.end_screen()
        
    def create_board_frame(self, root) -> tk.Frame:
        board_frame = tk.Frame(root, bg=self.h.frame_colour)
        board_frame.place(relx=0.5, rely=.56, anchor="center")
        return board_frame

    def create_board3(self, board_frame):
        for row in range(3):
            for column in range(3):
                widget = tk.Button(board_frame, text="", width=6, height=3, font=(self.h.button_text_font, self.h.button_text_size))
                widget.grid(row=row, column=column)
                widget.configure(command=lambda clicked_button=widget: self.player_action(clicked_button))
                self.board_widgets.append(widget)

    def create_board4(self, board_frame):
        for row in range(4):
            for column in range(4):
                widget = tk.Button(board_frame, text="", width=5, height=2, font=(self.h.button_text_font, self.h.button_text_size))
                widget.grid(row=row, column=column)
                widget.configure(command=lambda clicked_button=widget: self.player_action(clicked_button))
                self.board_widgets.append(widget)

    def show(self, chosen_board_size) -> None:
        self.title_frame.pack()
        self.player_turn_label.pack(side="top")
        # create chosen board
        if (chosen_board_size == "3"):
            self.create_board3(self.board_frame)
        elif (chosen_board_size == "4"):
            self.create_board4(self.board_frame)

    def hide(self):
        self.title_frame.pack_forget()
        self.player_turn_label.pack_forget()
        self.board_frame.pack_forget()
        for widget in self.board_widgets:
            widget.grid_forget()
            
    def destroy_widgets(self):
        # Destroy all the widgets
        self.title_frame.destroy()
        self.player_turn_label.destroy()
        self.board_frame.destroy()
        for widget in self.board_widgets:
            widget.destroy()
            
    def player_switch(self) -> None:
        if (self.current_player == self.h.players[0]):
            self.current_player = self.h.players[1]
        else:
            self.current_player = self.h.players[0]
            
    def player_action(self, clicked_button: tk.Button) -> None:
        # check if this tile is not already taken
        if (clicked_button.cget("text") == ""):
            clicked_button.configure(text=self.current_player)
            if (self.check_winner(self.game_controller.chosen_board_size)):
                self.h.player = self.current_player
                self.game_controller.end_screen()
            self.player_switch()
            self.player_turn_label.configure(text=self.current_player + "'s turn")
        else:
            messagebox.showwarning("Warning!", "This tile is already taken!")

    def check_winner(self, board_size) -> bool:
        if (board_size == "3"):
            # Horizontal check
            for row in range(3):
                if (self.board_widgets[row * 3]["text"] == 
                    self.board_widgets[row * 3 + 1]["text"] == 
                    self.board_widgets[row * 3 + 2]["text"] != ""
                    ):
                    return True
            # Vertical check
            for column in range(3):
                if (self.board_widgets[column]["text"] == 
                    self.board_widgets[column + 3]["text"] == 
                    self.board_widgets[column + 6]["text"] != ""
                    ):
                    return True
            # Diagonal check
            if (self.board_widgets[0]["text"] == 
                self.board_widgets[4]["text"] == 
                self.board_widgets[8]["text"] != ""
                ):
                return True
            if (self.board_widgets[2]["text"] == 
                self.board_widgets[4]["text"] == 
                self.board_widgets[6]["text"] != ""
                ):
                return True
            return False
        
        else:
            # Horizontal check
            for row in range(4):
                if (self.board_widgets[row * 4]["text"] == 
                    self.board_widgets[row * 4 + 1]["text"] == 
                    self.board_widgets[row * 4 + 2]["text"] != ""
                    ):
                    return True
                if (self.board_widgets[row * 4 + 1]["text"] == 
                    self.board_widgets[row * 4 + 2]["text"] == 
                    self.board_widgets[row * 4 + 3]["text"] != ""
                    ):
                    return True
            # Vertical check
            for column in range(4):
                if (self.board_widgets[column]["text"] == 
                    self.board_widgets[column + 4]["text"] == 
                    self.board_widgets[column + 8]["text"] != ""
                    ):
                    return True
                if (self.board_widgets[column + 4]["text"] == 
                    self.board_widgets[column + 8]["text"] == 
                    self.board_widgets[column + 12]["text"] != ""
                    ):
                    return True
            # Diagonal check
            diagonal_checks = [
               [0, 5, 10],
               [1, 6, 11],
               [2, 7, 12],
               [3, 6, 9],
               [4, 7, 10],
               [5, 8, 11],
               [6, 9, 12],
               [7, 10, 13],
               [8, 11, 14],
               [9, 12, 15]
            ]
            for combination in diagonal_checks:
                if (
                    self.board_widgets[combination[0]]["text"] == 
                    self.board_widgets[combination[1]]["text"] == 
                    self.board_widgets[combination[2]]["text"] != ""
                    ):
                    return True

            return False