# Tic Tac Toe Game in Python

# The game board (3x3 grid)
board = [" " for _ in range(9)]


# Print the Tic Tac Toe board
def display_baord():
    print("Tic Tac Toe board:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")


# The player's move
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move] != " ":
                print("This position is already taken. Try again.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


# Check for a winner
def check_winner(player):
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

    # Check if the player has any winning combination
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    # Check for a tie (no empty spaces left)
    if all(space != " " for space in board):
        print("It's a tie!")
        return True  # No winner, but the game is over

    return False  # No winner yet


# Main game loop
def play_game(player_name):
    print(f"{player_name.title()}, you will be playing against the computer.")
    print("Do you want to play as X or O?")
    player_choice = input("Enter X or O: ").strip().upper()
    while player_choice not in ["X", "O"]:
        player_choice = input("Invalid choice. Please enter X or O: ").strip().upper()

    computer_choice = "O" if player_choice == "X" else "X"
    print(f"You are {player_choice}, and the computer is {computer_choice}.")

    for turn in range(9):
        display_baord()
        # player's turn
        if turn % 2 == 0:
            player_move(player_choice)
            if check_winner(player_choice):
                display_baord()
                print(f"Congratulations {player_name.title()}, you win!")
                break
        else:
            # Computer's move (random choice)
            import random

            while True:
                move = random.randint(0, 8)
                if board[move] == " ":
                    board[move] = computer_choice
                    break
            if check_winner(computer_choice):
                display_baord()
                print(f"Computer wins! Better luck next time, {player_name.title()}!")
                break


# The game is over, and we can ask the players if they want to play again
def play_again(player_name):
    while True:
        again = (
            input(f"{player_name.title()}! Do you want to play again? (Yes/No): ")
            .strip()
            .lower()
        )
        if again == "yes":
            board[:] = [" " for _ in range(9)]  # Reset the board
            play_game(player_name)
        elif again == "no":
            print(f"Thanks {player_name.title()} for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


print("Let's play Tic Tac Toe!")
player_name = input("Enter your name: ")
print(f"Welcome {player_name.title()} to Tic Tac Toe game!")

play_game(player_name)
play_again(player_name)

# End of the game
