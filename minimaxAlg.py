def minimax(gameBoard_class, depth: int, is_maximizing: bool):
    human_player = gameBoard_class.h.player1
    computer_player = gameBoard_class.h.player2
    
    scores = {
        computer_player: 1,  
        human_player: -1,
        "draw": 0
    }
    
    if gameBoard_class.check_winner(gameBoard_class.game_controller.chosen_board_size):
        winner = gameBoard_class.current_player
        return scores[winner]
    
    if gameBoard_class.check_draw():
        return scores["draw"]
    
    if is_maximizing:
        best_score = float("-inf")
        for widget in gameBoard_class.board_widgets:
            if widget.cget("text") == "":
                widget.configure(text=computer_player)
                score = minimax(gameBoard_class, depth + 1, False)
                widget.configure(text="")
                best_score = max(score, best_score)
        return best_score
    
    else:
        best_score = float("inf")
        for widget in gameBoard_class.board_widgets:
            if widget.cget("text") == "":
                widget.configure(text=human_player)
                score = minimax(gameBoard_class, depth + 1, True)
                widget.configure(text="")
                best_score = min(score, best_score)
        return best_score