import Data


# Determines how much water to use on crops
def set_water_level():
    water_target = 1
    water_per_layer = Data.size**2
    water_supply = num_items(Items.Water)
    if water_supply < water_per_layer * 4:
        water_target = (water_supply / water_per_layer) / 4
    Data.water = water_target


# Travel to coordinate
def goto(coords):
    x, y = get_pos_x(), get_pos_y()
    dir_x, dir_y = West, South
    if x < coords[0]:
        dir_x = East
    if y < coords[1]:
        dir_y = North
    for i in range(abs(x - coords[0])):
        move(dir_x)
    for i in range(abs(y - coords[1])):
        move(dir_y)


# Waters crops and checks for harvestability/harvests
def ready_for_harvest():
    if num_items(Items.Water) > 0 and get_water() < Data.water:
        use_item(Items.Water)
    if get_entity_type() != None and can_harvest() == False:
        return False
    harvest()
    return True


# Tills ground if needed
def prep_ground(crop):
    ground = get_ground_type()
    wood = [Entities.Tree, Entities.Bush]
    if crop == Entities.Grass and ground == Grounds.Soil:
        till()
    elif ground == Grounds.Grassland and crop not in wood:
        till()


def get_sorted_list(unsorted_list):
    sorted_list = []
    holder_list = []
    for i in unsorted_list:
        holder_list.append(i)
    for value in range(max(unsorted_list) + 1):
        while value in holder_list:
            holder_list.remove(value)
            sorted_list.append(value)
    return sorted_list
