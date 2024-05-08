# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Print each row with "|" separating the cells
        print("-"*5)  # Print horizontal line separating rows

# Function to check if a player has won
def check_winner(board,player):
    # Check rows
    for row in board:
        if all(cell==player for cell in row): # Check if all cells in a row belong to the same player
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col]==player for row in range(3)):  # Check if all cells in a column belong to the same player
            return True
    # Check diagonals
    if all(board[i][i]==player for i in range(3)) or all(board[i][2-i]==player for i in range(3)):
        # Check if all cells in the main diagonal or anti-diagonal belong to the same player
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:  # If there's an empty cell, the board is not full
            return False
    return True

# Main function to run the Tic Tac Toe game
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Create an empty board
    current_player="X"  # Initialize the first player
    while True:  # Game loop
        print_board(board)  # Print the current board
        row=int(input(f"Player {current_player},enter row (0, 1, or 2): "))  # Get row input from the current player
        col=int(input(f"Player {current_player},enter column (0, 1, or 2): "))  # Get column input from the current player

        if board[row][col]!=" ":  # Check if the chosen cell is already taken
            print("That cell is already taken. Try again.")
            continue
        board[row][col]=current_player  # Place the player's symbol on the board
        if check_winner(board,current_player):  # Check if the current player has won
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):  # Check if the board is full (resulting in a tie)
            print_board(board)
            print("It's a tie!")
            break
        current_player="O" if current_player=="X" else "X"  # Switch to the next player
        
# Run the game
tic_tac_toe()