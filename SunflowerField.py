def SunflowerField():

	needSeeds(Entities.Sunflower)
	enoughWater()
	goto(0,0)
	
	fieldcords = []
	while True:
		plant(Entities.Sunflower)
		water()
		cord = get_pos_x(),get_pos_y()
		measurement = [measure(), cord]
		fieldcords.append(measurement)
		if atTopRight():
			break
		moveNext()
	
	goto(0,0)
	
	for i in sort(fieldcords):
		goto(i[0],i[1])
		harvest()
		
		
	