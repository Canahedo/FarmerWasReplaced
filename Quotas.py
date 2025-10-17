quotas = [
    [Items.Hay, Entities.Grass, 1000000 * 1],
    [Items.Wood, Entities.Tree, 1000000 * 4],
    [Items.Carrot, Entities.Carrot, 1000000 * 1],
    [Items.Power, Entities.Sunflower, 1000 * 7.5],
    [Items.Pumpkin, Entities.Pumpkin, 1000000 * 5],
    [Items.Cactus, Entities.Cactus, 1000000 * 1],
    # [Items.Gold, Entities.Treasure, 1000 * 1],
]


def pick_crop():
    for prospect in quotas:
        if num_items(prospect[0]) < prospect[2]:
            return prospect[1]
