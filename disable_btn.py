import kivy
from kivy.app import App
from kivy.logger import GREEN
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial

class KivyButton(App):

    def disable(self, instance, *args):
        instance.disabled = True

    def update(self, instance, *args):
        instance.text = "Disabled"

    def build(self):

        btn = Button(text="Click me to disable", pos=(50, 50), size_hint=(.25, .18))
        btn.bind(on_press=partial(self.disable))
        btn.bind(on_press=partial(self.update))
        return btn
    
KivyButton().run()