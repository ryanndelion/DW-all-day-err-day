# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:43:23 2017

@author: Rei
"""
#Extra uses

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#Note: for MenuScreen SwitchA function, change self.manager.current from 'choice' to 'input'

class InputScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.innerlayout = GridLayout(cols=2)
        self.title = Label(text='Due to our group only having one prototype for just 1 bin, we have to choose values for the other 2 bins')
        self.layout.add_widget(self.title)
        self.bus = Label(text='Bin B Ultrasonic Value (Lower indicates more rubbish)')
        self.b_us = (TextInput(multiline=False, text = '0', input_filter='float'))
        self.innerlayout.add_widget(self.bus)
        self.innerlayout.add_widget(self.b_us)
        self.bms = Label(text='Bin B Methane Value (Higher indicates greater methane emission)')
        self.b_ms = (TextInput(multiline=False, text = '0',input_filter='float'))
        self.innerlayout.add_widget(self.bms)
        self.innerlayout.add_widget(self.b_ms)
        self.cus = Label(text='Bin C Ultrasonic Value (Lower indicates more rubbish)')
        self.c_us = (TextInput(multiline=False, text = '0',input_filter='float'))
        self.innerlayout.add_widget(self.cus)
        self.innerlayout.add_widget(self.c_us)
        self.cms = Label(text='Bin C Methane Value (Higher indicates greater methane emission)')
        self.c_ms = (TextInput(multiline=False, text = '0',input_filter='float'))
        self.innerlayout.add_widget(self.cms)
        self.innerlayout.add_widget(self.c_ms)
        self.layout.add_widget(self.innerlayout)
        self.btn = Button(text='Next', on_press=self.switchB)
        self.layout.add_widget(self.btn)
        self.add_widget(self.layout)
    def switchB(self,instance):
        self.manager.current = 'choice'
        self.manager.transition.direction = 'left'
        
class TrashHold(App):
    def build(self):
        sm = ScreenManager()
        s = MapScreen(name='map')
        i = InputScreen(name='input')
        c = ChoiceScreen(name='choice')
        m = MenuScreen(name='menu')
        sm.add_widget(s)
        sm.add_widget(i)
        sm.add_widget(c)
        sm.add_widget(m)
        sm.current = 'menu'
        return sm