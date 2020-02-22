from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.vector import Vector

from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "650")


console_log = "CONSOLE LOG:\n"

"""def move_up(pos):
    pos[1] += 100
    return pos"""

def move_up(self):
    self.robot.pos[0] += 100


class MyProgram(Widget):
    code = ObjectProperty(None)
    console = ObjectProperty(None)
    robot = ObjectProperty(None)

    def get_code(self):
        print(self.code.text)

    """def move_robot(self):
        pos = self.robot.pos
        pos = move_up(pos)

        self.robot.pos = pos"""

    def move_robot(self):
        move_up(self)
        #self.robot.pos[0] += 100

    def set_console(self):
        self.console.text = console_log


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
