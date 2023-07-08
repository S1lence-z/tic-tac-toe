# my minimax algorithm
import tkinter as tk

def get_winner(board_widgets: tk.Button, board_size) -> str:
    if board_size == "3":
        # Horizontal check
        for row in range(3):
            if (board_widgets[row * 3] == 
                board_widgets[row * 3 + 1] == 
                board_widgets[row * 3 + 2] != ""
                ):
                return board_widgets[row]
        # Vertical check
        for column in range(3):
            if (board_widgets[column] == 
                board_widgets[column + 3] == 
                board_widgets[column + 6] != ""
                ):
                return board_widgets[column]
        # Diagonal check
        if (board_widgets[0] == 
            board_widgets[4] == 
            board_widgets[8] != ""
            ):
            return board_widgets[0]
        if (board_widgets[2] == 
            board_widgets[4] == 
            board_widgets[6] != ""
            ):
            return board_widgets[2]
        return None

def is_draw(board: list) -> bool:
    for text in board:
        if text == "":
            return False
    return True

def convert_to_board_widgets(board: list[str], board_widgets: list[tk.Button]) -> list[tk.Button]:
    for i in range(len(board)):
        board_widgets[i].configure(text=board[i])
    return board_widgets

def minimax(gameBoard_class, board_widgets, depth: int, is_maximizing: bool):
    board = [widget.cget("text") for widget in board_widgets]
    
    scores = {
        gameBoard_class.h.player1: -1,
        gameBoard_class.h.player2: 1,
        "tie": 0
    }

    if get_winner(board, gameBoard_class.game_controller.chosen_board_size):
        if is_maximizing:
            return scores[gameBoard_class.h.player2]
        else:
            return scores[gameBoard_class.h.player1]
    elif is_draw(board):
        return scores["tie"]

    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = gameBoard_class.h.player2
                temp = convert_to_board_widgets(board, board_widgets)
                score = minimax(gameBoard_class, temp, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = gameBoard_class.h.player1
                temp = convert_to_board_widgets(board, board_widgets)
                score = minimax(gameBoard_class, temp, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score