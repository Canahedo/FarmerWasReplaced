import Utils
import Data


def setup():
	change_hat(Hats.Dinosaur_Hat)
	Data.apple = measure()
	

def run():
	move(North)
	move_list = [North, South]
	move_toggle = 0
	for col in range(Data.size):
		for row in range(Data.size - 2):
			farm()
			move(move_list[move_toggle])
		farm()
		move(East)
		move_toggle = (move_toggle + 1) % 2
	move(South)
	for i in range(Data.size):
		move(West)
	

def farm():
	if get_entity_type() == Entities.Apple:
		Data.apple = (measure())
		quick_print(Data.apple)
		
def single():
	x, y = Data.apple[0], Data.apple[1]
	for i in range(y):
		move(North)
	for i in range(x):
		move(East)
		Data.apple = measure()
	for i in range(y):
		move(South)
	for i in range(x):
		move(West)


