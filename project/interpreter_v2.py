from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.animation import Animation

from kivy.config import Config
Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "650")

from interpreter_defcode_v2 import move_up, move_down, move_right, move_left

console_log = "CONSOLE LOG:\n"

"""def move_up(pos):
    pos[1] += 100
    return pos"""

def move_general(self):
    """anim = Animation(x=1100, y=0, duration=0.2)
    anim.start(self.robot)"""
    # self.robot.pos[0] += 100
    """if self.robot.pos > [1800, self.robot.pos[1]] or self.robot.pos < [1000, self.robot.pos[1]]:
        return"""
    anim = Animation(x=self.robot.pos[0] + 100, y=0, duration=0.2, t='in_out_cubic')
    #anim = Animation(pos=(0,800), duration=0.2)
    anim.start(self.robot)
    print(self.robot.pos)

class MyProgram(Widget):
    code = ObjectProperty(None)
    console = ObjectProperty(None)
    robot = ObjectProperty(None)

    def get_code(self):
        #print(self.code.text)
        pass

    """def move_robot(self):
        pos = self.robot.pos
        pos = move_up(pos)

        self.robot.pos = pos"""
     # TODO Border checker
    # TODO Code input / Console out style
    # TODO Add different animations to own code by kivy animator
    def move_robot(self):
        anim = Animation()
        anim = move_up(self, 5, anim)
        anim = move_down(self, 1, anim)
        anim = move_right(self, 4, anim)
        anim = move_down(self, 1, anim)
        anim = move_left(self, 3, anim)
        anim = anim.start(self.robot)
        #self.robot.pos[0] += 100

    def set_console(self):
        pass
        #self.console.text = console_log


class LightBot_v2App(App):
    def build(self):
        return MyProgram()


if __name__ == "__main__":
    LightBot_v2App().run()


#TODO Create 2d array of variables after lexer read
# code than step by step with timer move through this variables

#TODO Create lexer
#TODO Create tree viewer in lexer
#TODO Create
