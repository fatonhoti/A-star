from sys import exit

from models.grid import Grid
from settings import *

import pygame


SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("A-star")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def run():

    grid = Grid(SCREEN, SCREEN_SIZE, cell_size=10)

    # ----- PYGAME LOOP -----
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if event.button == LEFT_CLICK:
                    pass

                if event.button == RIGHT_CLICK:
                    pass

            # Handle space-bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

        # Draw

        # Update display
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    run()
