def harvestWait():
	while True:
		if can_harvest():
			harvest()
			break

def even(int):
	if int % 2 == 0:
		return True
	return False

def enoughItems(item, target):
	if num_items(item) < target:
		return False
	return True
	
def theLoopCheck(pumpkin, carrot, wood, hay, power):
 if enoughItems(Items.Pumpkin, pumpkin):
  if enoughItems(Items.Carrot, carrot):
   if enoughItems(Items.Wood, wood):
    if enoughItems(Items.Hay, hay):
     if enoughItems(Items.Power, power):
         return False
 return True
	
def sortSunflowers(input):
	sortedlist = []
	petals = 15
	while petals > 6:
		for i in input:
			if i[0] == petals:
				sortedlist.append(i[1])
		petals = petals - 1
	return sortedlist