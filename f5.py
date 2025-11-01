#322277
def goto(destination = (0,0)):
	movement(get_pos_x(), destination[0], [East, West])
	movement(get_pos_y(), destination[1], [North, South])
	
def movement(start, to, dirs):
	size = get_world_size()
	distance = abs(start - to)
	
	if start > to:
		if distance > size / 2:
			distance = (size - start) + to
			dir = dirs[0]
		else:
			dir = dirs[1]
	else:
		if distance > size / 2:
			distance = (size - to) + start
			dir = dirs[1]
		else:	
			dir = dirs[0]

	for j in range(distance):
		move(dir)