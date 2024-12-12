def treeField():
	goto(0,0)
	while True:
		if even(get_pos_y()):
			if even(get_pos_x()):
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		else:
			if even(get_pos_x()):
				plant(Entities.Bush)
			else:
				plant(Entities.Tree)
		if atTopRight():
			break
		moveNext()
		
	goto(0,0)
	harvestField()
		
	