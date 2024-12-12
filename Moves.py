def moveNext():
	wc = get_world_size() - 1
	if get_pos_y() == wc:
		moveNorth()
		moveEast()
	else:
		moveNorth()
			
def moveNorth():
	move(North)

def moveEast():
	move(East)

def moveSouth():
	move(South)
	
def moveWest():
	move(West)

def goto(x, y):
    yDist = get_pos_y() - y  
    xDist = get_pos_x() - x  
    halfWorldSize = get_world_size()/2
    while get_pos_y() != y:
        if yDist >= halfWorldSize or (-halfWorldSize <= yDist and yDist < 0):
            moveNorth()
        else:
            moveSouth()
    while get_pos_x() != x:
        if xDist >= halfWorldSize or (-halfWorldSize <= xDist and xDist < 0):
            moveEast()
        else:
            moveWest()