from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox


class Calculator(App):
    def answer(self, src):
        try:
            self.result_text.text = self.calcul
        except:
            self.result_text.text = "select an operation"

    def substraction(self, instance, src):
        if src:
            try:
                self.calcul = str(int(self.number1.text) - int(self.number2.text))
            except:
                self.calcul = "Error"

    def addition(self, instance, src):
        if src:
            try:
                self.calcul = str(int(self.number1.text) + int(self.number2.text))
            except:
                self.calcul = "Error"

    def multiplication(self, instance, src):
        if src:
            try:
                self.calcul = str(int(self.number1.text) * int(self.number2.text))
            except:
                self.calcul = "Error"

    def division(self, instance, src):
        if src:
            try:
                self.calcul = str(int(self.number1.text) / int(self.number2.text))
            except:
                self.calcul = "Error"

    def build(self):
        self.title = 'calculator'
        box = BoxLayout(orientation='vertical')

        calcul = BoxLayout(orientation='vertical')

        substraction = CheckBox(group='state')
        substraction.bind(active=self.substraction)
        calcul.add_widget(substraction)
        calcul.add_widget(Label(text='-'))

        addition = CheckBox(group='state')
        addition.bind(active=self.addition)
        calcul.add_widget(addition)
        calcul.add_widget(Label(text='+'))

        multiplication = CheckBox(group='state')
        multiplication.bind(active=self.multiplication)
        calcul.add_widget(multiplication)
        calcul.add_widget(Label(text='*'))

        division = CheckBox(group='state')
        division.bind(active=self.division)
        calcul.add_widget(division)
        calcul.add_widget(Label(text='/'))

        box.add_widget(calcul)

        operation = BoxLayout(orientation='horizontal')
        self.number1 = TextInput()
        self.number2 = TextInput()
        button = Button(text="=")
        button.bind(on_press=self.answer)
        operation.add_widget(self.number1)
        operation.add_widget(self.number2)
        operation.add_widget(button)
        box.add_widget(operation)

        result = BoxLayout(orientation='horizontal')
        self.result_text = Label()
        result.add_widget(self.result_text)
        box.add_widget(result)

        return box


Config.set('graphics', 'width', '1')
Config.set('graphics', 'height', '1')

if __name__ == "__main__":
    Calculator().run()
