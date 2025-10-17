## TODO: Do more per loop, fewer loops
## TODO: Don't increment horizintally, search


import Utils
import Data
import Quotas
import SingleFarmer

farmer_type = "single"  # "single" or "multi"

while True:
    Utils.goto([0, 0])
    Data.size = get_world_size()
    Data.crop = Quotas.pick_crop()
    Utils.set_water_level()
    Data.DEBUG()  # Comment out to disable

    # Break loop if all quotas met
    if Data.crop == None:
        print("Quotas Met")
        break

    if farmer_type == "single":
        SingleFarmer.run()

    else:
        # TODO: Multi Drone Farm Handler
        pass
