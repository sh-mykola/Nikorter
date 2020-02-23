from kivy.animation import Animation

def move_up(self, times):
    #check = self.robot.pos[1] + 100 * times
    anim = Animation(y=self.robot.pos[1] + 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)

def move_down(self, times):
    anim = Animation(y=self.robot.pos[1] - 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)

def move_right(self, times):
    anim = Animation(x=self.robot.pos[0] + 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)

def move_left(self, times):
    anim = Animation(x=self.robot.pos[0] - 100*times, duration=0.2, t='in_out_cubic')
    anim.start(self.robot)