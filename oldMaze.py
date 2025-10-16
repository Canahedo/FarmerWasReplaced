import Utils

maze_map = {}


def start():
    global maze_map
    size = 5  # get_world_size()
    maze_map = {}

    # Single full loop over farm
    move_toggle = 0
    move_list = [North, South]
    for col in range(size):
        for row in range(size - 1):
            prep_maze()
            move(move_list[move_toggle])
        prep_maze()
        move(East)
        move_toggle = (move_toggle + 1) % 2
    substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


# Run on each tile
def prep_maze():
    global maze_map
    if Utils.ready_for_harvest() == False:
        return
    Utils.prep_ground(Entities.Bush)
    plant(Entities.Bush)
    coords = (get_pos_x(), get_pos_y())
    maze_map[coords] = None
