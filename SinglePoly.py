import Utils
import Data


def run():
	Data.map = {}
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
	if Utils.ready_for_harvest() == False:
		return
	
	# Decide what to plant
	x, y = get_pos_x(), get_pos_y()
	if (x, y) in Data.map:
		to_plant = Data.map[(x,y)]
		
	#If farm is large enough, can run w/ only tree
	elif Data.crop == Entities.Tree and Data.size <= 20:
		Data.tree_toggle = (Data.tree_toggle + 1) % 2
		wood_list = [Entities.Bush, Entities.Tree]
		to_plant = wood_list[Data.tree_toggle]
	
	else:
		to_plant = Data.crop

	Utils.prep_ground(to_plant)
	plant(to_plant)

	# Record new companion
	(comp_crop, comp_position) = get_companion()
	if comp_position not in Data.map:
		Data.map[comp_position] = comp_crop