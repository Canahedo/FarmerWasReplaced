import Utils
import Data
import Quotas
import SingleFarmer
import MultiFarmer

farmer_type = "single"  # "single" or "multi"

change_hat(Hats.Straw_Hat)
while True:
	Utils.goto([0, 0])
	Data.size = get_world_size()
	Utils.set_water_level()

	# Break loop if all quotas met
	if Data.crop == None:
		print("Quotas Met")
		break

	if farmer_type == "single":			
		SingleFarmer.run() 

	else:
		MultiFarmer.run()
		
	Data.prev_crop = Data.crop
	