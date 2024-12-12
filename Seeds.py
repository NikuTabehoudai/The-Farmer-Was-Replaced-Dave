def getSeeds(type):
	target = buyTargets(type) 
	if target > 0:
		trade(type, target)
	

def needSeeds(type):
	if type == Entities.Carrots:
		getSeeds(Items.Carrot_Seed)
	
	if type == Entities.Sunflower:
		getSeeds(Items.Sunflower_Seed)
	
	if type == Entities.Pumpkin:
		getSeeds(Items.Pumpkin_Seed)
		
def buyTargets(type):
	fs = get_world_size() * get_world_size()
	return fs - num_items(type)
		

def enoughSeeds(type):
	fs = get_world_size() * get_world_size()
	if type == Entities.Carrots:
		if num_items(Items.Hay) < fs or num_items(Items.Wood) < fs:
			return False
		return True
			
	if type ==  Entities.Sunflower:
		if num_items(Items.Carrot) < fs:
			return False
		return True
	
	if type == Entities.Pumpkin:
		if num_items(Items.Carrot) < fs:
			return False
		return True