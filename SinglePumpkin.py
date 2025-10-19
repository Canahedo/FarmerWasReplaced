import Utils
import Data


def run():
	Data.map = []
	for col in range(Data.size):	
		for row in range(Data.size):
			farm()
			move(North)
		clean_up()
		move(East)


def farm():
	coords = (get_pos_x(), get_pos_y())
	Data.map.append(coords)
	if Utils.ready_for_harvest():
		Utils.prep_ground(Entities.Pumpkin)
		plant(Entities.Pumpkin)


# Checks tile for dead pumpkins and replants if needed
def check_pumpkin():
	pumpkin = get_entity_type()
	if pumpkin == Entities.Pumpkin and can_harvest():
		return True
	if pumpkin in [Entities.Dead_Pumpkin, None]:
		plant(Entities.Pumpkin)
	if num_items(Items.Water) > 0 and get_water() < Data.water:
		use_item(Items.Water)
	return False


def clean_up():
	while len(Data.map) > 0:
		prospect = Data.map.pop(0)
		Utils.goto(prospect)
		if not check_pumpkin():
			Data.map.append(prospect)
