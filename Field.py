def field(type):
	needSeeds(type)
	soil = needsSoil(type)
	enoughWater()
	goto(0,0)
	while True:
		if type != Entities.Grass:
			makeSoil(soil)
			water()
		plant(type)
		
		
		if atTopRight():
			break
		moveNext()
		
	goto(0,0)
	harvestField()