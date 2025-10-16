map = {}
size = 10

#####################################################################


# Translate map to list matrix from dict
def get_sliced_map():

    # Create blank list matrix
    matrix = []
    for col in range(size):
        matrix.append([])
        for row in range(size):
            matrix[col].append([])

    # Sort map points into slice matrix
    for point in map:
        (x, y) = point
        matrix[x].pop(y)
        matrix[x].insert(y, map[point])
    return matrix


# Build package to be sorted
def slice_packager(slices, index):
    # Prevents trying to sort edge slices
    edges = {0: 1, size: -1}
    if index in edges:
        index += edges[index]
    # Package contains indexed slice and both neighbors
    pkg = []
    for i in [-1, 0, 1]:
        pkg.append(slices[index + i])
    return pkg, index


def goto(coords):
    x, y = coords[1], coords[2]


def package_sorter(raw):
    new = [[], [], []]

    # Check one chunk at a time
    for i in range(len(raw[0])):
        a, b, c = raw[0][i], raw[1][i], raw[2][i]

        # Sort chunk
        while not (a <= b <= c):

            # Low swap
            if b == c < a or a == c > b or b < a < c or b < c < a:
                a, b = b, a
                swap(West)

            # High swap
            elif a == c < b or a == b > c or a < c < b or c < a < b or c < b < a:
                b, c = c, b
                swap(East)

        # Add to new package
        x = {0: a, 1: b, 2: c}
        for j in x:
            new[j].append(x[j])

    return new


def update_map(position, sorted_pkg):
    pkg_indexs = [position - 1, position, position + 1]
    for i in range(3):
        for j in range(len(sorted_pkg[0])):
            map[(pkg_indexs[i], j)] = sorted_pkg[i][j]


####################################################################

slices = get_sliced_map()
for i in range(len(slices)):
    pkg, slice_index = slice_packager(slices, i)
    goto((slice_index, 0))
    sorted_pkg = package_sorter(pkg)
    if sorted_pkg != pkg:
        update_map(slice_index, sorted_pkg)
