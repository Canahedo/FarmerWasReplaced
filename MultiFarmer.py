import Utils
import Data
#import MultiPoly
#import MultiSunflower
#import MultiPumpkin
#import MultiCactus
#import MultiMaze


#def poly():
	#MultiPoly.run()


#def pumpkin():
	#MultiPumpkin.run()


#def sunflower():
	#MultiSunflower.run()


#def cactus():
	#MultiCactus.run()


#def maze():
	#if get_entity_type() not in [Entities.Treasure, Entities.Hedge]:
		#MultiMaze.setup()
	#else:
		#MultiMaze.just_map()
	#MultiMaze.run()


def run():
	for plant in plant_types:
		if Data.crop in plant_types[plant]:
			plant()


plant_types = {
	#poly: [Entities.Grass, Entities.Tree, Entities.Carrot],
	#pumpkin: [Entities.Pumpkin],
	#sunflower: [Entities.Sunflower],
	#cactus: [Entities.Cactus],
	#maze: [Entities.Treasure],
}