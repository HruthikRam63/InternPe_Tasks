import pygame  # Import the pygame library for game development
import random  # Import the random module for generating random numbers

# Initialize Pygame
pygame.init()

# Define some colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)

# Define screen size
WIDTH=800
HEIGHT=600

# Create the screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))

# Define snake block size
block_size=10

# Define initial snake speed
snake_speed=15

def draw_snake(snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(screen,GREEN,[x[0],x[1],block_size,block_size])

def message(msg,color):
    """Display a message on the screen."""
    font_style=pygame.font.SysFont(None,50)  # Use a system font with size 50
    rendered_message=font_style.render(msg,True,color)  # Render the message
    screen.blit(rendered_message,[WIDTH/6,HEIGHT/3])  # Display the message on the screen

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False
    x1=WIDTH/2
    y1=HEIGHT/2
    x1_change=0
    y1_change=0
    snake_list=[]
    length_of_snake=1

    # Generate initial food position
    food_x=round(random.randrange(0,WIDTH-block_size)/10.0)*10.0
    food_y=round(random.randrange(0,HEIGHT-block_size)/10.0)*10.0

    clock=pygame.time.Clock()

    # Main game loop
    while not game_over:

        while game_close:  # Game over screen loop
            screen.fill(BLACK)
            message("You Lost! Press Q (Quit) or C (Retry)",WHITE)
            pygame.display.update()

            # Event handling for game over screen
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        game_close=False
                        game_loop()

        # Event handling for game
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and x1_change!=block_size:
                    x1_change=-block_size
                    y1_change=0
                elif event.key==pygame.K_RIGHT and x1_change!=-block_size:
                    x1_change=block_size
                    y1_change=0
                elif event.key==pygame.K_UP and y1_change!=block_size:
                    y1_change=-block_size
                    x1_change=0
                elif event.key==pygame.K_DOWN and y1_change!=-block_size:
                    y1_change=block_size
                    x1_change=0

        # Update snake position
        x1+=x1_change
        y1+=y1_change
        screen.fill(BLACK)  # Clear the screen
        pygame.draw.rect(screen,RED,[food_x,food_y,block_size,block_size])  # Draw food

        # Add new head position to snake list
        snake_head=[x1,y1]
        snake_list.append(snake_head)
        if len(snake_list)>length_of_snake:
            del snake_list[0]

        # Check for collisions with snake body & with boundaries
        for x in snake_list[:-1]:
            if x==snake_head:
                game_close=True
        
        if x1>=WIDTH or x1<0 or y1>=HEIGHT or y1<0:
            game_close=True

        # Check if snake has eaten food
        if x1==food_x and y1==food_y:
            food_x=round(random.randrange(0,WIDTH-block_size)/10.0)*10.0
            food_y=round(random.randrange(0,HEIGHT-block_size)/10.0)*10.0
            length_of_snake+=1
        # Draw the snake
        draw_snake(snake_list)
        # Update display
        pygame.display.update()
        # Set game speed
        clock.tick(snake_speed)
    
    pygame.quit()  # Quit pygame
    quit()

# Start the game
game_loop()