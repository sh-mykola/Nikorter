from kivy.animation import Animation
from kivy.metrics import dp
durations = 0.4

def move_up(times, animation, position):
    #check = self.robot.pos[1] + 100 * times
    #self.robot.pos[1] += 100 *times
    if position[1] + dp(50) * times <= dp(600):
        position[1] += dp(50) * times
        animator = Animation(y=position[1], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]


def move_down(times, animation, position):
    if position[1] - dp(50) * times >= dp(0):
        position[1] -= dp(50) * times
        animator = Animation(y=position[1], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]


def move_right(times, animation, position):
    if position[0] + dp(50) * times <= dp(1000):
        position[0] += dp(50) * times
        animator = Animation(x=position[0], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]

def move_left(times, animation, position):
    if position[0] - dp(50) * times >= dp(500):
        position[0] -= dp(50) * times
        animator = Animation(x=position[0], duration=durations, t=animation)
        print("Current pos:" + str(position))
        return [animator, position]
    else:
        print("Error! Out of border")
        return [Animation(), position]

def change_color(color, position):
    animator = Animation(rgb=color, duration=0.2)
    return [animator, position]






