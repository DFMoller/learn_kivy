import kivy
from kivy.app import App
from kivy.logger import GREEN
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

Builder.load_string('''

<exampleRV>:

    viewclass: 'Button'

    RecycleBoxLayout:

        size_hint_y: None

        height: self.minimum_height

        orientation: 'vertical'

''')

class ExampleRV(RecycleView):

    def __init__(self, **kwargs):

        super(ExampleRV, self).__init__(**kwargs)
        
        self.data = [{'text': str(x)} for x in range(20)]

class RecycleApp(App):
    
    def build(self):
    
        return ExampleRV()
    

RecycleApp().run()