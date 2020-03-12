from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color, get_color
time = 0
def timer():
	global time
	time += 0.3
	return time
def move_algorithm(self):
	change_color(self, (0.0, 0.0, 1.0), timer())
	move_up(self, 2, timer(), 'in_out_cubic') 
	change_color(self, (0.0, 1.0, 0.0), timer())
	move_right(self, 4, timer(), 'in_out_bounce') 
	pass
