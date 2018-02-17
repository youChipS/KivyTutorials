import kivy
from kivy.app import App
from kivy.uix.widget import Widget

kivy.require("1.9.0")


class CustomWidget(Widget):
    pass


class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()


customWidget = CustomWidgetApp()
customWidget.run()
