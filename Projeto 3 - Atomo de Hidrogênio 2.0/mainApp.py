from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MainWindow(Screen):
    pass

class EnergyWindow(Screen):
    def show_answer(self, title, text):
        Popups.BuildPop(self, title, text)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

class Popups(Popup):
    def BuildPop(self, title, text):
        self.box = FloatLayout()

        self.lab = (Label(text=text, font_size=15,
                          size_hint=(None, None), pos_hint={'x':.4, 'y':.5 }))
        self.box.add_widget(self.lab)

        self.but = (Button(text="Close", size_hint=(None, None),
                           width=200, height=50, pos_hint={'x': 0.25, 'y': 0}))
        self.box.add_widget(self.but)

        self.main_pop = Popup(title=title, content=self.box,
                              size_hint=(None, None), size=(450, 450), auto_dismiss=False, title_size=15)

        self.but.bind(on_press=self.main_pop.dismiss)

        self.main_pop.open()


class MyMainWindow(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyMainWindow().run()