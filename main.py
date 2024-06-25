import numpy as np 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.image import Image


class DiceSimImage(Image):
   def __init__(self,app, **kwargs):
        super(DiceSimImage,self).__init__(**kwargs)
        self.app=app
   def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.app.roll_dice()
            return True
        return super(DiceSimImage,self).on_touch_down(touch)
    
class DiceSimApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.image=DiceSimImage(app=self,source='dice1.png')
        self.layout.add_widget(self.image)
        return self.layout
    
    def roll_dice(self):
            dice_face = np.random.randint(1, 7)
            self.image.source = f'dice{dice_face}.png'

if __name__=="__main__":
    DiceSimApp().run()
