from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation

from kivy.graphics import (Color, Rectangle)

from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "650")

offset = 1000


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 0, 1, 1)
            Rectangle(pos = (0+offset, 0), size = (100, 100))

        def move(self):
            anim = Animation(x=100, y=100)
            anim.start(self)


class LightBotApp(App):
    def build(self):
        main_layout = BoxLayout()
        control_layout = BoxLayout(orientation = "vertical")
        game = GameWidget()

        code = CodeInput()
        start = Button(text="Interpret", size_hint_y=None, height=100)

        control_layout.add_widget(code)
        control_layout.add_widget(start)
        main_layout.add_widget(control_layout)
        main_layout.add_widget(game)

        return main_layout


if __name__ == "__main__":
    LightBotApp().run()
