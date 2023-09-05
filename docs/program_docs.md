# Code Documentation

This part of the game documentation provides information about the scripts and classes the game uses to operate.

There are **7 files**:

1. **main.py** - contains the TicTacToeGame class which represents the game as a whole and uses classes and methods from all the other scripts
2. **appWindow.py** - contains the AppWindow class which represents the main application window for the game in made with tkinter
3. **endScreen.py** - contains the EndScreen class which represents the end screen of the game, contains all the necessary buttons and titles
4. **gameBoard.py** - contains the GameBoard class which represents the game board for the game, it contatins both 3x3 and 4x4 boards
5. **help.py** - contatins settings which area used throughout the whole game, for example window and text colours or the chosen game board size
6. **mainMenu.py** - contains the MainMenu class which represents the main menu of the game, it is also made with tkinter
7. **minimaxAlg.py** - contains the minimax algorithm which is in a function and also the get_winner() method which is used to determine if the game is finished