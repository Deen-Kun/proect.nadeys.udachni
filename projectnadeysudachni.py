from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        lab1 = BoxLayout(orientation="horizontal")
        #btn = Button(text="1",size_hint = (.4,.1),pos=(1000, 100))
        self.i1 = AsyncImage(source='mylogo.jpg')
        self.add_widget(lab1)
        #lab1.add_widget(btn)
        lab1.add_widget(self.i1)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        sm.current='first'
        return sm
    

app = MyApp()
app.run()