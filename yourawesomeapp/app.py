"""
NOTES:

Access your assets like:
'assets/images/icon.png'
'assets/shaders/blocks.glsl'

You can choose to put all your third-party libraries in the `lib` folder.

"""
__all__ = ('YourAwesomeApp',)
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


class YourAwesome(FloatLayout):
    def __init__(self, **kwargs):
        super(YourAwesome, self).__init__(**kwargs)

        self.add_widget(Label(text='Hello world!'))


class YourAwesomeApp(App):
    def build(self):
        return YourAwesome()
