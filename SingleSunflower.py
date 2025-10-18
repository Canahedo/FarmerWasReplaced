import Utils
import Data


def setup():
	new_map = []
	for i in range(9):
		new_map.append([])
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
	if Utils.ready_for_harvest() == False:
		return

	# Plant and record on map
	Utils.prep_ground(Entities.Sunflower)
	plant(Entities.Sunflower)
	level = measure() - 7
	coords = (get_pos_x(), get_pos_y())
	Data.map[level].append(coords)


def clean_up():
	cut_off = 0.25  # Drone will give up with this % remaining
	start_total = count_flowers(Data.map)
	for i in range(8, -1, -1):
		for coord in Data.map[i]:
			Utils.goto(coord)
			while can_harvest() == False:
				do_a_flip()
			harvest()
		Data.map[i] = []

		# Stops harvesting after collecting 75% of flowers
		if start_total * cut_off > count_flowers(Data.map):
			return


# Counts how many flowers remain
def count_flowers(map):
	sum = 0
	for list in map:
		sum += len(list)
	return sum
