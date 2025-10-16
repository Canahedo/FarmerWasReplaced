import Utils
import Cactus


def start(axis=0):
    global cactus_list
    global move_toggle
    global move_list
    size = get_world_size()

    if axis == 0:
        move_list = [North, South]
    else:
        move_list = [East, West]

    # Main loop
    for col in range(size):
        cactus_list = []
        move_toggle = 0

        # Plant a single column/row
        for row in range(size - 1):
            cactus_list.append(measure())
            if row > 0 and cactus_list[-2] > cactus_list[-1]:
                swap([South, West][axis])
                cactus_list.append(cactus_list.pop(-2))
            move(move_list[move_toggle])
        cactus_list.append(measure())

        # Sort that col/row
        sorted_list = Utils.get_sorted_list(cactus_list)
        while cactus_list != sorted_list:
            move_toggle = (move_toggle + 1) % 2
            move(move_list[move_toggle])
            if move_toggle == 1:
                plan = range(size - 2, 0, -1)
            else:
                plan = range(1, size - 1, 1)
            for pos in plan:
                cactus_sort(cactus_list, axis, pos)
                move(move_list[move_toggle])

        # next_row
        if axis == 0:
            Utils.goto([get_pos_x(), 0])
            move(East)
        else:
            Utils.goto([0, get_pos_y()])
            move(North)
    Utils.goto([0, 0])


def cactus_sort(cactus_list, axis, pos):
    a, b, c = cactus_list[pos - 1], cactus_list[pos], cactus_list[pos + 1]

    # If sorted
    if a <= b <= c:
        return

    # Low swap
    elif b == c < a or a == c > b or b < a < c or b < c < a:
        swap([South, West][axis])
        new_loc = pos - 1

    # High swap
    elif a == c < b or a == b > c or a < c < b or c < a < b or c < b < a:
        swap([North, East][axis])
        new_loc = pos + 1

    cactus_list.insert(new_loc, cactus_list.pop(pos))
    return cactus_sort(cactus_list, axis, pos)


Utils.goto([0, 0])
start()
start(1)
