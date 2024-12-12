def harvestWait():
	while True:
		if can_harvest():
			harvest()
			break

def even(int):
	if int % 2 == 0:
		return True
	else:
		return False

def enoughItems(item, target):
	if num_items(item) < target:
		return False
	return True
	
def theLoopCheck(pumpkin, carrot, wood, hay, power):
 if num_items(Items.Pumpkin) > pumpkin:
  if num_items(Items.Carrot) > carrot:
   if num_items(Items.Wood) > wood:
    if num_items(Items.Hay) > hay:
     if num_items(Items.Power) > power:
         return False
 return True
	
def sort(input):
	sortedlist = []
	petals = 15
	while petals > 6:
		for i in input:
			if i[0] == petals:
				sortedlist.append(i[1])
		petals = petals - 1
	return sortedlist