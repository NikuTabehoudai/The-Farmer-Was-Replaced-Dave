def field(type):
	needSeeds(type)
	soil = needsSoil(type)
	enoughWater()
	goto(0,0)
	measuredField = []
	while True:
		if type != Entities.Grass:
			makeSoil(soil)
			water()
		plant(type)
		
		if type == Entities.Sunflower:
			cord = get_pos_x(),get_pos_y()
			measurement = [measure(), cord]
			measuredField.append(measurement)
		
		if atTopRight():
			break
		moveNext()
		
	
	if type == Entities.Sunflower:
		harvestSunflowerField(measuredField)
	else:
		harvestField()