import Utils
import Data
import SinglePoly
import SingleSunflower
import SinglePumpkin
import SingleCactus


def poly():
	SinglePoly.run()


def pumpkin():
	SinglePumpkin.run()


def sunflower():
	SingleSunflower.setup()
	SingleSunflower.run()
	SingleSunflower.clean_up()


def cactus():
	SingleCactus.setup()
	SingleCactus.run()
	SingleCactus.clean_up()
	while True:
		do_a_flip()


def maze():
	pass


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
}
