import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
Window.size=(400,600)
Window.color=(1,1,1,0)
class Fapp(App):
    def build(self):
        self.title='Drag App[rakwan]'
        f=FloatLayout()
        s=Scatter()
        l=Label(text='rakwan ali',font_size=22)
        l.pos=(100,300)
        f.add_widget(s)
        s.add_widget(l)
        return f
if __name__=='__main__':
    Fapp().run()
