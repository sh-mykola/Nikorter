from kivy.animation import Animation
from kivy.clock import Clock
from functools import partial


def move_up_main(self, times, *largs):
    #check = self.robot.pos[1] + 100 * times
    #self.robot.pos[1] += 100 *times
    anim = Animation(y=self.robot.pos[1] + 100 * times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)


def move_down_main(self, times, *largs):
    #self.robot.pos[1] -= 100 *times
    anim = Animation(y=self.robot.pos[1] - 100 * times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)


def move_right_main(self, times, *largs):
    anim = Animation(x=self.robot.pos[0] + 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)

def move_left_main(self, times, *largs):
    anim = Animation(x=self.robot.pos[0] - 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)

def move_up(self, times, timer):
    Clock.schedule_once(partial(move_up_main, self, times), timer)

def move_down(self, times, timer):
    Clock.schedule_once(partial(move_down_main, self, times), timer)

def move_right(self, times, timer):
    Clock.schedule_once(partial(move_right_main, self, times), timer)

def move_left(self, times, timer):
    Clock.schedule_once(partial(move_left_main, self, times), timer)