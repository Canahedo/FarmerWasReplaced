def goto(coords = (0,0)):
	x, y = coords
	cx = get_pos_x()
	cy = get_pos_y()

	size = get_world_size()
	half = size / 2

	dx = (x - cx + half) % size - half
	dy = (y - cy + half) % size - half

	if dx > 0:
		x_dir = East
	else:
		x_dir = West

	if dy > 0:
		y_dir = North
	else:
		y_dir = South

	for i in range(abs(dx)):
		move(x_dir)

	for i in range(abs(dy)):
		move(y_dir)