"""
CP1404/CP5632 Practical
Kivy GUI program to convert m to miles
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_CONST = 0.000621371192


class ConvertMtoKm(App):
    miles = StringProperty()

    def build(self):
        Window.size = (400, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.miles = str(float(self.root.ids.input_number.text) * MILES_CONST)
        return self.root

    def convert_m_to_km(self, m):
        self.miles = str(float(m) * MILES_CONST)

    def increase_m(self, m):
        self.root.ids.input_number.text = str(m + 1)

    def decrease_m(self, m):
        self.root.ids.input_number.text = str(m - 1)


ConvertMtoKm().run()
