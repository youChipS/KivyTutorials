import kivy
from kivy.app import App
from kivy.uix.button import Label

kivy.require("1.9.0")


class HelloKivyApp(App):

    def build(self):
        return Label()


helloKivy = HelloKivyApp()
helloKivy.run()
