from termcolor import colored


class Cell:
    def __init__(self, alive: bool = False):
        self.__alive: bool = alive

    def __str__(self):
        return colored("1", 'dark_grey') if self.__alive else colored("0", 'white')

    def set_alive(self):
        self.__alive = True

    def set_dead(self):
        self.__alive = False

    @property
    def alive(self):
        return self.__alive
