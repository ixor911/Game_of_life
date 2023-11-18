from multipledispatch import dispatch
from Cell import Cell
import json
import random

class Map:
    @dispatch()
    def __init__(self):
        self.map = []

    @dispatch(int)
    def __init__(self, n):
        self.map = []
        for i in range(n):
            line = []

            for j in range(n):
                line.append(Cell())

            self.map.append(line)

    @dispatch(int, int)
    def __init__(self, x, y):
        self.map = []
        for i in range(x):
            line = []

            for j in range(y):
                line.append(Cell())

            self.map.append(line)

    @dispatch(str)
    def __init__(self, fp: str):
        self.load(fp)

    def random(self):
        for line in self.map:
            for cell in line:
                if random.randint(0, 1) == 0:
                    cell.set_dead()
                else:
                    cell.set_alive()

    def load(self, fp: str):
        try:
            data: dict = json.load(open(fp))
            if "map" not in data.keys():
                raise ValueError

            self.map = []
            for data_line in data['map']:
                line = []

                for item in data_line:
                    if item == 0:
                        line.append(Cell(False))
                    elif item == 1:
                        line.append(Cell(True))
                    else:
                        raise ValueError

                self.map.append(line)

        except FileNotFoundError:
            print("File was not found!")
        except ValueError:
            print("There is value error in file!")
        except Exception as err:
            print(err)

    def show(self):
        for line in self.map:
            line_str = ""
            for cell in line:
                line_str += f"{cell} "
            print(line_str)
        print()

    def cell(self, x, y) -> Cell:
        return self.map[x][y]

    def set(self, map: list):
        self.map = map
