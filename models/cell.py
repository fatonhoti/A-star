import pygame
from settings import *


class Cell:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = WHITE
        self.edge_cell = False

    def draw(self):
        if self.edge_cell:
            pygame.draw.rect(
                self.screen,
                self.color,
                (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
        elif self.color is not WHITE:
            pygame.draw.rect(
                self.screen,
                self.color,
                (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
        else:
            pygame.draw.rect(
                self.screen,
                self.color,
                (
                    self.x * CELL_SIZE + 1,
                    self.y * CELL_SIZE + 1,
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

    def reset(self):
        self.color = WHITE

    def get_pos(self):
        return self.x, self.y
