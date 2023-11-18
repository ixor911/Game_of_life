from multipledispatch import dispatch
from Cell import Cell
from Map import Map
import time
import os


clear = lambda: os.system("cls")
wait_time = 0.2


class Game:
    @dispatch()
    def __init__(self):
        self.map = Map()

    @dispatch(Map)
    def __init__(self, map: Map):
        self.map = map

    @dispatch(str)
    def __init__(self, fp: str):
        self.map = Map(fp)

    def check_cell(self, x: int, y: int):
        try:
            cell: Cell = self.map.map[x][y]
            return cell.alive
        except Exception:
            return False

    def neighbours(self, x: int, y: int):
        neighbours = [
            self.check_cell(x - 1, y - 1),
            self.check_cell(x, y - 1),
            self.check_cell(x + 1, y - 1),
            self.check_cell(x + 1, y),
            self.check_cell(x + 1, y + 1),
            self.check_cell(x, y + 1),
            self.check_cell(x - 1, y + 1),
            self.check_cell(x - 1, y)
        ]

        lives = len([item for item in neighbours if item])
        return lives

    def step(self, x: int, y: int) -> bool:
        try:
            cell = self.map.cell(x, y)
        except Exception as err:
            print(err)
            return False

        lives = self.neighbours(x, y)

        if cell.alive and lives < 2:
            return False
        elif cell.alive and 2 <= lives <= 3:
            return True
        elif cell.alive and 3 < lives:
            return False
        elif not cell.alive and lives == 3:
            return True

    def generation(self):
        new_map = []
        for x in range(0, len(self.map.map)):
            line = []
            for y in range(0, len(self.map.map[x])):
                if self.step(x, y):
                    line.append(Cell(True))
                else:
                    line.append(Cell(False))
            new_map.append(line)
        self.map.set(new_map)

    def after_gen(self):
        clear()
        self.map.show()
        time.sleep(wait_time)

    @dispatch(int)
    def start(self, steps: int):
        for i in range(steps):
            self.generation()
            self.after_gen()

    @dispatch()
    def start(self):
        while True:
            self.generation()
            self.after_gen()
