from math import inf, sqrt
from queue import PriorityQueue
from sys import exit

import pygame

from models.grid import Grid
from settings import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_caption("Path Finding Algorithm")
pygame.display.set_icon(icon)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def draw(grid):
    # Draw
    grid.draw()

    # Draw the individual cells
    grid.draw_cells()

    # Update display
    pygame.display.flip()
    clock.tick(FPS)


def d(cell, goal_cell):
    (x1, y1) = cell.get_pos()
    (x2, y2) = goal_cell.get_pos()
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, grid):
    # total_path = [current]
    current.make_solution()
    while current in came_from.keys():

        current = came_from[current]  # Step back
        current.make_solution()
        # total_path.insert(0, current)

        draw(grid)

    # return total_path


def a_star(grid):

    start_cell = grid.start_cell
    end_cell = grid.end_cell

    # ----- START OF THE A* ALGORITHM -----

    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    open_set = PriorityQueue()
    open_set.put((d(start_cell, end_cell), 0, start_cell))

    # The nodes that have already been considered
    closed_set = set()

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    came_from = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    g_score = {cell: inf for row in grid.cells for cell in row}
    g_score[start_cell] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    f_score = {cell: inf for row in grid.cells for cell in row}
    f_score[start_cell] = g_score[start_cell] + d(start_cell, end_cell)

    while open_set.qsize() > 0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current = open_set.get()[2]
        closed_set.add(current)

        if current == end_cell:
            reconstruct_path(came_from, current, grid)
            return

        if current != start_cell:
            current.make_closed()

        for neighbour in current.neighbours(grid):
            if neighbour in closed_set:
                continue

            # d(current,neighbour) is the weight of the edge from current to neighbour
            # tentative_gScore is the distance from start to the neighbour through current
            tentative_g_score = g_score[current] + d(current, neighbour)
            if tentative_g_score < g_score[neighbour]:
                # This path to neighbour is better than any previous one. Record it!
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + d(neighbour, end_cell)
                if neighbour not in list(map(lambda x: x[2], open_set.queue)):
                    open_set.put(
                        (d(neighbour, end_cell), f_score[neighbour], neighbour)
                    )
                    neighbour.make_open()

        draw(grid)


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
                    elif grid.end_cell is None and grid.start_cell is not None:
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
                if (
                    event.key == pygame.K_SPACE
                    and grid.start_cell is not None
                    and grid.end_cell is not None
                ):
                    a_star(grid)

                # Clear board
                if event.key == pygame.K_c:
                    grid.reset()

        draw(grid)


if __name__ == "__main__":
    run()
