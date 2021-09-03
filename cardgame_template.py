import pygame
import sys

from cardgame_classes import Button, Deck

# A few variables for our colors
BLACK = (0,0,0)
GREEN = (0,120,10)
WHITE = (255, 255, 255)
WIDTH = 700
HEIGHT = 700


# Initialize PyGame
pygame.init()
pygame.display.set_caption('My Card Game')
canvas = pygame.display.set_mode((WIDTH, HEIGHT))

# Setup buttons and such
def ex_function():
    print('Ex_function called')

button = Button('Default Button', (100, 100), (250, 100), ex_function)


while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (button.isOver()):
                button.action()

    # Fill screen with bg color, then your drawings
    canvas.fill(GREEN)
    button.draw(canvas)

    # The logic of your game
    # Draws things, moves things etc.
    pygame.display.flip()




