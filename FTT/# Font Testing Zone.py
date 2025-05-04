from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup 
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.image import Image

font_path2 = r"PressStart2P-Regular.ttf"
LabelBase.register(name="MyFont1",fn_regular=font_path2)    


font_path3 = r"Hesiga Font DEMO.ttf"
LabelBase.register(name="MyFont2_2_2_2",fn_regular=font_path3)    


font_path4 = r"Honk-Regular-VariableFont_MORF,SHLN.ttf"
LabelBase.register(name="MyFont3_2_2_2",fn_regular=font_path4)    


font_path5 = r"Isabela Dokeef Demo.otf"
LabelBase.register(name="MyFont4_2_2_2",fn_regular=font_path5)    


font_path6 = r"Piloom Font DEMO.ttf"
LabelBase.register(name="MyFont5_2_2_2",fn_regular=font_path6)    


font_path7 = r"Rainbow Christmas.otf"
LabelBase.register(name="MyFont6_2_2_2_2",fn_regular=font_path7)    


font_path8 = r"28 Days Later.ttf"
LabelBase.register(name="MyFont7_2_2_2_2",fn_regular=font_path8)    


font_path9 = r"Busines Signature.otf"
LabelBase.register(name="MyFont8_2_2_2_2",fn_regular=font_path9)    


font_path10 = r"Scary Story.otf"
LabelBase.register(name="MyFont9_2_2_2_2",fn_regular=font_path10)    


font_path11 = r"Simple Santa.otf"
LabelBase.register(name="MyFont10_2_2_2_2",fn_regular=font_path11)    


font_path12 = r"Summer Christmas.otf"
LabelBase.register(name="MyFont11_2_2_2_2",fn_regular=font_path12)    


font_path13 = r"Sunshine.otf"
LabelBase.register(name="MyFont12_2_2_2_2",fn_regular=font_path13)    

####
font_path14 = r"Anton-Regular.ttf"
LabelBase.register(name="MyFont13",fn_regular=font_path14)    


font_path15 = r"BebasNeue-Regular.ttf"
LabelBase.register(name="MyFont14",fn_regular=font_path15)    


font_path16 = r"LondrinaSketch-Regular.ttf"
LabelBase.register(name="MyFont15",fn_regular=font_path16)    


font_path17 = r"NotoSansSC-VariableFont_wght.ttf"
LabelBase.register(name="MyFont16",fn_regular=font_path17)    


font_path18 = r"Orbitron-VariableFont_wght.ttf"
LabelBase.register(name="MyFont17",fn_regular=font_path18)    





font_path = r"Rubik.ttf"

LabelBase.register(name="MyFont",fn_regular=font_path)

class FontConverterApp(App):
    def build(self):
        Window.fullscreen =  True
        Window.size = (1920,800)
        Window.clearcolor = (0,1,0.4)
        self.layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Font Converter 1.0'a hoşgeldiniz",size_hint=(None,None),size=(150,150))
        self.button = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont1",font_size="7sp")
        self.button2 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont2_2_2_2",font_size="15sp")
        self.button3 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont3_2_2_2",font_size="15sp")
        self.button4 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont4_2_2_2",font_size="15sp")
        self.button5 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont5_2_2_2",font_size="15sp")
        self.button6 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont6_2_2_2_2",font_size="25sp")
        self.button7 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont7_2_2_2_2",font_size="15sp")
        self.button8 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont8_2_2_2_2",font_size="15sp")
        self.button9 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont9_2_2_2_2",font_size="15sp")
        self.button10 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont10_2_2_2_2",font_size="15sp")
        self.button11 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont11_2_2_2_2",font_size="15sp")
        self.button12 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont12_2_2_2_2",font_size="15sp")
        self.button14 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont14",font_size="15sp")
        self.button15 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont15",font_size="15sp")
        self.button16 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont16",font_size="15sp")
 
        self.button18 = Button(text="Press Start 2p",size_hint=(None,None),size=(150,60),font_name="MyFont17",font_size="15sp") 
        self.button2.font_name = "MyFont2_2_2_2"      
        self.text_input = TextInput(text="",size_hint=(None,None),size=(1250,200),hint_text="Birşeyler Yazın",font_name="MyFont",font_size="15sp")
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button) 
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button2)
        self.layout.add_widget(self.button3)
        self.layout.add_widget(self.button4)
        self.layout.add_widget(self.button5)
        self.layout.add_widget(self.button6)
        self.layout.add_widget(self.button7)
        self.layout.add_widget(self.button8)
        self.layout.add_widget(self.button9)
        self.layout.add_widget(self.button10) 
        self.layout.add_widget(self.button11)
        self.layout.add_widget(self.button12)
        self.layout.add_widget(self.button14)
        self.layout.add_widget(self.button15)
        self.layout.add_widget(self.button16)
        self.layout.add_widget(self.button18)
        self.text_input.font_size = "35sp"


        self.button.bind(on_press=self.press_start_2p)
        self.button2.bind(on_press=self.press_start_3p)
        self.button3.bind(on_press=self.press_start_4p)
        self.button4.bind(on_press=self.press_start_5p)
        self.button5.bind(on_press=self.press_start_6p)
        self.button7.bind(on_press=self.press_start_7p)
        self.button8.bind(on_press=self.press_start_8p)
        self.button9.bind(on_press=self.press_start_9p)
        self.button10.bind(on_press=self.press_start_10p)
        self.button11.bind(on_press=self.press_start_11p)
        self.button12.bind(on_press=self.press_start_12p)
        self.button14.bind(on_press=self.press_start_14p)
        self.button15.bind(on_press=self.press_start_15p)
        self.button16.bind(on_press=self.press_start_16p)             
        self.button18.bind(on_press=self.press_start_17p)    
        return self.layout
    def on_start(self,*args):
        anim1 = Animation(x=650,y=800)
        anim1.start(self.text_input)
        anim2 = Animation(x=200,y=400)
        anim2.start(self.button)
        anim3 = Animation(x=50,y=400)
        anim3.start(self.button2)
        anim4 = Animation(x=350,y=400)
        anim4.start(self.button3)
        anim5 = Animation(x=500,y=400)
        anim5.start(self.button4)
        anim6 = Animation(x=650,y=400)
        anim6.start(self.button5)           
        anim7 = Animation(x=800,y=400)
        anim7.start(self.button6)  
        anim8 = Animation(x=950,y=400)
        anim8.start(self.button7)   
        anim9 = Animation(x=1100,y=400)
        anim9.start(self.button8)
        anim10 = Animation(x=1250,y=400)
        anim10.start(self.button9)
        anim11 = Animation(x=1400,y=400)
        anim11.start(self.button10)
        anim12 = Animation(x=1550,y=400)
        anim12.start(self.button11)
        anim13 = Animation(x=1700,y=400)
        anim13.start(self.button12)
        anim14 = Animation(x=800,y=300)
        anim14.start(self.button14)           
        anim15 = Animation(x=650,y=300) 
        anim15.start(self.button15)  
        anim16 = Animation(x=950,y=300)
        anim16.start(self.button16)  
        anim17 = Animation(x=800,y=300)
        anim17.start(self.button18)                             
    def press_start_2p(self,*args):
        font_path2_1 = r"PressStart2P-Regular.ttf"
        LabelBase.register(name="MyFont2",fn_regular=font_path2_1)    
        self.text_input.font_name = "MyFont2"
    def press_start_3p(self,*args):
        font_path2_2 = r"Hesiga Font DEMO.ttf"
        LabelBase.register(name="MyFont3",fn_regular=font_path2_2)    
        self.text_input.font_name = "MyFont2_2_2_2"
    def press_start_4p(self,*args):
        font_path2_3 = r"Honk-Regular-VariableFont_MORF,SHLN.ttf"
        LabelBase.register(name="MyFont4",fn_regular=font_path2_3)    
        self.text_input.font_name = "MyFont3_2_2_2"
    def press_start_5p(self,*args):
        font_path2_4 = r"Isabela Dokeef Demo.otf"
        LabelBase.register(name="MyFont5",fn_regular=font_path2_4)    
        self.text_input.font_name = "MyFont4_2_2_2"
    def press_start_6p(self,*args):
        font_path2_5 = r"Piloom Font DEMO.ttf"
        LabelBase.register(name="MyFont6",fn_regular=font_path2_5)    
        self.text_input.font_name = "MyFont5_2_2_2"   
    def press_start_7p(self,*args):
        font_path2_7 = r"28 Days Later.ttf"
        LabelBase.register(name="MyFont7",fn_regular=font_path2_7)    
        self.text_input.font_name = "MyFont7"      
    def press_start_8p(self,*args):
        font_path2_8 = r"Busines Signature.otf"
        LabelBase.register(name="MyFont8",fn_regular=font_path2_8)    
        self.text_input.font_name = "MyFont8"
    def press_start_9p(self,*args):
        font_path2_9 = r"Scary Story.otf"
        LabelBase.register(name="MyFont9",fn_regular=font_path2_9)    
        self.text_input.font_name = "MyFont9"
    def press_start_10p(self,*args):
        font_path2_10 = r"Simple Santa.otf"
        LabelBase.register(name="MyFont10",fn_regular=font_path2_10)    
        self.text_input.font_name = "MyFont10"
    def press_start_11p(self,*args):
        font_path2_11 = r"Summer Christmas.otf"
        LabelBase.register(name="MyFont11",fn_regular=font_path2_11)    
        self.text_input.font_name = "MyFont11"
    def press_start_12p(self,*args):
        font_path2_12 = r"Sunshine.otf"
        LabelBase.register(name="MyFont12",fn_regular=font_path2_12)    
        self.text_input.font_name = "MyFont12"                                             
    def press_start_8p(self,*args):
        font_path2_8 = r"Busines Signature.otf"
        LabelBase.register(name="MyFont8",fn_regular=font_path2_8)    
        self.text_input.font_name = "MyFont8"
    def press_start_9p(self,*args):
        font_path2_9 = r"Scary Story.otf"
        LabelBase.register(name="MyFont9",fn_regular=font_path2_9)    
        self.text_input.font_name = "MyFont9"
    def press_start_10p(self,*args):
        font_path2_10 = r"Simple Santa.otf"
        LabelBase.register(name="MyFont10",fn_regular=font_path2_10)    
        self.text_input.font_name = "MyFont10"
    def press_start_11p(self,*args):
        font_path2_11 = r"Summer Christmas.otf"
        LabelBase.register(name="MyFont11",fn_regular=font_path2_11)    
        self.text_input.font_name = "MyFont11"
    def press_start_12p(self,*args):
        font_path2_12 = r"Sunshine.otf"
        LabelBase.register(name="MyFont12",fn_regular=font_path2_12)    
        self.text_input.font_name = "MyFont12"                  
    def press_start_14p(self,*args):
        font_path2_14 = r"Anton-Regular.ttf"
        LabelBase.register(name="MyFont12",fn_regular=font_path2_14)    
        self.text_input.font_name = "MyFont14"         
    def press_start_15p(self,*args):
        font_path2_15 = r"BebasNeue-Regular.ttf"
        LabelBase.register(name="MyFont12",fn_regular=font_path2_15)    
        self.text_input.font_name = "MyFont15"         
    def press_start_16p(self,*args):
        font_path2_16 = r"LondrinaSketch-Regular.ttf"
        LabelBase.register(name="MyFont12",fn_regular=font_path2_16)    
        self.text_input.font_name = "MyFont16"         
    def press_start_17p(self,*args):
        font_path2_17 = r"NotoSansSC-VariableFont_wght.ttf"
        LabelBase.register(name="MyFont12",fn_regular=font_path2_17)    
        self.text_input.font_name = "MyFont17"         
         

FontConverterApp().run()    

        