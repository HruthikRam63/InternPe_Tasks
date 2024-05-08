import numpy as np  # Importing numpy library for numerical operations
import pygame  # Importing pygame library for game development
import sys  # Importing sys module for system-specific parameters and functions
import math  # Importing math module for mathematical operations

# Define color constants
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW =(255,255,0)
ROW_COUNT=6  # Number of rows in the game board
COLUMN_COUNT=7  # Number of columns in the game board

def create_board():
    """Create an empty game board."""
    board=np.zeros((ROW_COUNT,COLUMN_COUNT))  # Create a 2D numpy array filled with zeros
    return board

def drop_piece(board,row,col,piece):
    """Drop a game piece onto the board."""
    board[row][col]=piece

def is_valid_location(board,col):
    """Check if a column is a valid location for dropping a piece."""
    return board[ROW_COUNT-1][col]==0

def get_next_open_row(board,col):
    """Find the next available row in a column."""
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r

def print_board(board):
    """Print the game board."""
    print(np.flip(board,0))  # Print the board, flipping it vertically for better visualization

def winning_move(board,piece):
    """Check if a player has won the game."""
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

def draw_board(board):
    """Draw the game board."""
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))  # Draw the board squares
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):      
            if board[r][c]==1:
                pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)  # Draw Player 1's piece
            elif board[r][c]==2: 
                pygame.draw.circle(screen,YELLOW,(int(c*SQUARESIZE+SQUARESIZE/2),height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)  # Draw Player 2's piece
    pygame.display.update()

# Create the game board
board=create_board()
print_board(board)
game_over=False
turn=0

# Initialize pygame
pygame.init()

SQUARESIZE=100  # Size of each square on the board

width=COLUMN_COUNT*SQUARESIZE  # Calculate the width of the game window
height=(ROW_COUNT+1)*SQUARESIZE  # Calculate the height of the game window

size=(width,height)  # Set the size of the game window

RADIUS=int(SQUARESIZE/2-5)  # Calculate the radius of the game pieces

screen=pygame.display.set_mode(size)  # Set up the game window
draw_board(board)  # Draw the initial game board
pygame.display.update()

myfont=pygame.font.SysFont("monospace",75)  # Define the font for displaying text on the screen

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))  # Clear the top row of the game window
            posx=event.pos[0]  # Get the x-coordinate of the mouse position
            if turn==0:
                pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)  # Draw Player 1's piece in the top row
            else: 
                pygame.draw.circle(screen,YELLOW,(posx,int(SQUARESIZE/2)),RADIUS)  # Draw Player 2's piece in the top row
        pygame.display.update()

        if event.type==pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))  # Clear the top row of the game window
            # Ask for Player 1 Input
            if turn==0:
                posx=event.pos[0]
                col=int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,row,col,1)

                    if winning_move(board,1):
                        label=myfont.render("Player 1 wins!!",1,RED)
                        screen.blit(label,(40,10))
                        game_over=True

            # Ask for Player 2 Input
            else:                
                posx=event.pos[0]
                col=int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,row,col,2)

                    if winning_move(board,2):
                        label=myfont.render("Player 2 wins!!",1,YELLOW)
                        screen.blit(label,(40,10))
                        game_over=True

            print_board(board)
            draw_board(board)

            turn+=1
            turn=turn%2

            if game_over:
                pygame.time.wait(3000)  # Wait for 3 seconds before exiting the game
