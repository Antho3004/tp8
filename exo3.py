from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random


def change_color(button):
    color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    button.background_color = random.choice(color)


class Grid(App):

    def build(self):
        self.title = 'Grid'
        grid = GridLayout(rows=5, cols=5)
        list_button = []
        for i in range(25):
            list_button.append(Button(background_color='white'))
            list_button[i].bind(on_press=change_color)
            grid.add_widget(list_button[i])

        return grid


Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

if __name__ == "__main__":
    Grid().run()
