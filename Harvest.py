def harvestField():
	goto(0,0)
	while True:
		harvestWait()
		if atTopRight():
			break
		moveNext()

def harvestSunflowerField(unsortedlist):
	for i in sortSunflowers(unsortedlist):
		goto(i[0],i[1])
		harvest()
	