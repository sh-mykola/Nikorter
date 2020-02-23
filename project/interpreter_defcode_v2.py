from kivy.animation import Animation

import time

def move_up(self, times, *largs):
    #check = self.robot.pos[1] + 100 * times
    #self.robot.pos[1] += 100 *times
    anim = Animation(y=self.robot.pos[1] + 100 * times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)


def move_down(self, times, *largs):
    #self.robot.pos[1] -= 100 *times
    anim = Animation(y=self.robot.pos[1] - 100 * times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)


def move_right(self, times, *largs):
    anim = Animation(x=self.robot.pos[0] + 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)

def move_left(self, times, *largs):
    anim = Animation(x=self.robot.pos[0] - 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)