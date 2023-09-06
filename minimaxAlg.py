import tkinter as tk

def get_winner(board: list[str], board_size: str) -> str:
    """
    Determines the winner of the tic-tac-toe game based on the current board configuration.

    Args:
        board (list[str]): The current state of the tic-tac-toe board.
        board_size (str): The size of the tic-tac-toe board (either "3" or "4").

    Returns:
        str: The winner of the game ("X" or "O") or "tie" for a tie game. If the game is not yet over, returns None.
    """
    if board_size == "3":
        # Define the winning combinations for a 3x3 board
        winning_combinations = [
            # Rows
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Columns
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonals
            [0, 4, 8], [2, 4, 6]
        ]
        
        # Check each winning combination to see if any player has won
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != "":
                return board[combination[0]]
        
        # If there are no empty spaces left on the board, it's a tie
        if "" not in board:
            return "tie"
        
        # No winner yet
        return None
    
    elif board_size == "4":
        # Define the winning combinations for a 4x4 board
        winning_combinations = [
            # Horizontal
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15],
            # Vertical
            [0, 4, 8, 12],
            [1, 5, 9, 13],
            [2, 6, 10, 14],
            [3, 7, 11, 15],
            # Diagonal (top-left to bottom-right)
            [0, 5, 10, 15],
            [3, 6, 9, 12]
        ]

        # Check each winning combination to see if any player has won
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] == board[combination[3]] != "":
                return board[combination[0]]

        # If there are no empty spaces left on the board, it's a tie
        if "" not in board:
            return "tie"

        # No winner yet
        return None

def check_tie_3(gameBoard_class) -> bool:
    """This function returns True if the 3x3 game cannot be won by either player (the only outcome is a tie) else false.

    Args:
        gameBoard_class (GameBoard): an instance of the GameBoard class

    Returns:
        bool: if the only outcome is a tie returns true else false
    """
    return

def check_tie_4(gameBoard_class) -> bool:
    """This function returns True if the 4x4 game cannot be won by either player (the only outcome is a tie) else false.

    Args:
        gameBoard_class (GameBoard): an instance of the GameBoard class

    Returns:
        bool: if the only outcome is a tie returns true else false
    """
    return
    

def minimax(gameBoard_class, board, depth: int, is_maximizing: bool, alpha: float, beta: float, memoization_table: dict) -> float:
    """
    Implementation of the minimax algorithm with alpha-beta pruning to find the best move for the AI player.

    Args:
        gameBoard_class: An instance of the game board class.
        board (list[str]): The current state of the tic-tac-toe board.
        depth (int): The current depth of the minimax search tree.
        is_maximizing (bool): Indicates whether it's the maximizing player's turn or not.
        alpha (float): The alpha value for alpha-beta pruning.
        beta (float): The beta value for alpha-beta pruning.

    Returns:
        float: The best score for the current board state.
    """
    human_player = gameBoard_class.h.player1
    ai_player = gameBoard_class.h.player2
    
    scores = {
        human_player: -1,
        ai_player: 1,
        "tie": 0
    }
    
    # I have to convert the board to an immutable object
    hash_ready_board = tuple(board)
    if hash_ready_board in memoization_table:
        return memoization_table[hash_ready_board]
    
    winner = get_winner(board, gameBoard_class.game_controller.chosen_board_size)
    if winner is not None:
        final_score = scores.get(winner)
        memoization_table[hash_ready_board] = final_score
        return final_score

    if is_maximizing:
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = ai_player
                score = minimax(gameBoard_class, board, depth + 1, not is_maximizing, alpha, beta, memoization_table)
                board[i] = ""
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        memoization_table[hash_ready_board] = best_score
        return best_score
    
    else:
        best_score = float("inf")
        for i in range(len(board)):
            if board[i] == "":
                board[i] = human_player
                score = minimax(gameBoard_class, board, depth + 1, not is_maximizing, alpha, beta, memoization_table)
                board[i] = ""
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        memoization_table[hash_ready_board] = best_score
        return best_score