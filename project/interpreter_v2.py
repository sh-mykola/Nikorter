import interpreter_code_v2
import interpreter_code
from importlib import reload
import random
import webcolors
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1050")
Config.set("graphics", "height", "650")

local_path = os.path.dirname(__file__)
print(local_path)

def create_code(code_plain):
    f = open("interpreter_code_v2.py", "w+")
    f.write("from interpreter_defcode_v2 import *")
    f.write("\nfrom kivy.animation import Animation\n")
    f.write("\ndef move_algorithm(self):\n")

    f.write("\tanim = []\n")
    f.write("\tposition = list(self.robot.pos)\n")
    f.write("\tc_r = self.robot.rgb\n\tcolor = (c_r[0], c_r[1], c_r[2])\n")
    for i in code_plain:
        f.write("\t{}\n".format(i))
        if i[0:4] == "elif" or i[0:2] == "if":
            pass
        else:
            f.write("\tposition = list(anim[-1][1])\n")
        # f.write("\tprint('---:', position)\n")

    # f.write("\tprint(anim)\n")
    f.write("\tanimator = Animation()\n\tfor i in range(len(anim)):\n\t\tanimator += anim[i][0]\n")
    f.write("\tanimator.start(self.robot)\n")

    f.close()

labyrinth = False

class MyProgram(Widget):
    code = ObjectProperty(None)
    console = ObjectProperty(None)
    robot = ObjectProperty(None)
    local_dir = StringProperty(local_path)

    """def __init__(self, **kwargs):
        super(MyProgram, self).__init__(**kwargs)
        self.local_dir = str(local_path)"""

    def start_interpret(self):
        # getting code
        code = self.code.text
        if code == "":
            return
        reload(interpreter_code)
        data = interpreter_code.run(code)
        if len(data[0]) == 0 or data[0][0] == "Error!" or data[1] == True:
            self.console.text = "Error!"
            return

        create_code(data[0])
        # starting code
        # move_up(self, 2, timer())
        reload(interpreter_code_v2)
        interpreter_code_v2.move_algorithm(self)
        # Clock.schedule_once(partial(move_algorithm, self), 2)
        # setting console
        self.console.text = "For tree check console or tree_view.txt"  # data[1]

    def reset_position(self):
        self.console.text = "Reseted!"
        self.robot.rgb = (1, 1, 1)
        Animation.cancel_all(self.robot)
        anim = Animation(x=1500, y=0, duration=0.4, t='in_out_cubic')
        anim.start(self.robot)
        # self.robot.pos = [1000, 0]

    def randomize_position(self):
        self.console.text = ""
        x = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
        y = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]

        rand_x = random.choice(x)
        rand_y = random.choice(y)
        rand_color = (random.random(), random.random(), random.random())
        rand_color_hex = webcolors.rgb_to_hex((int(round(rand_color[0] * 255, 3)), int(round(rand_color[1] * 255, 3)),
                                               int(round(rand_color[2] * 255, 3))))

        self.robot.rgb = rand_color

        Animation.cancel_all(self.robot, 'x')
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

    def show_labyrinth(self):
        global labyrinth
        sound = SoundLoader.load(local_path+'/resources/sounds/ROBOTIC_Mech_Movement_01_Footstep_stereo.wav')
        if labyrinth:
            sound.play()
            anim = Animation(labyrinth_opacity = 0, duration=0.5, t='in_out_back')
            anim.start(self.robot)
            labyrinth = False
        else:
            sound.play()
            anim = Animation(labyrinth_opacity = 1, duration=0.5, t='in_out_back')
            anim.start(self.robot)
            labyrinth = True



    """
    def place_robot(self):
        self.robot.pos += [100, 100]

    place_robot()
    
    def move_robot(self):
    pos = self.robot.pos
    pos = move_up(pos)

    self.robot.pos = pos
    """


class LightBot_v2App(App):
    def build(self):
        return MyProgram()


if __name__ == "__main__":
    LightBot_v2App().run()

# TODO Make special location for robot
# TODO Border checker
# TODO Code input / Console out style
# TODO: Cool background maybe gif with dif layers for cool effect
# TODO: Same to robot
# TODO: Move sounds
# TODO: Remove absolute path
