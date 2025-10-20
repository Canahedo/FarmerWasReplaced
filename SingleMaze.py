import Utils
import Data
import MR


def setup():	
	Data.map = {}	
	for col in range(Data.size):
		for row in range(Data.size):
			Data.map[(get_pos_x(), get_pos_y())] = {}
	harvest()
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	while num_items(Items.Weird_Substance) < substance * 300:
		plant(Entities.Tree)
		while not can_harvest():
			use_item(Items.Fertilizer)
		harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance)


def farm():
	Data.map[(get_pos_x(), get_pos_y())] = {}
	if get_entity_type() == Entities.Bush:
		return
	harvest()
	plant(Entities.bush)
	Utils.water()
	
	
def just_map():
	Data.map = {}	
	for col in range(Data.size):
		for row in range(Data.size - 1):
			Data.map[(get_pos_x(), get_pos_y())] = {}
			
	
def run():
	while get_entity_type() != Entities.Treasure:
		if can_move(MR.dirs[MR.hand]):
			move(MR.dirs[MR.hand])
			turn("right")
		elif can_move(MR.dirs[MR.face]):
			move(MR.dirs[MR.face])
		elif can_move(MR.dirs[MR.off_hand]):
			move(MR.dirs[MR.off_hand])
			turn("left")
		elif can_move(MR.dirs[MR.back]):
			move(MR.dirs[MR.back])
			turn("around")
	harvest()
		
	
def turn(dir): # "right", "around", or "left"
	if dir == "right":
		turn = 1
	elif dir == "around":
		turn = 2
	elif dir == "left":
		turn = 3
	MR.face = (MR.face + turn) % 4
	MR.hand = (MR.hand + turn) % 4
	MR.back = (MR.back + turn) % 4
	MR.off_hand = (MR.off_hand + turn) % 4