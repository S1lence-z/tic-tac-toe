import tkinter as tk
from help import Help

class TicTacToeBoard:
    def __init__(self, board):
        h = Help()
        self.h = h
        title_frame = tk.Frame(board, pady=10, bg=h.frame_colour)
        title_frame.pack()
       
        player_turn_label = tk.Label(title_frame, padx=10, pady=10, text=h.player + " turn", font=(h.font1, h.title_size), bg=h.title_colour)
        player_turn_label.pack(side="top")
        self.create_board3(board)

    def create_board3(self, board):
        board_frame = tk.Frame(board)
        board_frame.place(relx=0.5, rely=.56, anchor="center")
        
        for row in range(3):
            for column in range(3):
                self.h.board3[row][column] = tk.Button(board_frame, text="", width=16, height=8)
                self.h.board3[row][column].grid(row=row, column=column)