from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *

class GroceryListLayout(FloatLayout):
    def __init__(self, **kwargs):
        # call parent init
        super(GroceryListLayout, self).__init__(**kwargs)
        # draw a red box where the layout is
        self.canvas.add(Color(1,0,0))
        self.canvas.add(Rectangle(pos=(0,0),size=self.size))
    def add_widget(self, widget):
        # place added widgets and space them apart some
        # saw 30 as a good size in some other example...
        widget.height = 30
        widget.y = 35*len(self.children)
        widget.x = 0
        # draw a red box where each added widget is.
        #  expecting red because that's the last color I set in
        #  the canvas (in the constructor)
        self.canvas.add(Rectangle(pos=(widget.x, widget.y), size=(widget.width, widget.height)))
        # actually add the widget via the parent's add_widget method
        super(GroceryListLayout,self).add_widget(widget)

class MyApp(App):
    '''Boilerplate Kivy App Code'''
    def build(self):
        '''Build and return the main widget'''
        # create the main widget with size 300x300
        #  saw this size in the Float Layout docs as an example
        main_widget = GroceryListLayout(size=(300,300))
        # Add labels with grocery items to the widget
        main_widget.add_widget(Label(text="milk"))
        main_widget.add_widget(Label(text="eggs"))
        main_widget.add_widget(Label(text="spam"))
        main_widget.add_widget(Label(text="spam"))
        main_widget.add_widget(Label(text="spam"))
        return main_widget

if __name__ == '__main__':
    # [Kivy App Startup]
    MyApp().run()
