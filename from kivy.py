from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        layout = FloatLayout()  # Use FloatLayout for better positioning
        background = Image(source="Kare_Arka_Plan.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        return layout

if __name__ == "__main__":
    MyApp().run()
