# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 14:53:50 2017

@author: Rei
"""
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Rotate
from kivy.properties import NumericProperty
from time import sleep

    
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout = BoxLayout()
        self.image = Image(source='TrashHold.png', size_hint=(2, 0.9))
        self.btn = Button(text='Start', size_hint=(1, 0.1), on_touch_down=self.switchA)
        self.btn2 = Button(text='Quit', size_hint=(1, 0.1), on_press=self.quitApp)
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.btn2)
        self.add_widget(self.layout)
    def switchA(self,instance, touch):
        self.manager.current = 'choice'
        self.manager.transition.direction = 'left'
    def quitApp(self,instance):
        App.get_running_app().stop()
        
class ChoiceScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout = BoxLayout()
        self.bt1 = Button(text='Bugis', on_press=self.switchC)
        self.bt2 = Button(text='Clementi', on_press=self.switchC)
        self.bt3 = Button(text='Pasir Ris', on_press=self.switchC)
        self.bt4 = Button(text='Bugis', on_press=self.switchC)
        self.layout.add_widget(self.bt1)
        self.layout.add_widget(self.bt2)
        self.layout.add_widget(self.bt3)
        self.layout.add_widget(self.bt4)
        self.add_widget(self.layout)
    def switchC(self,instance):
        self.manager.current = 'map'
        self.manager.transition.direction = 'left'
        
class MapScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout = BoxLayout()
        self.image = Image(source='Map.png', size_hint=(1, 0.9))
        self.btn = Button(text='Analyze Route', size_hint=(0.5, 0.1), on_touch_down=self.path)
        self.btn2 = Button(text='Switch to Menu', size_hint=(0.5, 0.1), on_press=self.switchM)
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.btn2)
        self.add_widget(self.layout)
    def path(self, instance, touch,):
        self.image.source = 'Map2.png'
        self.btn2.text = 'Bin Cleared, Next Route'
    def switchM(self,instance):
        self.manager.current = 'menu'
        self.manager.transition.direction = 'right'
        
class TrashHold(App):
    def build(self):
        sm = ScreenManager()
        s = MapScreen(name='map')
        c = ChoiceScreen(name='choice')
        m = MenuScreen(name='menu')
        sm.add_widget(s)
        sm.add_widget(c)
        sm.add_widget(m)
        sm.current = 'menu'
        return sm
TrashHold().run()