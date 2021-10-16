from random import choice, uniform

import pygame
from settings import *

from .cell import Cell


class Grid:
    def __init__(self, screen):
        self.screen = screen
        self.matrix_dims = (SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)
        self.cells = None
        self.start_cell = None
        self.end_cell = None

    def create(self):
        sparsity = 0.3  # 1 in 3 cells will be walls.
        """
        Generate a random matrix of empty cells and wall-cells.
        :return: Nothing
        """
        self.cells = []
        amount_of_cells = SCREEN_WIDTH // CELL_SIZE
        for i in range(amount_of_cells):
            row = []
            for j in range(amount_of_cells):
                cell = Cell(self.screen, i, j)
                row.append(cell)
                if uniform(0, 1) < sparsity:
                    cell.make_wall()
            self.cells.append(row)

        # Pick the start- and end cell at random
        flattened_cells = [c for row in self.cells for c in row]
        empty_cells = list(filter(lambda x: x.color == WHITE, flattened_cells))

        start_cell = choice(empty_cells)
        start_cell.make_start()
        self.start_cell = start_cell
        empty_cells.remove(start_cell)

        end_cell = choice(empty_cells)
        end_cell.make_end()
        self.end_cell = end_cell

    def draw(self):
        """
        Draws gridlines on the screen to form a matrix.
        :return: Nothing
        """
        # Clear screen
        self.screen.fill(WHITE)

        rows, cols = self.matrix_dims

        # Draw horizontal lines
        for y in range(0, rows):
            pygame.draw.line(
                self.screen,
                BLACK,
                (0, y * CELL_SIZE),
                (SCREEN_WIDTH, y * CELL_SIZE),
                1,
            )

        # Draw vertical lines
        for x in range(0, cols):
            pygame.draw.line(
                self.screen,
                GREY,
                (x * CELL_SIZE, 0),
                (x * CELL_SIZE, SCREEN_HEIGHT),
                1,
            )

    def draw_cells(self):
        for row in self.cells:
            for cell in row:
                cell.draw()

    def get_cell(self, row, col):
        return self.cells[row][col]

    def reset(self):
        """
        Resets the grid.
        :return: Nothing
        """
        self.start_cell = None
        self.end_cell = None
        self.create()
