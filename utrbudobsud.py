from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.wimg = Image(source='milogo.jpg')
        self.layout.add_widget(self.wimg)
        self.img = Image(source = "dia.png", pos_hint = {"x":-.1, "y":-.2})
        self.add_widget(self.img)
        self.t1 = Label(text = "привет!", size_hint = (.8, .8), pos_hint= {"x":-.2, "y":-.15})
        self.add_widget(self.t1)
        self.btn = Button(text="next",size_hint = (.1,.1))
        self.add_widget(self.btn)
        self.btn.on_press = self.next
    
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'boo2'
class  MScr(Screen):
    def __init__(self, name='boo2'):
        super().__init__(name=name) 
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.wimg2 = Image(source='fon11.jpg')
        self.layout.add_widget(self.wimg2)
        self.sprite = Image(source = "seles1.png", pos_hint = {"x":-.3, "y":-.2})
        self.add_widget(self.sprite)
        self.img2 = Image(source = "dia.png", pos_hint = {"x":-.1, "y":-.2})
        self.add_widget(self.img2)
        self.t1 = Label(text = "не игнорируйте меня", size = (.10, .10), pos_hint= {"x":-.29, "y":-.25})
        self.add_widget(self.t1)
        self.btn = Button(text="next",size_hint = (.1,.1))
        self.add_widget(self.btn)
        self.btn.on_press = self.next 
    def next(self):    
        self.btn2 =Button(text= "игнорировать", size_hint=(.2 , .1), pos_hint= {"x":.1, "y":.4})
        self.add_widget(self.btn2)
        self.btn3 =Button(text= " не игнорировать", size_hint=(.2 , .1), pos_hint= {"x":.7, "y":.4})
        self.add_widget(self.btn3)
        self.btn2.on_press = self.next1
    def next1(self):
        self.t1.text = "ох как грубо с вашей стороны"
        self.btn3.set_disabled(True)
        self.btn2.set_disabled(True)
        #self.add_widget(self.t1)

    

class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        self.kor = MenuScreen(name='boo')
        self.kor2 =  MScr(name="boo2")
        sm.add_widget(self.kor)
        sm.add_widget(self.kor2)
        
        sm.current='boo'
        return sm

if __name__ == '__main__':
    TestApp().run()