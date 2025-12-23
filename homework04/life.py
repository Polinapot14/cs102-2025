import pathlib
import random
import typing as tp

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[int] = None,
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = self.create_grid()
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_generations = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid: Grid = []
        for _ in range(self.rows):
            row: Cells = []
            for _ in range(self.cols):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        row, col = cell
        neighbours: Cells = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r = row + dr
                c = col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    neighbours.append(self.curr_generation[r][c])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid: Grid = []
        for row in range(self.rows):
            new_row: Cells = []
            for col in range(self.cols):
                neighbours = self.get_neighbours((row, col))
                alive_neighbours = sum(neighbours)
                if self.curr_generation[row][col] == 1:
                    new_row.append(1 if alive_neighbours in (2, 3) else 0)
                else:
                    new_row.append(1 if alive_neighbours == 3 else 0)
            new_grid.append(new_row)
        return new_grid

    def step(self) -> None:
        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        if self.max_generations is None:
            return False
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        grid: Grid = [[int(ch) for ch in line] for line in lines]
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        game = GameOfLife((rows, cols), randomize=False)
        game.curr_generation = grid
        game.prev_generation = game.create_grid(randomize=False)
        game.generations = 1
        return game

    def save(self, filename: pathlib.Path) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            for row in self.curr_generation:
                f.write("".join(map(str, row)) + "\n")
