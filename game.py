import pygame
import sys
import math 
import numpy as np
import os
from pygame.locals import *
from random import randint

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
MENU_FONT_SIZE = 48
MENU_ITEM_PADDING = 40

# Colors
WHITE = (250,42,85)
GREEN = (219,219,250)
RED = (255,0,0)
BLACK = (0, 0, 0)
abc = (227,11,93)
# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2-Player Game Menu")

# Initialize the font
font = pygame.font.Font(None, MENU_FONT_SIZE)

# Menu items
menu_items = ["Connect 4", "Air Hockey", "Tic Tac Toe", "Quit"]
selected_item = 0

def draw_menu():
    screen.fill(GREEN)
    for i, item in enumerate(menu_items):
        text = font.render(item, True, WHITE if i == selected_item else BLACK)
        #text_rect = text.get_rect(center=(WIDTH // 2,(i + 1) * MENU_ITEM_PADDING))
        font1 = pygame.font.Font(None,54)
        text1 = font1.render("2 - PLAYER GAMES",True,WHITE)
        screen.blit(text1,((WIDTH - text1.get_width()) // 2, 70))
        menu_height = len(menu_items) * MENU_ITEM_PADDING
        start_y = (HEIGHT - menu_height) // 2
        text_rect = text.get_rect(center=(WIDTH // 2, start_y + i * MENU_ITEM_PADDING))
        screen.blit(text, text_rect)
    pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if selected_item == len(menu_items) - 1:
                    running = False
                else:
                    print("Selected game:", menu_items[selected_item])  # Replace with your game logic
                    if selected_item == 0:
                        import connect4
                    elif selected_item == 1:
                        import airHockey
                    elif selected_item == 2:
                        import ticTacToe

    draw_menu()

pygame.quit()
sys.exit()
