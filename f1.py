import Utils

dir_map = {North: South, East: West, South: North, West: East}


def find_edges(x, y, size):
    edge_map = {North: (y == size), East: (x == size), South: (y == 0), West: (x == 0)}
    edges = []
    for dir in dir_map:
        if edge_map[dir]:
            edges.append(dir)
    return edges
