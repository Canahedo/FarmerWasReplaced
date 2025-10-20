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
	harvest()


def farm():
	if get_entity_type() == Entities.Pumpkin:
		return
	if not Utils.ready_for_planting():
		return
	Utils.prep_ground(Entities.Pumpkin)
	plant(Entities.Pumpkin)
	Utils.water()
	Data.map.append((get_pos_x(), get_pos_y()))
		

# Checks tile for dead pumpkins and replants if needed
def check_pumpkin():
	pumpkin = get_entity_type()
	if pumpkin == Entities.Pumpkin and can_harvest():
		return True
	elif pumpkin in [Entities.Dead_Pumpkin, None]:
		plant(Entities.Pumpkin)
	Utils.water()
	return False


def clean_up():
	while len(Data.map) > 0:
		prospect = Data.map.pop(0)
		Utils.goto(prospect)
		if not check_pumpkin():
			Data.map.append(prospect)
