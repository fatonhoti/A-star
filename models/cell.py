import pygame
from settings import *


class Cell:
    def __init__(self, screen, row, col):
        self.screen = screen
        self.row = row
        self.col = col
        self.color = WHITE

    def __repr__(self):
        return f"({self.row}, {self.col}), color={self.color}, {hex(id(self))}"

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return (self.screen, self.row, self.col, self.color) == (
            other.screen,
            other.row,
            other.col,
            other.color,
        )

    def __lt__(self, other):
        return False

    def neighbours(self, grid):
        neighbours = []

        r = self.row
        c = self.col

        starting_row = r if (r - 1) < 0 else r - 1
        ending_row = r + 1 if (r + 1) < grid.matrix_dims[0] else r

        starting_col = c if (c - 1) < 0 else c - 1
        ending_col = c + 1 if (c + 1) < grid.matrix_dims[1] else c

        for row in range(starting_row, ending_row + 1):
            for col in range(starting_col, ending_col + 1):
                if (col, row) != (c, r) and grid.cells[row][col].color is not BLACK:
                    neighbours.append(grid.cells[row][col])

        return neighbours

    def draw(self):
        if self.color is not WHITE:
            pygame.draw.rect(
                self.screen,
                self.color,
                (self.row * CELL_SIZE, self.col * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
        else:
            pygame.draw.rect(
                self.screen,
                self.color,
                (
                    self.row * CELL_SIZE + 1,
                    self.col * CELL_SIZE + 1,
                    CELL_SIZE - 1,
                    CELL_SIZE - 1,
                ),
            )

    def make_wall(self):
        self.color = BLACK

    def make_start(self):
        self.color = TURQUOISE

    def make_end(self):
        self.color = ORANGE

    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_solution(self):
        self.color = PURPLE

    def reset(self):
        self.color = WHITE

    def get_pos(self):
        return self.row, self.col
