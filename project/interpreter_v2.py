from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from functools import partial
from kivy.animation import Animation

from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "650")

import interpreter_code_v2
from importlib import reload
import sys
import time as tm

console_log = "CONSOLE LOG:\n"

def create_code(code_plain):
    f = open("interpreter_code_v2.py", "w+")
    f.write("from interpreter_defcode_v2 import move_up, move_down, move_right, move_left")
    f.write("\ntime = 0\ndef timer():\n\tglobal time\n\ttime += 0.3\n\treturn time")
    f.write("\ndef move_algorithm(self):\n")
    code = code_plain.split("\n")
    for i in code:
        f.write("\t{}\n".format(i))
    f.write("\tpass\n")
    f.close()

time = 0
def timer():
    global time
    time += 0.3
    return time

create_code("")

class MyProgram(Widget):
    code = ObjectProperty(None)
    console = ObjectProperty(None)
    robot = ObjectProperty(None)

    def start_interpret(self):
        #getting code
        code = self.code.text
        create_code(code)
        #starting code
        # move_up(self, 2, timer())
        reload(interpreter_code_v2)
        interpreter_code_v2.move_algorithm(self)
        #Clock.schedule_once(partial(move_algorithm, self), 2)
        #setting console
        self.console.text = console_log


    # TODO Make special location for robot
    """def place_robot(self):
        self.robot.pos += [100, 100]

    place_robot()"""


    """def move_robot(self):
        pos = self.robot.pos
        pos = move_up(pos)

        self.robot.pos = pos"""

    # TODO Border checker
    # TODO Code input / Console out style
    # TODO Add different animations to own code by kivy animator
    # TODO Publish on GitHub in ideal version for portfolio


class LightBot_v2App(App):
    def build(self):
        return MyProgram()


if __name__ == "__main__":
    LightBot_v2App().run()

# TODO Create 2d array of variables after lexer read
# code than step by step with timer move through this variables

# TODO Create lexer
# TODO Create tree viewer in lexer
# TODO Create
