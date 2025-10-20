import Utils
import Data


def run():
	for axis in range(2):
		for col in range(Data.size):
			Data.map = []
			for row in range(Data.size):
				if axis == 0:
					farm()
				else:
					Data.map.append(measure())
				move([North, East][axis])
			slice_sort(axis, col)
			Utils.goto([(col, 0),(0, col)][axis])
			move([East, North][axis])
		Utils.goto()
	harvest()

		
def farm():
	if get_entity_type() == Entities.Cactus:
		Data.map.append(measure())
		return
	if not Utils.ready_for_planting():
		return
	Utils.prep_ground(Entities.Cactus)
	plant(Entities.Cactus)
	Utils.water()
	Data.map.append(measure())


def slice_sort(axis, col):
	sorted_slice = Utils.get_sorted_list(Data.map)
	while Data.map != sorted_slice:
		low_bar, high_bar = update_bounds(sorted_slice)
		Utils.goto([(col, low_bar),(low_bar, col)][axis])
		for i in range(low_bar, high_bar):
			sort(i, axis)
			move([North, East][axis])
		sort(high_bar, axis)
		for i in range(high_bar, low_bar, -1):
			sort(i, axis)
			move([South, West][axis])
		sort(low_bar, axis)


def update_bounds(sorted):
	low, high = None, None
	for i in range(Data.size):
		if sorted[i] != Data.map[i]:
			low = i
			break
	for i in range(Data.size-1, -1, -1):
		if sorted[i] != Data.map[i]:
			high = i
			break
	if low == None:
		pass
	elif low < 1:
		low = 1
	if high == None:
		pass
	elif high > Data.size - 2:
		high = Data.size - 2
	return low, high


def sort(index, axis):
	a, b, c = Data.map[index - 1],Data.map[index],Data.map[index + 1]
	while not a<=b<=c:
		#Low swap
		if b==c<a or a==c>b or b<a<c or b<c<a:
			a, b = b, a
			swap([South,West][axis])
		# High swap
		elif a==c<b	or a==b>c or a<c<b or c<a<b or c<b<a:
			b, c = c, b
			swap([North,East][axis])
	Data.map[index - 1],Data.map[index],Data.map[index + 1] = a, b, c