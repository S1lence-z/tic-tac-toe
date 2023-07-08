# my minimax algorithm
import tkinter as tk

def get_winner(board: list[str], board_size: str) -> str:
    if board_size == "3":
        # Horizontal check
        for row in range(3):
            if (board[row * 3] == 
                board[row * 3 + 1] == 
                board[row * 3 + 2] != ""
                ):
                return board[row]
        # Vertical check
        for column in range(3):
            if (board[column] == 
                board[column + 3] == 
                board[column + 6] != ""
                ):
                return board[column]
        # Diagonal check
        if (board[0] == 
            board[4] == 
            board[8] != ""
            ):
            return board[0]
        if (board[2] == 
            board[4] == 
            board[6] != ""
            ):
            return board[2]
        return "nothing"

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
    if winner != "nothing":
        # i have to return -1 as a default value, it does not work for this case
        # ['O', 'X', '', 'O', 'O', '', 'X', 'X', 'X']
        # for this case the returned score by the minimax functino is None!
        # it also does not work when the human player starts in the middle
        return scores.get(winner, -1)
    elif is_draw(board):
        return scores.get("tie", -1)

    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = ai_player
                score = minimax(gameBoard_class, board, depth + 1, not is_maximizing)
                board[i] = ""
                if score == None or best_score == None:
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