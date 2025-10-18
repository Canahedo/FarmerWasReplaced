import Utils
import Data


def setup():
	Data.map = []
	# Data.size = 6


def run():
	move_toggle = 0
	move_list = [North, South]
	for col in range(Data.size):
		for n in range(2):
			for row in range(Data.size - 1):
				farm(n)
				move(move_list[move_toggle])
		move(move_list[move_toggle])
		farm(0)
		move(East)
		move_toggle = (move_toggle + 1) % 2


def farm(n):
	coords = (get_pos_x(), get_pos_y())

	# First Pass
	if n == 0:
		Data.map.append(coords)
		if Utils.ready_for_harvest():
			Utils.prep_ground(Entities.Pumpkin)
			plant(Entities.Pumpkin)

	# Second Pass
	elif n == 1 and check_pumpkin():
		Data.map.remove(coords)


# Checks tile for dead pumpkins and replants if needed
def check_pumpkin():
	pumpkin = get_entity_type()
	if pumpkin == Entities.Pumpkin and can_harvest():
		return True
	elif pumpkin in [Entities.Dead_Pumpkin, None]:
		plant(Entities.Pumpkin)
	return False


def clean_up():
	while len(Data.map) > 0:
		prospect = Data.map.pop(0)
		Utils.goto(prospect)
		if check_pumpkin():
			continue
		Data.map.append(prospect)
		if len(Data.map) == 1:
			use_item(Items.Fertilizer)
