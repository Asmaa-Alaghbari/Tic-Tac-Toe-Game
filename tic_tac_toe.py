# Tic Tac Toe Game in Python

import random


class TicTacToe:
    def __init__(self, player_name, player_symbol):
        self.player_name = player_name.title()
        self.player_symbol = player_symbol  # Player's symbol (X or O)
        self.computer_symbol = "X" if player_symbol == "O" else "O"
        self.board = [" " for _ in range(9)]  # Game board (3x3 grid)

    # Display the game board
    def display_board(self):
        print(f"\nLet's start, {self.player_name}! Here your Tic Tac Toe board:\n")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-" * 9)
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-" * 9)
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")

    # Player's move
    def player_move(self):
        while True:
            try:
                move = (
                    int(
                        input(
                            f"Player {self.player_symbol} ({self.player_name}), enter your move (1-9): "
                        )
                    )
                    - 1
                )
                if move < 0 or move > 8:
                    print("Invalid move. Please enter a number between 1 and 9.")
                elif self.board[move] != " ":
                    print("This position is already taken. Try another position.")
                else:
                    self.board[move] = self.player_symbol
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    # Computer's move
    def computer_move(self):
        move = self.find_best_move()
        self.board[move] = self.computer_symbol
        print(f"Player {self.computer_symbol} (Computer) plays at position {move + 1}.")

    # Find the best move for the computer
    def find_best_move(self):
        for move in range(9):
            if self.board[move] == " ":
                self.board[move] = self.computer_symbol
                if self.check_winner(self.computer_symbol):
                    self.board[move] = " "
                    return move  # Winning move
                self.board[move] = " "

        for move in range(9):
            if self.board[move] == " ":
                self.board[move] = self.player_symbol
                if self.check_winner(self.player_symbol):
                    self.board[move] = " "
                    return move
                self.board[move] = " "

        return random.choice([i for i in range(9) if self.board[i] == " "])

    # Check for a winner
    def check_winner(self, symbol):
        # Define winning combinations (3 in a row)
        winning_combinations = [
            [0, 1, 2],  # Horizontal
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],  # Vertical
            [2, 5, 8],
            [0, 4, 8],  # Diagonal
            [2, 4, 6],
        ]

        # Check if any winning combination is met
        return any(
            all(self.board[i] == symbol for i in combo)
            for combo in winning_combinations
        )

    # Main game loop
    def play_game(self):
        print(f"\nWelcome {self.player_name} to Tic Tac Toe game!")
        print(
            f"You are playing as {self.player_symbol}, and the computer is {self.computer_symbol}."
        )

        while True:
            self.display_board()

            self.player_move()

            # Check if the player has won
            if self.check_winner(self.player_symbol):
                self.display_board()
                print(f"Congratulations {self.player_name}, you win!")
                break

            # Check if the game is a draw
            if all(space != " " for space in self.board):
                self.display_board()
                print("It's a tie!")
                break

            self.computer_move()

            # Check if the computer has won
            if self.check_winner(self.computer_symbol):
                self.display_board()
                print(f"Computer wins! Better luck next time, {self.player_name}.")
                break

            # Check if the game is a draw
            if all(space != " " for space in self.board):
                self.display_board()
                print("It's a tie!")
                break

        self.play_again()

    def play_again(self):
        while True:
            again = (
                input(f"{self.player_name}, do you want to play again? (Yes/No): ")
                .strip()
                .lower()
            )
            if again == "yes" or again == "y":
                self.board = [" " for _ in range(9)]  # Reset the board
                self.play_game()
            elif again == "no" or again == "n":
                print(f"Thanks for playing, {self.player_name}! See you next time!")
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")


# Game setup
player_name = input("Enter your name: ").strip()
player_symbol = (
    input(f"{player_name.title()}, do you want to play as X or O? ").strip().upper()
)
while player_symbol not in ["X", "O"]:
    player_symbol = input("Invalid choice. Please enter X or O: ").strip().upper()

game = TicTacToe(player_name, player_symbol)
game.play_game()

# End of the game
