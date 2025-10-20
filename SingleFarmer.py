import Utils
import Data
import SinglePoly
import SingleSunflower
import SinglePumpkin
import SingleCactus
import SingleMaze
import SingleSnake


def poly():
	SinglePoly.run()


def pumpkin():
	SinglePumpkin.run()


def sunflower():
	SingleSunflower.run()


def cactus():
	SingleCactus.run()


def maze():
	if get_entity_type() not in [Entities.Treasure, Entities.Hedge]:
		SingleMaze.setup()
	else:
		SingleMaze.just_map()
	SingleMaze.run()
	

def snake():
	SingleSnake.setup()


def run():
	for plant in plant_types:
		if Data.crop in plant_types[plant]:
			plant()


plant_types = {
	poly: [Entities.Grass, Entities.Tree, Entities.Carrot],
	pumpkin: [Entities.Pumpkin],
	sunflower: [Entities.Sunflower],
	cactus: [Entities.Cactus],
	maze: [Entities.Treasure],
	snake: [Entities.Apple],
}
