from sys import exit

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("A-star")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def run():

    # ----- PYGAME LOOP -----
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handle left-click

            # Handle right-click

            # Handle space-bar

        # Draw

        # Update display
        pygame.display.flip()
        clock.tick(30)  # Limit to 30 frames per second


if __name__ == "__main__":
    run()
