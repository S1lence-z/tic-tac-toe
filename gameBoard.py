import tkinter as tk
from help import Help

class GameBoard:
    def __init__(self, board, help: Help):
        self.h = help
        self.board = board
        self.title_frame = tk.Frame(board, pady=10, bg=help.frame_colour)
        self.player_turn_label = tk.Label(self.title_frame, padx=10, pady=10, text=help.player + " turn", font=(help.button_text_font, help.title_size), bg=help.title_colour)
        self.board_widgets = []

    def create_board3(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")

        for row in range(3):
            for column in range(3):
                widget = tk.Button(board_frame, text="", width=20, height=10)
                widget.grid(row=row, column=column)
                self.board_widgets.append(widget)

    def create_board4(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")

        sub_frame = tk.Frame(board_frame)
        sub_frame.grid(row=0, column=0)

        for row in range(4):
            for column in range(4):
                widget = tk.Button(sub_frame, text="", width=18, height=7)
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