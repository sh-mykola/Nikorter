from kivy.animation import Animation
durations = 0.2

def move_up(times, animation, position):
    #check = self.robot.pos[1] + 100 * times
    #self.robot.pos[1] += 100 *times
    if (position[1] + 100 * times <= 1200):
        position[1] = position[1] + 100 * times
        animator = Animation(y=position[1], duration=durations, t=animation)
        # print("Current pos:" + str(self.robot.pos))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]


def move_down(self, times, animation):
    #self.robot.pos[1] -= 100 *times
    if (self.robot.pos[1] - 100 * times >= 0):
        animator = Animation(y=self.robot.pos[1] - 100 * times, duration=durations, t=animation)
        # print("Current pos:" + str(self.robot.pos))
        return animator
    else:
        print("Error! Out of border")
        return Animation()


def move_right(self, times, animation):
    if (self.robot.pos[0] + 100 * times <= 1900):
        animator = Animation(x=self.robot.pos[0] + 100*times, duration=durations, t=animation)
        #print("Current pos:" + str(self.robot.pos))
        return animator
    else:
        print("Error! Out of border")
        return Animation()

def move_left(self, times, animation):
    if (self.robot.pos[0] - 100 * times >= 1000):
        animator = Animation(x=self.robot.pos[0] - 100*times, duration=durations, t=animation)
        #print("Current pos:" + str(self.robot.pos))
        return animator
    else:
        print("Error! Out of border")
        return Animation()

def change_color(self, color):
    animator = Animation(rgb=color, duration=durations)
    return animator


def get_color(self):
    color = self.robot.rgb
    color_norm = (color[0], color[1], color[2])
    return color_norm






