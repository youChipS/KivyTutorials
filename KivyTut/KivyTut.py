import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button


class HelloKivyApp(App):

    def build(self):
        return Button()



helloKivy = HelloKivyApp()

helloKivy.run()

