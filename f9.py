#321406
def goto(target_coords):
	x1 = get_pos_x()
	y1 = get_pos_y()
	x2, y2 = target_coords
	world_size = get_world_size()
	world_half = world_size / 2

	dx = (x2 - x1 + world_half) % world_size - world_half
	dy = (y2 - y1 + world_half) % world_size - world_half

	if dx > 0:
		x_dir = East
	else:
		x_dir = West

	if dy > 0:
		y_dir = North
	else:
		y_dir = South

	adx = abs(dx)
	for i in range(adx):
		move(x_dir)

	ady = abs(dy)
	for i in range(ady):
		move(y_dir)