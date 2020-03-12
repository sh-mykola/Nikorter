from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color, get_color
from kivy.animation import Animation


def move_algorithm(self):
	anim = []
	position = self.robot.pos
	anim.append(move_up(1, 'in_out_cubic', position))
	position = anim[-1][1]
	print('---:', position)
	print(anim)
	animator = Animation()
	for i in range(len(anim)):
		animator += anim[i][0]
	animator.start(self.robot)
