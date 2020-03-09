from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color
time = 0
def timer():
	global time
	time += 0.3
	return time
def move_algorithm(self):
	move_up(self, 2, timer(), 'in_out_cubic') 
	move_right(self, 4, timer(), 'in_out_bounce') 
	change_color(self, (1.0, 0.0, 0.0), timer())
	move_up(self, 2, timer(), 'in_out_circ') 
	pass
