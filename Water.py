def enoughWater():
	fs = get_world_size() * get_world_size()
	if num_items(Items.Water_Tank) < fs * 4:
		while num_items(Items.Wood) < (fs * 4) * 5:
			treeField()
		trade(Items.Empty_Tank,fs * 4)

def water():
	while get_water() < 1:
		if num_items(Items.Water_Tank) == 0:
			break
		use_item(Items.Water_Tank)
