def atTopRight():
	ws = get_world_size()
	if get_pos_x() == ws - 1 and get_pos_y() == ws -1:
		return True

def atStart():
	if get_pos_x() == 0 and get_pos_y() == 0:
		return True