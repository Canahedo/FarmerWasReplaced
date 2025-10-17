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


# Translate map to list matrix from dict
def get_sliced_map(vert):
    # Create blank list matrix
    matrix = []
    for col in range(Data.size):
        matrix.append([])
        for row in range(Data.size):
            matrix[col].append([])
    # Sort map points into slice matrix
    for point in Data.map:
        if vert:
            (x, y) = point
        else:
            (y, x) = point
        matrix[x].pop(y)
        matrix[x].insert(y, Data.map[point])
    return matrix


def get_sorted_slices(vert):
    turned_slices = []
    sorted_slices = []
    for slice in get_sliced_map(not vert):
        turned_slices.append(Utils.get_sorted_list(slice))
    for i in range(Data.size):
        sorted_slices.append([])
        for j in range(Data.size):
            sorted_slices[i].append(turned_slices[j].pop(0))
    return sorted_slices


# Build package to be sorted
def slice_packager(slices, index):
    # Prevents trying to sort edge slices
    if index <= 0:
        index = 1
    elif index >= Data.size - 1:
        index = Data.size - 2
    # Package contains indexed slice and both neighbors
    pkg = []
    for i in [-1, 0, 1]:
        pkg.append(slices[index + i])
    return pkg, index


def package_sorter(unsorted, slice_index):
    new = [[], [], []]
    sorted = True
    # Check one chunk at a time
    for i in range(len(unsorted[0])):
        a, b, c = unsorted[0][i], unsorted[1][i], unsorted[2][i]
        # Sort chunk
        while not (a <= b <= c):
            sorted = False
            Utils.goto((slice_index, i))
            # Low swap
            if (b == c < a) or (a == c > b) or (b < a < c) or (b < c < a):
                a, b = b, a
                swap(West)
            # High swap
            elif (
                (a == c < b)
                or (a == b > c)
                or (a < c < b)
                or (c < a < b)
                or (c < b < a)
            ):
                b, c = c, b
                swap(East)
        # Add to new package
        x = {0: a, 1: b, 2: c}
        for j in x:
            new[j].append(x[j])
    if sorted == False:
        package_sorter(new, slice_index)
    return new


def update_map(slices, position, sorted_pkg):
    pkg_indexs = [position - 1, position, position + 1]
    for i in range(3):
        slices[pkg_indexs[i]] = sorted_pkg[i]
        for j in range(len(sorted_pkg[0])):
            Data.map[(pkg_indexs[i], j)] = sorted_pkg[i][j]
    return slices


def sort_loop(slices, mode):
    plans = [range(1, Data.size - 1, 1), range(Data.size - 2, 0, -1)]
    if mode == 3:
        plan = plans[(random() * 100 // 1) % 2]
    else:
        plan = plans[mode]
    for i in plan:
        pkg, slice_index = slice_packager(slices, i)
        sorted_pkg = package_sorter(pkg, slice_index)
        if sorted_pkg != pkg:
            slices = update_map(slices, slice_index, sorted_pkg)
            if mode == 3:
                return slices
    return slices


def clean_up(vert=True):
    slices = get_sliced_map(vert)
    sorted_slices = get_sorted_slices(vert)
    sort_loop(slices, 0)
    sort_loop(slices, 1)
    while slices != sorted_slices:
        slices = sort_loop(slices, False)
