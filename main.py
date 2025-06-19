from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Window.clearcolor = (0.15, 0.15, 0.15, 1)  

class TempConv(GridLayout):
    def build(self):
        self.cols = 1
        self.padding = [30, 30, 30, 30]
        self.spacing = 20

        self.title = Label(
            text="Temperature Converter",
            font_size=32,
            bold=True,
            color=(0.2, 1, 1, 1)
        )
        self.add_widget(self.title)

        self.input_label = Label(text="Enter Temperature:", font_size=20, color=(1, 1, 1, 1))
        self.add_widget(self.input_label)

        self.input_temp = TextInput(
            multiline=False,
            font_size=20,
            hint_text="100",
            background_color=(0.25, 0.25, 0.25, 1),
            foreground_color=(1, 1, 1, 1),
            padding_y=(10, 10),
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.input_temp)

        self.from_label = Label(text="Convert From:", font_size=18, color=(1, 1, 1, 1))
        self.add_widget(self.from_label)

        self.from_unit = Spinner(
            text="",
            values=["Celsius", "Fahrenheit", "Kelvin"],
            size_hint=(1, None),
            height=40,
            background_color=(0.3, 0.3, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.from_unit)

        self.to_label = Label(text="Convert To:", font_size=18, color=(1, 1, 1, 1))
        self.add_widget(self.to_label)

        self.to_unit = Spinner(
            text="",
            values=["Celsius", "Fahrenheit", "Kelvin"],
            size_hint=(1, None),
            height=40,
            background_color=(0.3, 0.3, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.to_unit)

        self.convert_button = Button(
            text="Convert",
            font_size=20,
            background_color=(0, 0.6, 0.4, 1),
            color=(1, 1, 1, 1),
            bold=True,
            size_hint=(1, None),
            height=50
        )
        self.convert_button.bind(on_press=self.convert_temp)
        self.add_widget(self.convert_button)

        self.result_label = Label(
            text="",
            font_size=22,
            color=(1, 0.8, 0.4, 1),
            bold=True
        )
        self.add_widget(self.result_label)

    def convert_temp(self, instance):    
            value = float(self.input_temp.text)
            from_Unit = self.from_unit.text
            to_Unit = self.to_unit.text

            if from_Unit == to_Unit:
                result = value
            elif from_Unit == "Celsius" and to_Unit == "Fahrenheit":
                result = (value * 9 / 5) + 32
            elif from_Unit == "Celsius" and to_Unit == "Kelvin":
                result = value + 273.15
            elif from_Unit == "Fahrenheit" and to_Unit == "Celsius":
                result = (value - 32) * 5 / 9
            elif from_Unit == "Fahrenheit" and to_Unit == "Kelvin":
                result = ((value - 32) * 5 / 9) + 273.15
            elif from_Unit == "Kelvin" and to_Unit == "Celsius":
                result = value - 273.15
            elif from_Unit == "Kelvin" and to_Unit == "Fahrenheit":
                result = ((value - 273.15) * 9 / 5) + 32
            else:
                self.result_label.text = "Invalid conversion"
                return

            self.result_label.text = f"{value} {from_Unit} = {round(result, 2)} {to_Unit}"
        
        


class TempConverterApp(App):
    def build(self):
        converter = TempConv()
        converter.build()
        return converter


if __name__ == "__main__":
    TempConverterApp().run()
