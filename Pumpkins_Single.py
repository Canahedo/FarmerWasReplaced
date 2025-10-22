# Success Condition: num_items(Items.Pumpkin) >= 10000000

# Travel to coordinate
# Accepts a tuple (x,y)
def goto(destination = (0,0)):

	x = [get_pos_x(), destination[0], [East, West]]
	y = [get_pos_y(), destination[1], [North, South]]
			
	for i in [x, y]:
		start = i[0]
		to = i[1]
		
		# Toggles direction if "to" is West/South of "start"
		if start > to:
			toggle = 1
		else:
			toggle = 0
		
		# Direct path is shorter
		distance = abs(start - to)
		if distance <= 4:
			for j in range(distance):
				move(i[2][toggle])
			
		# Warp is shorter, toggle direction
		else:
			distance = 8 - start + to
			toggle = (toggle + 1) % 2
			for j in range(distance):
				move(i[2][toggle])

move_toggle = 0

map = []
for col in range(8):	
	for row in range(7):
		till()
		plant(Entities.Pumpkin)
		map.append((get_pos_x(), get_pos_y()))
		move([North, South][move_toggle])
	till()
	plant(Entities.Pumpkin)
	map.append((get_pos_x(), get_pos_y()))
	move(East)
	move_toggle = (move_toggle + 1) % 2
while len(map) > 0:
	prospect = map.pop(0)
	goto(prospect)
	if get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)
	if not can_harvest():
		use_item(Items.Water)
		map.append(prospect)
harvest()
goto()
	
while True:
	if num_items(Items.Pumpkin) >= 10000000:
		break

	for col in range(8):	
		for row in range(7):
			plant(Entities.Pumpkin)
			map.append((get_pos_x(), get_pos_y()))
			move([North, South][move_toggle])
		plant(Entities.Pumpkin)
		map.append((get_pos_x(), get_pos_y()))
		move(East)
		move_toggle = (move_toggle + 1) % 2
	while len(map) > 0:
		prospect = map.pop(0)
		goto(prospect)
		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
		if not can_harvest():
			use_item(Items.Water)
			map.append(prospect)
	harvest()
	goto()