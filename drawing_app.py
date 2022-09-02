# import kivy module    
import kivy  
       
# base Class of your App inherits from the App class.    
# app:always refers to the instance of your application   
from kivy.app import App 
     
# this restrict the kivy version i.e  
kivy.require('1.9.0') 
 
from kivy.uix.widget import Widget
 
from kivy.uix.relativelayout import RelativeLayout
 
# Create the Widget class
class Paint_brush(Widget):
    pass
 
# Create the layout class
# define Paint_brush() class
class Drawing(RelativeLayout):
 
    # On mouse press how Paint_brush behaves
    def on_touch_down(self, touch):
        pb = Paint_brush()
        pb.center = touch.pos
        self.add_widget(pb)
         
    # On mouse movement how Paint_brush behaves
    def on_touch_move(self, touch):