import pygame
from settings import *

from cell import Cell


class Grid:
    def __init__(self, screen):
        self.screen = screen
        self.matrix_dims = (SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)
        self.grid = []
        self.start_cell = None
        self.end_cell = None

    def create(self):
        grid = []
        amount_of_cells = SCREEN_WIDTH // CELL_SIZE
        for x in range(amount_of_cells):
            row = []
            for y in range(amount_of_cells):
                cell = Cell(self.screen, x, y)
                if (
                    x == 0
                    or x == amount_of_cells - 1
                    or y == 0
                    or y == amount_of_cells - 1
                ):
                    cell.edge_cell = True
                    cell.make_wall()
                row.append(cell)
            grid.append(row)
        self.grid = grid

    def draw(self):
        # Clear screen
        self.screen.fill(WHITE)

        rows, cols = self.matrix_dims

        # Draw horizontal lines
        for y in range(0, rows):
            pygame.draw.line(
                self.screen,
                BLACK,
                (CELL_SIZE, y * CELL_SIZE - CELL_SIZE),
                (SCREEN_WIDTH - CELL_SIZE, y * CELL_SIZE - CELL_SIZE),
                1,
            )

        # Draw vertical lines
        for x in range(0, cols):
            pygame.draw.line(
                self.screen,
                GREY,
                (x * CELL_SIZE - CELL_SIZE, CELL_SIZE),
                (x * CELL_SIZE - CELL_SIZE, SCREEN_HEIGHT - CELL_SIZE),
                1,
            )

    def draw_cells(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def get_cell(self, row, col):
        return self.grid[row][col]

    def reset(self):
        self.start_cell = None
        self.end_cell = None
        self.create()
