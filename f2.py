def just_move():
    size = get_world_size()
    # Single full loop over farm
    move_toggle = 0
    move_list = [North, South]
    for col in range(size):
        for row in range(size - 1):
            move(move_list[move_toggle])
        move(East)
        move_toggle = (move_toggle + 1) % 2
