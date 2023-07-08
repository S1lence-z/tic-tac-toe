# my minimax algorithm
import tkinter as tk

def get_winner(board_widgets: tk.Button, board_size) -> str:
    if board_size == "3":
        # Horizontal check
        for row in range(3):
            if (board_widgets[row * 3]["text"] == 
                board_widgets[row * 3 + 1]["text"] == 
                board_widgets[row * 3 + 2]["text"] != ""
                ):
                return board_widgets[row]["text"]
        # Vertical check
        for column in range(3):
            if (board_widgets[column]["text"] == 
                board_widgets[column + 3]["text"] == 
                board_widgets[column + 6]["text"] != ""
                ):
                return board_widgets[column]["text"]
        # Diagonal check
        if (board_widgets[0]["text"] == 
            board_widgets[4]["text"] == 
            board_widgets[8]["text"] != ""
            ):
            return board_widgets[0]["text"]
        if (board_widgets[2]["text"] == 
            board_widgets[4]["text"] == 
            board_widgets[6]["text"] != ""
            ):
            return board_widgets[2]["text"]
        return None

def is_draw(board_widgets: tk.Button) -> bool:
    for widget in board_widgets:
        if widget.cget("text") == "":
            return False
    return True

def minimax(gameBoard_class, board_widgets, depth: int, is_maximizing: bool):
    human_player = gameBoard_class.h.player1
    ai_player = gameBoard_class.h.player2
    
    if gameBoard_class.check_winner(board_widgets, gameBoard_class.game_controller.chosen_board_size):
        winner = get_winner(board_widgets, gameBoard_class.game_controller.chosen_board_size)
        if winner == ai_player:
            return 1
        elif winner == human_player:
            return -1
        elif is_draw(board_widgets):
            return 0
    
    if is_maximizing:
        best_score = float("-inf")
        for widget in board_widgets:
            if widget.cget("text") == "":
                widget.configure(text=ai_player)
                score = minimax(gameBoard_class, board_widgets, depth + 1, False)
                widget.configure(text="")
                best_score = max(score, best_score)
        return best_score
    
    else:
        best_score = float("inf")
        for widget in board_widgets:
            if widget.cget("text") == "":
                widget.configure(text=human_player)
                score = minimax(gameBoard_class, board_widgets, depth + 1, True)
                widget.configure(text="")
                best_score = min(score, best_score)
        return best_score