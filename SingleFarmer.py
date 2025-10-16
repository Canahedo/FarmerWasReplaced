import Utils
import Data
import SinglePoly
import SingleSunflower
import SinglePumpkin
import SingleCactus


def poly():
    SinglePoly.setup()
    SinglePoly.run()


def pumpkin():
    SinglePumpkin.setup()
    SinglePumpkin.run(0)
    Utils.goto([0, 0])
    SinglePumpkin.run(1)
    SinglePumpkin.clean_up()


def sunflower():
    SingleSunflower.setup()
    SingleSunflower.run()
    SingleSunflower.clean_up()


def cactus():
    SingleCactus.setup()
    SingleCactus.run()
    SingleCactus.clean_up()


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
