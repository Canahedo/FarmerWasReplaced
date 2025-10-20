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
	Utils.poly_cleanup()
	SingleMaze.setup()
	SingleMaze.single()
	SingleMaze.run()
	

def snake():
	Utils.poly_cleanup()
	SingleSnake.setup()
	while True:
		#SingleSnake.run()
		SingleSnake.single()

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
