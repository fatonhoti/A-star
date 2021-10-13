from settings import *
import pygame


class Grid:

    def __init__(self, screen, screen_size, cell_size):
        self.screen = screen
        self.screen_size = screen_size
        self.cell_Size = cell_size
        self.matrix_dims = (self.screen_size[0] // cell_size, self.screen_size[1] // cell_size)
        self.grid = self.create_grid()

    def create_grid(self):
        grid = []
        cell_size = 10
        amount_of_cells = self.screen_size[0] // cell_size
        for x in range(amount_of_cells):
            row = []
            for y in range(amount_of_cells):
                row.append((x, y))
            self.grid.append(row)
        return grid

    def draw(self):
        rows, cols = self.matrix_dims
        for x in range(cols):
            for y in range(rows):
                pygame.draw.line(self.screen, BLACK, )
