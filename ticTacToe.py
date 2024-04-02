import pygame
from pygame.locals import *

pygame.init()

screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

# Define colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define font
font = pygame.font.SysFont(None, 40)

# Define variables
clicked = False
player = 1
pos = (0, 0)
markers = []
game_over = False
winner = 0

# Create empty 3 x 3 list to represent the grid
for x in range(3):
    row = [0] * 3
    markers.append(row)

def draw_board():
    bg = (255, 255, 210)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, 100 * x), (screen_width, 100 * x), line_width)
        pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
            if y == -1:
                pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

def check_game_over():
    global game_over
    global winner

    x_pos = 0
    for x in markers:
        # Check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        # Check rows
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == -3:
            winner = 2
            game_over = True
        x_pos += 1

    # Check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

    # Check for tie
    if game_over == False:
        tie = True
        for row in markers:
            for i in row:
                if i == 0:
                    tie = False
        # If it is a tie, then call game over and set the winner to 0 (no one)
        if tie == True:
            game_over = True
            winner = 0

def draw_game_over(winner):
    if winner != 0:
        end_text = "Player " + str(winner) + " wins!"
    elif winner == 0:
        end_text = "You have tied!"

    end_img = font.render(end_text, True, blue)
    pygame.draw.rect(screen, green, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(end_img, (screen_width // 2 - 100, screen_height // 2 - 50))

# Main loop
run = True
while run:
    # Draw board and markers first
    draw_board()
    draw_markers()

    # Handle events
    for event in pygame.event.get():
        # Handle game exit
        if event.type == pygame.QUIT:
            run = False
        # Handle left mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if game_over == False:
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if markers[cell_x][cell_y] == 0:
                    markers[cell_x][cell_y] = player
                    player *= -1
                    check_game_over()
        # Wait for a key press after game over
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_LCTRL or pygame.K_LSHIFT or pygame.K_RETURN or pygame.K_RSHIFT or pygame.RCTRL:
                import game
        

    # Check if the game has been won
    if game_over == True:
        draw_game_over(winner)


    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
