#321677
def goto(destination = (0,0)):
	movement(get_pos_x(), destination[0], East, West)
	movement(get_pos_y(), destination[1], North, South)
	
def movement(start, to, dir0, dir1):
	size = get_world_size()
	distance = abs(start - to)
	
	if start > to:
		if distance > size / 2:
			distance = (size - start) + to
			dir = dir0
		else:
			dir = dir1
	else:
		if distance > size / 2:
			distance = (size - to) + start
			dir = dir1
		else:	
			dir = dir0

	for i in range(distance):
		move(dir)