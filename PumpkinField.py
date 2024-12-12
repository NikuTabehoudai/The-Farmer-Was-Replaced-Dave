def pumpkinField():
	needSeeds(Entities.Pumpkin)
	enoughWater()
	goto(0,0)
	plantPumkins(needsSoil(Entities.Pumpkin))
	
def plantPumkins(soil):
	done = False
	while True:
		makeSoil(soil)
		if get_entity_type() == None:
			water()
			done = False
		plant(Entities.Pumpkin)
		if atTopRight() and done == True:
			harvest()
			break
		elif atTopRight():
			needSeeds(Entities.Pumpkin)
			done = True
		moveNext()