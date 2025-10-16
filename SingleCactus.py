import Utils
import Data


def setup():
    new_map = {}
    for x in range(Data.size):
        for y in range(Data.size):
            new_map[(x, y)] = None
    Data.map = new_map


def run():
    move_list = [North, South]
    move_toggle = 0
    for col in range(Data.size):
        for row in range(Data.size - 1):
            farm()
            move(move_list[move_toggle])
        farm()
        move(East)
        move_toggle = (move_toggle + 1) % 2


def farm():
    if Utils.ready_for_harvest() == False:
        return

    # Plant and record on map
    Utils.prep_ground(Entities.Cactus)
    plant(Entities.Cactus)
    coords = (get_pos_x(), get_pos_y())
    Data.map[coords] = measure()


def clean_up():
    pass
