from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color, get_color
from kivy.animation import Animation

def move_algorithm(self):
	anim = []
	position = list(self.robot.pos)
	anim.append(change_color((1.0, 1.0, 1.0), position))
	position = list(anim[-1][1])
	if get_color(self) == (1.0, 1.0, 0.0):
		anim.append(change_color((1.0, 0.0, 0.0), position))
	elif get_color(self) == (1.0, 1.0, 1.0):
		anim.append(change_color((1.0, 0.0, 1.0), position))
	else:
		anim.append(change_color((0.0, 0.0, 1.0), position))
	position = list(anim[-1][1])
	animator = Animation()
	for i in range(len(anim)):
		animator += anim[i][0]
	animator.start(self.robot)
