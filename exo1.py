from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SommeApp(App):
    def build(self):
        self.title = 'Somme de 2 nombres'
        box = BoxLayout(orientation='vertical')

        add = BoxLayout(orientation='horizontal')
        self.number1 = TextInput()
        self.number2 = TextInput()
        add.add_widget(self.number1)
        add.add_widget(self.number2)
        btn1 = Button(text="+")
        btn1.bind(on_press=self.add)
        add.add_widget(btn1)

        box.add_widget(add)

        result = BoxLayout(orientation='horizontal')
        self.result_text = Label()
        result.add_widget(self.result_text)

        box.add_widget(result)
        return box

    def add(self, btn1):
        try:
            if btn1:
                calcul = int(self.number1.text) + int(self.number2.text)
                self.result_text.text = str(calcul)
        except:
            self.result_text.text = "SYNTAX ERROR"


Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '50')

SommeApp().run()
