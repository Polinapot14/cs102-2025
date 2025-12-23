import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()

            self.draw_grid()
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        grid: Grid = []
        for _ in range(self.cell_height):
            row: Cells = []
            for _ in range(self.cell_width):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        for row in range(self.cell_height):
            for col in range(self.cell_width):
                color = (
                    pygame.Color("green")
                    if self.grid[row][col] == 1
                    else pygame.Color("white")
                )
                pygame.draw.rect(
                    self.screen,
                    color,
                    (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size),
                )

    def get_neighbours(self, cell: Cell) -> Cells:
        row, col = cell
        neighbours: Cells = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r = row + dr
                c = col + dc
                if 0 <= r < self.cell_height and 0 <= c < self.cell_width:
                    neighbours.append(self.grid[r][c])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid: Grid = []
        for row in range(self.cell_height):
            new_row: Cells = []
            for col in range(self.cell_width):
                neighbours = self.get_neighbours((row, col))
                alive_neighbours = sum(neighbours)
                if self.grid[row][col] == 1:
                    new_row.append(1 if alive_neighbours in (2, 3) else 0)
                else:
                    new_row.append(1 if alive_neighbours == 3 else 0)
            new_grid.append(new_row)
        return new_grid