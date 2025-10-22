import Utils
import Data
import Quotas
import Farmer

farmer_type = "single"  # "single" or "multi"
crop_override = None
size_override = None
leaderboard = True

change_hat(Hats.Straw_Hat)
while True:
	Utils.goto()
	Data.size = size_override
	
	if crop_override == None:
		Data.crop = Quotas.pick_crop()
	else:
		Data.crop = crop_override
	if num_items(Items.Power) < 5000:
		Data.crop = Entities.Sunflower
		
	if leaderboard:
		Data.leaderboard = True
	if farmer_type == "multi":			
		Data.multi = True
		
	Utils.set_water_level()

	# Break loop if all quotas met
	if Data.crop == None:
		print("Quotas Met")
		break
	
	Farmer.run()
			
	Data.prev_crop = Data.crop
