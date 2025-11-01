def goto(coords = (0,0)):
	x, y = coords
	cx = get_pos_x()
	cy = get_pos_y()
	ws = get_world_size()
	
	xp = abs(ws + x - cx) % ws
	xr = abs(-ws + x - cx) % ws
	yp = abs(ws + y - cy) % ws
	yr = abs(-ws + y - cy) % ws
	
	if xp < xr:
		for _ in range(0, xp):
			move(East)
	elif xp > xr:
		for _ in range(0, xr):
			move(West)
	if yp < yr:
		for _ in range(0, yp):
			move(North)
	elif yp > yr:
		for _ in range(0, yr):
			move(South)
			
##############
