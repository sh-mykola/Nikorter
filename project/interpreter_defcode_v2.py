from kivy.animation import Animation
from kivy.clock import Clock
from functools import partial

def move_up_main(self, times, animation, *largs):
    #check = self.robot.pos[1] + 100 * times
    #self.robot.pos[1] += 100 *times
    if (self.robot.pos[1] + 100 * times <= 1200):
        anim = Animation(y=self.robot.pos[1] + 100 * times, duration=0.2, t=animation)
        anim.start(self.robot)
        print("Current pos:" + str(self.robot.pos))
    else:
        print("Error! Out of border")


def move_down_main(self, times, animation, *largs):
    #self.robot.pos[1] -= 100 *times
    if (self.robot.pos[1] - 100 * times >= 0):
        anim = Animation(y=self.robot.pos[1] - 100 * times, duration=0.2, t=animation)
        anim.start(self.robot)
        print("Current pos:" + str(self.robot.pos))
    else:
        print("Error! Out of border")


def move_right_main(self, times, animation, *largs):
    if (self.robot.pos[0] + 100 * times <= 1900):
        anim = Animation(x=self.robot.pos[0] + 100*times, duration=0.2, t=animation)
        anim.start(self.robot)
        print("Current pos:" + str(self.robot.pos))
    else:
        print("Error! Out of border")

def move_left_main(self, times, animation, *largs):
    if (self.robot.pos[0] - 100 * times >= 1000):
        anim = Animation(x=self.robot.pos[0] - 100*times, duration=0.2, t=animation)
        anim.start(self.robot)
        print("Current pos:" + str(self.robot.pos))
    else:
        print("Error! Out of border")

def change_color_main(self, color, *largs):
    self.robot.rgb = color

colors = ()

def get_color_main(self, *largs):
    global colors
    color = self.robot.rgb
    # (int(round(rand_color[0]*255, 3))
    # color_hex = webcolors.rgb_to_hex((int(round(color[0]*255, 3)), int(round(color[1]*255, 3)), int(round(color[2]*255, 3))))
    color_norm = (color[0], color[1], color[2])
    """print("Def_code:")
    print(color)"""
    colors = color_norm

def move_up(self, times, timer, animation="in_out_cubic"):
    Clock.schedule_once(partial(move_up_main, self, times, animation), timer)

def move_down(self, times, timer, animation="in_out_cubic"):
    Clock.schedule_once(partial(move_down_main, self, times, animation), timer)

def move_right(self, times, timer, animation="in_out_cubic"):
    Clock.schedule_once(partial(move_right_main, self, times, animation), timer)

def move_left(self, times, timer, animation="in_out_cubic"):
    Clock.schedule_once(partial(move_left_main, self, times, animation), timer)

def change_color(self, color, timer):
    Clock.schedule_once(partial(change_color_main, self, color), timer)

def get_color(self, timer):
    Clock.schedule_once(partial(get_color_main, self), timer)
    return colors



