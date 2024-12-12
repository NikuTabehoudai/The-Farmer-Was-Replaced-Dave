def fetch(pumpkin, carrot, wood, hay, power):
	while theLoopCheck(pumpkin, carrot, wood, hay, power):
		while num_items(Items.Power) < power:
			if enoughSeeds(Entities.Sunflower):
				field(Entities.Sunflower)
			elif enoughSeeds(Entities.Carrots):
				field(Entities.Carrots)
			else:
				field(Entities.Grass)
				treeField() 
		
		while num_items(Items.Pumpkin) < pumpkin:
			if enoughSeeds(Entities.Pumpkin):
				pumpkinField()
			elif enoughSeeds(Entities.Carrots):
				field(Entities.Carrots)
			else:
				field(Entities.Grass)
				treeField()
			
		while num_items(Items.Carrot) < carrot:
			if enoughSeeds(Entities.Carrots):
				field(Entities.Carrots)
			else:
				field(Entities.Grass)
				treeField()
		
		while num_items(Items.Wood) < wood:
			treeField()
			
		while num_items(Items.Hay) < hay:
			field(Entities.Grass)
	
			