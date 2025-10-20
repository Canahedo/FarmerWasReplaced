import Utils
import Data
import Quotas
import SingleFarmer

## DEBUG SETTINGS - Set to None for default
debug_size = None
debug_crop = Entities.Pumpkin
debug_clear = False
## END OF DEBUG SETTINGS

farmer_type = "single"  # "single" or "multi"

while True:
	if debug_clear:
		clear()
		while can_harvest() == False:
			do_a_flip()
	else:
		Utils.goto((0,0))
			
	if debug_size == None:
		Data.size = get_world_size()
	else:
		Data.size = debug_size
	if debug_crop == None:
		Data.crop = Quotas.pick_crop()
	else:
		Data.crop = debug_crop
	
	Utils.set_water_level()

	# Break loop if all quotas met
	if Data.crop == None:
		print("Quotas Met")
		break

	if farmer_type == "single":
		SingleFarmer.run() 

	else:
		# TODO: Multi Drone Farm Handler
		pass
		