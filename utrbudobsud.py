from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        self.wimg = Image(source='unnamed (1).jpg')
        self.layout.add_widget(self.wimg)

class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        self.kor = MenuScreen(name='boo')
        sm.add_widget(self.kor)
        sm.current_screen='boo'
        return sm

if __name__ == '__main__':
    TestApp().run()