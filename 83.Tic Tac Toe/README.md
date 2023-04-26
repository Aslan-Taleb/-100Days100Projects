## Tic Tac Toe Game
This is a simple implementation of the classic Tic Tac Toe game in Python 3. It allows two players to play against each other and keeps track of their scores, as well as the number of draws.

![Image of My Project](https://i.imgur.com/lTUcswT.png)

Link : https://replit.com/@AslanTaleb/Tic-Tac-Toe

## How to Run

Clone the repository to your local machine.
Open the terminal/command prompt and navigate to the directory where the repository is cloned.
Run the following command to start the game: python tic_tac_toe.py
## How to Play:

The game board will be displayed on the screen.
Player 1 will be represented by X and Player 2 by O.
Players will take turns to select a position on the board where they want to place their symbol.
The game will end when a player wins, or there is a draw.
At the end of the game, players will be prompted if they want to play again.

## Technical Details:

The game is implemented using Python 3 and uses a two-dimensional list to represent the game board. The game board is displayed using the show_game() function, which is called after each move.
The test_win() function is used to check if a player has won the game. It checks the rows, columns, and diagonals of the game board to see if all the elements belong to the same player.
The test_draw() function is used to check if the game has ended in a draw. It does this by checking if all the positions on the board are filled with symbols and no player has won.
The game uses the os module to clear the screen after each move, providing a better user experience.
The game keeps track of the scores using a dictionary, scores, which stores the number of wins for each player and the number of draws.

## Acknowledgments:

This implementation of Tic Tac Toe is based on the classic game and is intended as a simple demonstration of Python programming. The code is not optimized and can be improved upon. Suggestions and contributions are welcome.

## ideas for when i have time : 

add Ia Player and try to make impossible to beat