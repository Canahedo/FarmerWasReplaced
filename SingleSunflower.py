import Utils
import Data


def run():
	move_list = [North, South]
	move_toggle = 0
	
	Data.map = []
	for i in range(9):
		Data.map.append([])
	
	for col in range(Data.size):
		for row in range(Data.size - 1):
			farm()
			move(move_list[move_toggle])
		farm()
		move(East)
		move_toggle = (move_toggle + 1) % 2
	
	clean_up()


def farm():
	if not Utils.ready_for_planting():
		return
	Utils.prep_ground(Entities.Sunflower)
	plant(Entities.Sunflower)
	Utils.water()
	level = measure() - 7
	Data.map[level].append((get_pos_x(), get_pos_y()))


def clean_up():
	for i in range(8, -1, -1):
		while len(Data.map[i]) > 0:
			coord = Data.map[i].pop(0)
			Utils.goto(coord)
			if can_harvest():
				harvest()
			else:
				Data.map[i].append(coord)