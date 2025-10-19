import Utils
import Data


def setup():
	Data.map = []
	for i in range(9):
		Data.map.append([])


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
	Utils.prep_ground(Entities.Sunflower)
	plant(Entities.Sunflower)
	level = measure() - 7
	Data.map[level].append((get_pos_x(), get_pos_y()))


def clean_up():
	cut_off = 0.25  # Drone will give up with this % remaining
	start_total = count_flowers(Data.map)
	for i in range(8, -1, -1):
		while len(Data.map[i]) > 1:
			coord = Data.map[i].pop(0)
			quick_print(coord)
			Utils.goto(coord)
			while can_harvest() == False:
				do_a_flip()
			harvest()
		# Stops harvesting after collecting 75% of flowers
		if start_total * cut_off > count_flowers(Data.map):
			return


# Counts how many flowers remain
def count_flowers(map):
	sum = 0
	for list in map:
		sum += len(list)
	return sum
