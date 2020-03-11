from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color, get_color
time = 0
def timer():
	global time
	time += 0.3
	return time
def move_algorithm(self):
	change_color(self, (0.06666666666666667, 1.0, 0.2), timer())
	for i in range(2):
		move_right(self, 2, timer(), 'in_out_cubic') 
	for i in range(3):
		move_up(self, 3, timer(), 'in_out_cubic') 
	change_color(self, (1.0, 0.0, 0.2), timer())
	if get_color(self, timer()) == (1.0, 0.0, 0.2):
		change_color(self, (1.0, 1.0, 1.0), timer())
		print('Changed', '-'*100)
	move_right(self, 2, timer(), 'in_out_cubic') 
	change_color(self, (0.0, 0.4666666666666667, 0.2), timer())
	move_left(self, 4, timer(), 'in_out_cubic') 
	pass
