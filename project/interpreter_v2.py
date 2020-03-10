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
import interpreter_code
from importlib import reload
import logging
import random
import webcolors
import numpy
#Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename="/Volumes/Niko/Python/Nikorter/project/console.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = "w")
logger = logging.getLogger()
logger.info("Initialization")

console_log = "CONSOLE LOG:\n"

def create_code(code_plain):
    f = open("interpreter_code_v2.py", "w+")
    f.write("from interpreter_defcode_v2 import move_up, move_down, move_right, move_left, change_color")
    f.write("\ntime = 0\ndef timer():\n\tglobal time\n\ttime += 0.3\n\treturn time")
    f.write("\ndef move_algorithm(self):\n")
    for i in code_plain:
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
        if code == "":
            return
        reload(interpreter_code)
        data = interpreter_code.run(code)
        if len(data[0]) == 0 or data[0][0] == "Error!" or data[2] == True:
            self.console.text = "Error!"
            return

        create_code(data[0])
        #starting code
        # move_up(self, 2, timer())
        reload(interpreter_code_v2)
        interpreter_code_v2.move_algorithm(self)
        #Clock.schedule_once(partial(move_algorithm, self), 2)
        #setting console
        self.console.text = data[1]

    def reset_position(self):
        self.console.text = "Reseted!"
        self.robot.rgb = (1, 1, 1)
        Animation.cancel_all(self.robot)
        anim = Animation(x = 1000, y = 0, duration=0.4, t='in_out_cubic')
        anim.start(self.robot)
        #self.robot.pos = [1000, 0]

    def randomize_position(self):
        self.console.text = ""
        x = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]
        y = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]

        rand_x = random.choice(x)
        rand_y = random.choice(y)
        rand_color = (random.random(), random.random(), random.random())
        rand_color_hex = webcolors.rgb_to_hex((int(round(rand_color[0]*255, 3)), int(round(rand_color[1]*255, 3)), int(round(rand_color[2]*255, 3))))

        self.robot.rgb = rand_color

        Animation.cancel_all(self.robot)
        anim = Animation(x=rand_x, y=rand_y, duration=0.4, t='in_out_cubic')
        anim.start(self.robot)
        self.console.text = "Randomized!\nPosition: [{}, {}]\nColor: {}".format(rand_x, rand_y, rand_color_hex)

    def open_from_file(self):
        self.console.text = "Loaded!"
        path = self.path.text
        raw_code = ""
        with open(path, 'r') as file:
            data = file.read()
        self.code.text = data



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
    # TODO Animation change +  color change as parametr in kiv  by global variable
    # TODO Double symbols problem


class LightBot_v2App(App):
    def build(self):
        return MyProgram()


if __name__ == "__main__":
    LightBot_v2App().run()

# TODO Create 2d array of variables after lexer read
# code than step by step with timer move through this variables

# TODO Create lexer
# TODO Create tree viewer in lexer
# TODO Transfer console to pogram
# TODO System events: (change color, change animation, last function)
# TODO Open from file
# TODO Random location and color
