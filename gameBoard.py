import tkinter as tk
from help import Help

class GameBoard:
    def __init__(self, board, h: Help):
        self.h = h
        self.board = board
        self.title_frame = tk.Frame(board, pady=10, bg=h.frame_colour)
        
        self.player_turn_label = tk.Label(self.title_frame, padx=10, pady=10, text=h.player + " turn", font=(h.button_text_font, h.title_size), bg=h.title_colour)

    def create_board3(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")
        
        for row in range(3):
            for column in range(3):
                self.h.board3[row][column] = tk.Button(board_frame, text="", width=20, height=10)
                self.h.board3[row][column].grid(row=row, column=column)
                
    def create_board4(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")

        sub_frame = tk.Frame(board_frame)
        sub_frame.grid(row=0, column=0)

        for row in range(4):
            for column in range(4):
                self.h.board4[row][column] = tk.Button(sub_frame, text="", width=18, height=7)
                self.h.board4[row][column].grid(row=row, column=column)
                
    def show(self, chosen_board) -> None:
        self.title_frame.pack()
        self.player_turn_label.pack(side="top")
        # create chosen board
        if (chosen_board == "3"):
            self.create_board3(self.board)
        elif (chosen_board == "4"):
            self.create_board4(self.board)