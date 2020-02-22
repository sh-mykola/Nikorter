from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "650")

class MyProgram(Widget):
    code = ObjectProperty(None)

    def get_code(self):
        print(self.code.text)


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
