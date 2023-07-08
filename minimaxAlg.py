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
    
    elif board == "5":
        winning_combinations = [
            # Rows
            [0, 1, 2, 3], [1, 2, 3, 4], [5, 6, 7, 8], [6, 7, 8, 9],
            [10, 11, 12, 13], [11, 12, 13, 14], [15, 16, 17, 18], [16, 17, 18, 19], [20, 21, 22, 23],
            [21, 22, 23, 24],
            # Columns
            [0, 5, 10, 15], [5, 10, 15, 20], [1, 6, 11, 16], [6, 11, 16, 21], [2, 7, 12, 17], [7, 12, 17, 22],
            [3, 8, 13, 18], [8, 13, 18, 23], [4, 9, 14, 19], [9, 14, 19, 24],
            # Diagonals
            [0, 6, 12, 18], [6, 12, 18, 24], [1, 7, 13, 19], [5, 11, 17, 23], [4, 8, 12, 16], [8, 12, 16, 20], [3, 7, 11, 15], [9, 13, 17, 21]
        ]

        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] == board[combination[3]] != "":
                return board[combination[0]]

        if "" not in board:
            return "tie"

        return None

def minimax(gameBoard_class, board, depth: int, is_maximizing: bool, alpha: float, beta: float):
    human_player = gameBoard_class.h.player1
    ai_player = gameBoard_class.h.player2
    
    scores = {
        human_player: -1,
        ai_player: 1,
        "tie": 0
    }
    
    winner = get_winner(board, gameBoard_class.game_controller.chosen_board_size)
    if winner != None:
        return scores.get(winner)

    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = ai_player
                score = minimax(gameBoard_class, board, depth + 1, not is_maximizing, alpha, beta)
                board[i] = ""
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    
    else:
        best_score = float("inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = human_player
                score = minimax(gameBoard_class, board, depth + 1, not is_maximizing, alpha, beta)
                board[i] = ""
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score