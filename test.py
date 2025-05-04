from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget

class MyApp(App):
    def build(self):
        widget = Widget()
        background = Image(source='Kare_Arka_Plan.jpg', allow_stretch=True, keep_ratio=False)
        widget.add_widget(background)
        return widget

if __name__ == '__main__':
    MyApp().run()
