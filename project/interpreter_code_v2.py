from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color
from kivy.animation import Animation

def move_algorithm(self):
	anim = []
	position = list(self.robot.pos)
	c_r = self.robot.rgb
	color = (c_r[0], c_r[1], c_r[2])
	anim.append(change_color((1.0, 1.0, 1.0), position))
	color = (1.0, 1.0, 1.0)
	position = list(anim[-1][1])
	if color == (1.0, 1.0, 0.0):
		anim.append(change_color((1.0, 0.0, 0.0), position))
		color = (1.0, 0.0, 0.0)
	elif color == (1.0, 1.0, 1.0):
		anim.append(change_color((1.0, 0.0, 1.0), position))
		color = (1.0, 0.0, 1.0)
	else:
		anim.append(change_color((0.0, 0.0, 1.0), position))
		color = (0.0, 0.0, 1.0)
	position = list(anim[-1][1])
	animator = Animation()
	for i in range(len(anim)):
		animator += anim[i][0]
	animator.start(self.robot)
