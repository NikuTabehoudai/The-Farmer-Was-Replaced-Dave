def harvestField():
	goto(0,0)
	while True:
		harvestWait()
		if atTopRight():
			break
		moveNext()