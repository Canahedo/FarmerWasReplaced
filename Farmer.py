import Utils
import Data
import Poly
import Sunflower
import Pumpkin
import Cactus
import Maze
import Snake


def poly():
	Poly.run()


def pumpkin():
	Pumpkin.run()


def sunflower():
	Sunflower.run()


def cactus():
	Cactus.run()


def maze():
	Utils.poly_cleanup()
	Maze.setup()
	Maze.run()
	

def snake():
	Utils.poly_cleanup()
	SingleSnake.setup()
	#while True:
	SingleSnake.run()
		#SingleSnake.single()

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