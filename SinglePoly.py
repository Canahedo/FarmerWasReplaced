import Utils
import Data


def setup():
	new_map = {}
	for x in range(Data.size):
		for y in range(Data.size):
			new_map[(x, y)] = None
	Data.map = new_map


def run():
	move_list = [North, South]
	move_toggle = 0
	for col in range(Data.size):
		for row in range(Data.size - 1):
			farm()
			move(move_list[move_toggle])
		farm()
		move(East)
		move_toggle = (move_toggle + 1) % 2


def farm():
	Data.tree_toggle = (Data.tree_toggle + 1) % 2
	if Utils.ready_for_harvest() == False:
		return

	# Decide what to plant
	x, y = get_pos_x(), get_pos_y()
	map_crop = Data.map[(x, y)]
	if map_crop:
		to_plant = map_crop
	elif Data.crop == Entities.Tree:
		wood_list = [Entities.Tree, Entities.Tree]
		#wood_list = [Entities.Bush, Entities.Tree]
		to_plant = wood_list[Data.tree_toggle]
	else:
		to_plant = Data.crop

	Utils.prep_ground(to_plant)
	plant(to_plant)

	# Record new companion
	(comp_crop, comp_position) = get_companion()
	Data.map[comp_position] = comp_crop
