from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color, get_color
from kivy.clock import Clock
from functools import partial
from kivy.animation import Animation

time = 0
def timer():
	global time
	time += 0.3
	return time


def animator(self, code, *largs):
	code.start(self.robot)


def move_algorithm(self):
	anim = []
	position = self.robot.pos
	anim.append(move_up(self, 2, 'in_out_cubic', position))

	print(anim)
	for i in anim:
		Clock.schedule_once(partial(animator, self, i), timer())
