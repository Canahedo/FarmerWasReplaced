size = 0
crop = None
water = 0
tree_toggle = 0
map = None


def DEBUG():
    global size
    global crop

    size = 15
    crop = Entities.Cactus

    clear()
    while not can_harvest():
        do_a_flip()
