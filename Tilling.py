def needsSoil(type):
	if type == Entities.Carrots:
		return True
	
	if type ==  Entities.Pumpkin:
		return True
	
	if type == Entities.Sunflower:
		return True
	
	return False
	
		
def makeSoil(soil):
	if soil:
		if get_ground_type() != Grounds.Soil:
			till()
	if soil == False:
		if get_ground_type() != Grounds.turf:
			till()