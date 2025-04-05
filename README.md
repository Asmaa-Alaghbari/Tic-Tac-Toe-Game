# Tic Tac Toe Game

![Tic Tac Toe](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tic_tac_toe.svg/200px-Tic_tac_toe.svg.png)

A classic two-player strategy game where opponents alternate turns marking spaces on a 3x3 grid. The current player places their symbol (X or O), aiming to form a horizontal, vertical, or diagonal line of three matching marks to win. If all spaces are filled without a winner, the game ends in a draw.

## Table of Contents

## Project Details

- **Author**: Asmaa Alaghbari
- **Start date**: 04/04/2025
- **Last update**: 05/04/2025
- **Programming Language**: Python 3.x
- **Tool Used**: Visual Studio Code
- **Game Title**: Tic Tac Toe
- **Game Type**: Console-based
- **Game Mode**: Player vs Computer
- **Game Board**: 3x3 grid
- **Game Symbols**: X and O
- **Game Outcome**: Win, Lose, or Draw
- **Input Method**: Numbered positions (1-9) for player moves
- **Computer AI**: Random move selection
- **Input Validation**: Ensures valid moves and prevents overwriting existing marks

## Features

- Player vs Computer gameplay
- Intelligent computer move selection
- Clear display of the game board
- Win, lose, or draw messages
- Option to play again
- Simple yet extendable code for improvements

## How to Play

1. Clone the repository [Tic-Tac-Toe-Game
   ](https://github.com/Asmaa-Alaghbari/Tic-Tac-Toe-Game/) or download the ZIP file.
2. Open the `tic_tac_toe.py` file in your Python environment.
3. Run the script using Python 3.x.
4. Follow the on-screen instructions to play the game.
5. Enter your name when prompted
6. Choose to play as X or O (X goes first)
7. On your turn, enter a number (1-9) corresponding to the board position:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

8. The computer will automatically make its move after yours

9. The game ends when either:

   - A player gets 3 in a row (horizontally, vertically, or diagonally)
   - All spaces are filled (draw)

10. You'll be asked if you want to play again when the game ends
11. Type 'yes' or 'no' to continue or exit the game
12. Enjoy the game!

## Requirements

- Python 3.x
- No additional libraries are required
- Just run the script in a Python environment
- Compatible with Windows, macOS, and Linux

## Code Structure

| File/Function     | Description                          |
| ----------------- | ------------------------------------ |
| `tic_tac_toe.py`  | Main game file                       |
| `board`           | List representing the 3x3 game grid  |
| `display_board()` | Prints the current game state        |
| `player_move()`   | Handles player input and validation  |
| `computer_move()` | AI makes a move using basic strategy |
| `check_winner()`  | Checks win conditions                |
| `play_game()`     | Main game loop                       |
| `play_again()`    | Handles replay logic                 |

## References

- [Codecademy - Python](https://www.codecademy.com/learn/learn-python-3)
- [GeeksforGeeks - Tic Tac Toe in Python](https://www.geeksforgeeks.org/tic-tac-toe-in-python/)
- [Python Official Documentation](https://docs.python.org/3/)
- [W3Schools - Python](https://www.w3schools.com/python/)
- [Wikipedia - Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)
