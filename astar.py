from sys import exit

from models.grid import Grid
from settings import *

import pygame

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_caption("")
pygame.display.set_icon(icon)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def run():

    grid = Grid(SCREEN)
    grid.create()

    # ----- PYGAME LOOP -----
    while True:

        # ----- Event handler -----
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Get the cell that was clicked
                x, y = pygame.mouse.get_pos()
                row, col = x // CELL_SIZE, y // CELL_SIZE
                cell = grid.get_cell(row, col)

                if event.button == LEFT_CLICK:

                    # Create a start_cell if it does not exist
                    if grid.start_cell is None:
                        grid.start_cell = cell
                        cell.make_start()

                    # Create an end_cell if it does not exist but a start_cell exists
                    elif grid.start_cell is not None and grid.end_cell is None:
                        grid.end_cell = cell
                        cell.make_end()
                    else:
                        # Make sure so to not overwrite the start and end cells
                        if cell not in [grid.start_cell, grid.end_cell]:
                            cell.make_wall()

                # Clear the clicked cell
                if event.button == RIGHT_CLICK:
                    if cell is grid.start_cell:
                        grid.start_cell = None
                    elif cell is grid.end_cell:
                        grid.end_cell = None
                    cell.reset()

            # Handle space-bar (START A* algorithm)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

                # Clear board
                if event.key == pygame.K_c:
                    grid.reset()

        # Draw
        grid.draw()

        # Draw the individual cells
        grid.draw_cells()

        # Update display
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    run()
