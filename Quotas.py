quotas = [
	[Items.Hay, Entities.Grass, 1000000 * 1],
	[Items.Wood, Entities.Tree, 1000000 * 1],
	[Items.Carrot, Entities.Carrot, 1000000 * 1],
	[Items.Power, Entities.Sunflower, 1000 * 10],
	[Items.Pumpkin, Entities.Pumpkin, 1000000 * 10],
	[Items.Cactus, Entities.Cactus, 1000000 * 1],
	[Items.Gold, Entities.Treasure, 1000000 * 100],
	[Items.Bone, Entities.Apple, 1000000 * 200],
]


def pick_crop():
	for prospect in quotas:
		if num_items(prospect[0]) < prospect[2]:
			return prospect[1]
