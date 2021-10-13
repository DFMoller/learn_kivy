from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button

class ClockExample(App):
    
    i = 0

    def build(self):

        self.btn = Button(text='Number of Calls')

        Clock.schedule_interval(self.Clock_Callback, 2)

        return self.btn
    
    def Clock_Callback(self, dt):

        self.i = self.i + 1

        self.btn.text = "Call = %d"%self.i

ClockExample().run()