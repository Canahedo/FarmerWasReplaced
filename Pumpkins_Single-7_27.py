# Success Condition: num_items(Items.Pumpkin) >= 10000000

# Travel to coordinate
# Accepts a tuple (x,y)
def goto(destination = (0,0)):
	movement(get_pos_x(), destination[0], East, West)
	movement(get_pos_y(), destination[1], North, South)
	
def movement(start, to, dir0, dir1):
	distance = abs(start - to)
	
	if start > to:
		if distance > 4:
			distance = (8 - start) + to
			dir = dir0
		else:
			dir = dir1
	else:
		if distance > 4:
			distance = (8 - to) + start
			dir = dir1
		else:	
			dir = dir0

	for i in range(distance):
		move(dir)

def second_pass():
	map = []
	tog = 0
	for col in range(8):	
		for row in range(7):
			if not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
				if get_water() < .25:	
					use_item(Items.Water)
				map.append((col,get_pos_y()))
			move([North, South][tog])
		if not can_harvest():
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
			if get_water() < .25:	
				use_item(Items.Water)
			map.append((col,get_pos_y()))
		move(East)
		tog = (tog + 1) % 2
	return map
		
def cleanup(map):
	for i in range(len(map)):
		goto(map.pop(0))
		while not can_harvest():
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
	
########################################################
move_toggle = 0

for col in range(8):	
	for row in range(7):
		till()
		plant(Entities.Pumpkin)
		move([North, South][move_toggle])
	till()
	plant(Entities.Pumpkin)
	move(East)
	move_toggle = (move_toggle + 1) % 2
cleanup(second_pass())
harvest()
goto()
	
while num_items(Items.Pumpkin) < 10000000:
	for col in range(8):	
		for row in range(7):
			plant(Entities.Pumpkin)
			move([North, South][move_toggle])
		plant(Entities.Pumpkin)
		move(East)
		move_toggle = (move_toggle + 1) % 2
	cleanup(second_pass())
	harvest()
	goto()

	