from Game import Game
from Map import Map


def game_random(steps: int = None):
    game = Game(Map(30))
    game.map.random()
    game.map.show()

    if steps is None:
        game.start()
    else:
        game.start(steps)


def game_1(steps: int = None):
    game = Game("patterns/map1.json")
    game.map.show()

    if steps is None:
        game.start()
    else:
        game.start(steps)


def game_2(steps: int = None):
    game = Game("patterns/map2.json")
    game.map.show()

    if steps is None:
        game.start()
    else:
        game.start(steps)


def game_3(steps: int = None):
    game = Game("patterns/map3.json")
    game.map.show()

    if steps is None:
        game.start()
    else:
        game.start(steps)


# game = Game("patterns/pulsar.json")
# game.map.show()
# game.start()

game_random()
