from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class MainScreen(Screen):
    pass


class TimeDelay(Screen):
    pass


class PrankScreen(Screen):
    pass


class ButtonDelay(Button):
    def clocked_switch(self):
        Clock.schedule_once(self.switch_to_main, 3)

    def switch_to_main(self, *args):
        app = App.get_running_app()
        app.root.current = "prank"


class TimeDelayApp(App):
    def build(self):
        root_widget = Builder.load_file("test_core.kv")
        return root_widget


if __name__ == "__main__":
    TimeDelayApp().run()