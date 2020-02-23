from kivy.animation import Animation

def move_up(self, times, animator):
    #check = self.robot.pos[1] + 100 * times
    animator += Animation(y=self.robot.pos[1] + 100*times, duration=0.2, t='in_out_cubic')
    return animator

def move_down(self, times, animator):
    animator += Animation(y=self.robot.pos[1] - 100*times, duration=0.2, t='in_out_cubic')
    return animator

def move_right(self, times, animator):
    animator += Animation(x=self.robot.pos[0] + 100*times, duration=0.2, t='in_out_cubic')
    return animator

def move_left(self, times, animator):
    animator += Animation(x=self.robot.pos[0] - 100*times, duration=0.2, t='in_out_cubic')
    return animator