from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import analisaEntrada as analiseComp


class MainWindow(Screen):
    pass

class EnergyWindow(Screen):
    def show_answer(self, title, text):
        Popups.BuildPop(self, title, text)

class WaveLengthWindow(Screen):
    def show_answer(self, title, text):
        Popups.BuildPop(self, title, text)
    def chosenSerie(self, title, option):
        Popups.SeriePop(self, title, option)

    def trataSerie(self, ni, nf, serie):
        if nf == None:
            serie = serie.split(" ")
            info = analiseComp.getInputSerie(ni, serie[2])
            return self.show_answer(info[0], info[1])
        else:
            info = analiseComp.getInputComp(ni,nf)
            return self.show_answer(info[0], info[1])

class AbsorberPhoton(Screen):
    pass

class WindowManager(ScreenManager):
    pass

#kv = Builder.load_file("main.kv")
kv = Builder.load_string(open("main.kv", encoding="utf-8").read())
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

    def SeriePop(self, title, option):
        self.box = FloatLayout()

        self.labni = (Label(text="Digite o numero quântico N Inicial:", font_size=15,size_hint=(None, None), pos_hint={'x': .4, 'y': .72}))
        self.box.add_widget(self.labni)

        self.inpni = (TextInput(hint_text="Enter (ni)", multiline=False, pos_hint={"x": 0.35, "y": 0.67}, size_hint=(0.3, 0.07)))
        self.box.add_widget(self.inpni)

        if option == 2:
            self.labnf = (Label(text="Digite o numero quântico N Final:", font_size=15, size_hint=(None, None),pos_hint={'x': .4, 'y': .43}))
            self.box.add_widget(self.labnf)

            self.inpnf = (TextInput(hint_text= "Enter (nf)", multiline=False, pos_hint= {"x":0.35, "y":0.39}, size_hint= (0.3,0.07)))
            self.box.add_widget(self.inpnf)

        self.but = (Button(text="Confirmar", size_hint=(None, None), width=200, height=50, pos_hint={'x': 0.33, 'y': 0.2}))
        self.box.add_widget(self.but)

        self.butExit = (Button(text="Close", size_hint=(None, None), width=200, height=50, pos_hint={'x': 0.33, 'y': 0}))
        self.box.add_widget(self.butExit)

        self.main_pop = Popup(title=title, content=self.box, size_hint=(None, None), size=(600, 600), auto_dismiss=False, title_size=15)

        if option == 2:
            self.but.bind(on_press = lambda x:self.trataSerie(self.inpni.text, self.inpnf.text, title))
        else:
            self.but.bind(on_press=lambda x: self.trataSerie(self.inpni.text, None, title))

        self.butExit.bind(on_press=self.main_pop.dismiss)

        self.main_pop.open()

        def teste():
            print("a")


class MyMainWindow(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyMainWindow().run()