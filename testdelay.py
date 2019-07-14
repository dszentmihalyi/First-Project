from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock, mainthread
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty


class Terms(Screen):
    terms = ObjectProperty(None)

    def check_data(self):
        if self.terms.active:
            print('Terms')
    # def on_checkbox_active(checkbox, value):
    #     if value:
    #         print('The checkbox', checkbox, 'is active')
    #     else:
    #         print('The checkbox', checkbox, 'is inactive')
    #
    # checkbox = CheckBox()
    # checkbox.bind(active=on_checkbox_active)
    # pass


class MainScreen(Screen):
    pass


class TimeDelay(Screen):
    pass


class PrankScreen(Screen):
    pass


class StartScreen(Screen):
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

    def change_screen(self, screen_name):
        """get screen manager id"""
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


if __name__ == "__main__":
    TimeDelayApp().run()