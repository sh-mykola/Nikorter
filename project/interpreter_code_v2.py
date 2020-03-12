from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color
from kivy.animation import Animation

def move_algorithm(self):
	anim = []
	position = list(self.robot.pos)
	c_r = self.robot.rgb
	color = (c_r[0], c_r[1], c_r[2])
	anim.append(move_up(6, 'in_out_cubic', position))
	position = list(anim[-1][1])
	animator = Animation()
	for i in range(len(anim)):
		animator += anim[i][0]
	animator.start(self.robot)
