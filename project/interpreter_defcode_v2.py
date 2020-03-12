from kivy.animation import Animation
import time
durations = 0.4

def move_up(times, animation, position):
    #check = self.robot.pos[1] + 100 * times
    #self.robot.pos[1] += 100 *times
    if position[1] + 100 * times <= 1200:
        position[1] += 100 * times
        animator = Animation(y=position[1], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]


def move_down(times, animation, position):
    if position[1] - 100 * times >= 0:
        position[1] -= 100 * times
        animator = Animation(y=position[1], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]


def move_right(times, animation, position):
    if position[0] + 100 * times <= 1900:
        position[0] += 100 * times
        animator = Animation(x=position[0], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]

def move_left(times, animation, position):
    if position[0] - 100 * times >= 1000:
        position[0] -= 100 * times
        animator = Animation(x=position[0], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]

def change_color(color, position):
    animator = Animation(rgb=color, duration=durations)
    return [animator, position]


def get_color(self):
    time.sleep(durations)
    color = self.robot.rgb
    color_norm = (color[0], color[1], color[2])
    print(color_norm)
    return color_norm






