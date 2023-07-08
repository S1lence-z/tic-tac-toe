# my minimax algorithm
import tkinter as tk

def get_winner(board: list[str], board_size: str) -> str:
    if board_size == "3":
        winning_combinations = [
            # Rows
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Columns
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonals
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != "":
                return board[combination[0]]
        
        if "" not in board:
            return "tie"
        
        return None


def is_draw(board: list[str]) -> bool:
    for text in board:
        if text == "":
            return False
    return True

def minimax(gameBoard_class, board, depth: int, is_maximizing: bool):
    human_player = gameBoard_class.h.player1
    ai_player = gameBoard_class.h.player2
    
    scores = {
        human_player: -1,
        ai_player: 1,
        "tie": 0
    }
    
    winner = get_winner(board,  gameBoard_class.game_controller.chosen_board_size)
    if winner != None:
        return scores.get(winner)
    elif is_draw(board):
        return scores.get("tie")

    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = ai_player
                score = minimax(gameBoard_class, board, depth + 1, not is_maximizing)
                board[i] = ""
                if score == None or best_score == None:
                    print(board)
                    print(score, best_score)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = human_player
                score = minimax(gameBoard_class, board, depth + 1, not is_maximizing)
                board[i] = ""
                if score == None or best_score == None:
                    board[i] = human_player
                    print(board)
                    print(score, best_score)
                best_score = min(score, best_score)
        return best_score