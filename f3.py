import SingleCactus
import Data
import Utils


def a():
    new_map = {}
    for x in range(Data.size):
        for y in range(Data.size):
            new_map[(x, y)] = None
    Data.map = new_map


def b():
    move_list = [North, South]
    move_toggle = 0
    for col in range(Data.size):
        for row in range(Data.size - 1):
            c()
            move(move_list[move_toggle])
        c()
        move(East)
        move_toggle = (move_toggle + 1) % 2


def c():
    coords = (get_pos_x(), get_pos_y())
    Data.map[coords] = measure()


Utils.goto((0, 0))
Data.size = 10
a()
b()
SingleCactus.clean_up()
