from firebase import firebase
import time as time

url = "https://iot-dw-1d-2017.firebaseio.com/" # URL to Firebase database
token = "0lYSxo2k1Jrr3i3rxhyb3IFy3kTKEAsXP39n3mpV" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)
vals = [0.0,0.0,0.0,0.0] #initialize a value list for the inputs so that kivy can boot
wtv = [] #empty list used to replace vals list
from kivy.app import App
from kivy.lang import Builder #use builder to run the kivy code on the R-pi
infrared =  firebase.get('/BinA/Infrared') # get the value from the node infrared
#print infrared
methane = firebase.get('/BinA/Methane') #get value from node methane
#print methane
ultrasound = firebase.get('/BinA/Ultrasound') #get value from node ultrasound
#print ultrasound
coefficients = firebase.get('/coefficients') # get linear regression cofficients
# methane =  firebase.get('/Methane') #get value from methane node
# ultrasound = firebase.get('/Ultrasound')
if type(infrared) == str: #by default (before startup and after the sensors end), the values in firebase will be 0. If infrared has a string, it is triggered
    infrared = 1.0
else:
    infrared = 0.0
if ultrasound == 0: #by default, we set the value of the ultrasound sensor to be 25, as this balances the linear regression model.
    ultrasound = 25.0
if methane == 0: #by default, the methane sensor value is 0. It is 1 only if ppm greater than 250.
    methane = 0.0

# def keywithmaxval():
#     pass
dict_routes = {}

Builder.load_file("trashold.kv") #load file manually (normally python looks for a kivy file in the same directory, but this does not work in the raspberry pi)
#Layout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.floatlayout import FloatLayout

#Widgets
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.button import Button 
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

#Graphics
from kivy.graphics.vertex_instructions import (Rectangle, Line, Ellipse)
from kivy.graphics.context_instructions import Color
from kivy.utils import get_color_from_hex as hex 


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)

    def switchI(self):
        self.manager.current = 'input' #change to input screen
        self.manager.transition.direction = 'up' 

    def quitApp(self):
        App.get_running_app().stop() #end the app
        

class InputScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)

    def switchC(self):
        self.manager.current = 'choice' #change to choice screen
        self.manager.transition.direction = 'up'

    def switchM(self):
        self.manager.current = 'menu' #change to menu screen
        self.manager.transition.direction = 'down'

    
    def getvals(self, value):
        #try:
        wtv.append(value) #get slider values and add them to the empty list wtv
        # except:
        #     self.manager.current = 'menu'
        #     self.manager.transition.direction = 'down'
            # print 'me too thanks'
            
        if len(wtv) != 4:
            pass
        else:
            vals[0] = wtv.pop(0) #remove first value from wtv and replace the first value of vals with it. It is important to do this because we want the inputs to reset after each route analysis
            vals[1] = wtv.pop(0)
            vals[2] = wtv.pop(0)
            vals[3] = wtv.pop(0)
        #print vals
        return vals


class ChoiceScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        # self.layout = GridLayout(cols=2)
        # self.bt1 = Button(background_normal='bugis1.png',size_hint=(0.5,0.5), on_press=self.switchC)
        # self.bt2 = Button(background_normal='clementi1.png',size_hint=(0.5,0.5), on_press=self.switchC)
        # self.bt4 = Button(background_normal='pasirris1.png',size_hint=(0.5,0.5), on_press=self.switchC)
        # self.bt3 = Button(background_normal='hougang1.png',size_hint=(0.5,0.5), on_press=self.switchC)
        
        # self.layout.add_widget(self.bt1)
        # self.layout.add_widget(self.bt2)
        # self.layout.add_widget(self.bt4)
        # self.layout.add_widget(self.bt3)
        # self.add_widget(self.layout)
    
    def switchM(self):
        self.manager.current = 'map'
        self.manager.transition.direction = 'up'

    def switchL(self):
        self.manager.current = 'location'
        self.manager.transition.direction = 'up'

    def switchI(self):
        self.manager.current = 'input'
        self.manager.transition.direction = 'down'


class LocationScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
    
    def switchM(self):
        # self.manager.current = 'map'
        # self.manager.transition.direction = 'up'
        pass

    def switchC(self):
        self.manager.current = 'choice'
        self.manager.transition.direction = 'down'

        
class MapScreen(Screen):
    
    def main(self,instance): #main function that is called whenever the Analyze route button is pressed
        #print 'main'
        def algo(x,y):
            return coefficients[0]*x**2-coefficients[2]*x+coefficients[1]*y**2+coefficients[3]*y,25.0-x,y #algorithm that utilizes the coefficients from the linear regression code
        # state = False
        # def state(self):
        #     state = not state
        #     return state

        #while state:
        P_A,height_A,methane_A = algo(ultrasound,methane) #determine priority levels for A,B and C. This can be extended to any number of bins
        #print vals,wtv
        P_B,height_B,methane_A = algo(vals[0],vals[1])
        P_C,height_C,methane_C = algo(vals[2],vals[3])
        dict_routes = {}
        #print P_A,P_B,P_C

        P_BAC = 1/((6*P_B+15*P_A+28*P_C)*34) #formula to determine the probabilty of a certain route to be chosen
        P_ABC = 1/((12*P_A+21*P_B+34*P_C)*40)
        P_BCA = 1/((6*P_B+20*P_C+33*P_A)*39)
        P_ACB = 1/((12*P_A+25*P_C+38*P_B)*39)
        P_CBA = 1/((12*P_C+25*P_B+34*P_A)*40)
        P_CAB = 1/((12*P_C+24*P_A+33*P_B)*36)

        dict_routes['BAC'] = P_BAC #adding the keys and values to the empty dictionary defined earlier
        dict_routes['CAB'] = P_CAB
        dict_routes['CBA'] = P_CBA
        dict_routes['ACB'] = P_ACB
        dict_routes['BCA'] = P_BCA
        dict_routes['ABC'] = P_ABC

           # time.sleep(20)

        def keywithmaxval(d):
            """ a) create a list of the dict's keys and values;
                b) return the key with the max value"""

            v = list(d.values())
            k = list(d.keys())
            return k[v.index(max(v))]
        TheRoute =  keywithmaxval(dict_routes)  
        return TheRoute

    
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)

        # with self.canvas:
        #     Color(1, 0, 0, 1)  # set the colour to red
        #     self.rect = Rectangle(pos=self.pos,size=self.size)
        #self.state = self.path
        self.route = 'ACB' #define initial list, because kivy requires an initial value to run. We will change this later
        #self.route = keywithmaxval(dict_routes)
        #print self.route
        self.count = 0 #initialize a count to keep track of the current map
        self.layout = BoxLayout(orientation='vertical')
        self.nested = BoxLayout(orientation='horizontal', size_hint_y = 0.11) #create a nested boxlayout
        self.image = Image(source='Map1.png', allow_stretch = False )
        self.btn = Button(text='Analyze Route', color = hex('#151712'), on_press=self.main, on_release=self.path, font_size = 24, font_name = 'Adam', background_normal = '', background_color = hex('#83A55C'))
        self.btn2 = Button(text = 'Return to Menu', color = hex('#151712'), on_press=self.switchM, font_size = 24, font_name = 'Adam', background_normal = '', background_color = hex('#A93F55'))
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.nested)
        self.nested.add_widget(self.btn)
        self.nested.add_widget(self.btn2)
        self.add_widget(self.layout)
   

    def path(self, instance): #depending on user input/sensor input, the path will be determined by the algorithm
        self.count += 1
        self.route = self.main(Screen)
        #print self.route
        if self.route == 'ABC': #for the purposes of this project, we determine the routes in advance. However in a full implementation, we will use maps api to generate the routes.
            if self.count == 1:
                self.image.source = 'ADA2.png'
                self.btn.text = 'Bin cleared. Next route!'
            elif self.count == 2: 
                self.image.source = 'AAB2.png'
            elif self.count == 3: 
                self.image.source = 'ABC2.png'
            elif self.count >= 4: 
                self.image.source = 'ACD2.png'
                self.btn.text = 'All bins cleared!'
                self.btn.background_color = hex('#CBCEEE')

        if self.route == 'ACB':
            if self.count == 1:
                self.image.source = 'ADA2.png'
                self.btn.text = 'Bin cleared. Next route!'
            elif self.count == 2: 
                self.image.source = 'AAC2.png'
            elif self.count == 3: 
                self.image.source = 'ACB2.png'
            elif self.count >= 4: 
                self.image.source = 'ABD2.png'
                self.btn.text = 'All bins cleared!'
                self.btn.background_color = hex('#CBCEEE')

        if self.route == 'BAC':
            if self.count == 1:
                self.image.source = 'ADB2.png'
                self.btn.text = 'Bin cleared. Next route!'
            elif self.count == 2: 
                self.image.source = 'ABA2.png'
            elif self.count == 3: 
                self.image.source = 'AAC2.png'
            elif self.count >= 4: 
                self.image.source = 'ACD2.png'
                self.btn.text = 'All bins cleared!'
                self.btn.background_color = hex('#CBCEEE')

        if self.route == 'BCA':
            if self.count == 1:
                self.image.source = 'ADB2.png'
                self.btn.text = 'Bin cleared. Next route!'
            elif self.count == 2: 
                self.image.source = 'ABC2.png'
            elif self.count == 3: 
                self.image.source = 'ACA2.png'
            elif self.count >= 4: 
                self.image.source = 'AAD2.png'
                self.btn.text = 'All bins cleared!'
                self.btn.background_color = hex('#CBCEEE')

        if self.route == 'CAB':
            if self.count == 1:
                self.image.source = 'ADC2.png'
                self.btn.text = 'Bin cleared. Next route!'
            elif self.count == 2: 
                self.image.source = 'ACA2.png'
            elif self.count == 3: 
                self.image.source = 'AAB2.png'
            elif self.count >= 4: 
                self.image.source = 'ABD2.png'
                self.btn.text = 'All bins cleared!'
                self.btn.background_color = hex('#CBCEEE')

        if self.route == 'CBA':
            if self.count == 1:
                self.image.source = 'ADC2.png'
                self.btn.text = 'Bin cleared. Next route!'
            elif self.count == 2: 
                self.image.source = 'ACB2.png'
            elif self.count == 3: 
                self.image.source = 'ABA2.png'
            elif self.count >= 4: 
                self.image.source = 'AAD2.png'
                self.btn.text = 'All bins cleared!'
                self.btn.background_color = hex('#CBCEEE')

            # elif self.count > 4:
            #     self.btn = Button(text = 'hi', on_press=self.switchC)

    def switchM(self,instance): #changes back to the menu screen when the return to menu button is pressed
        self.image.source = 'Map1.png' #sets the map screen back to the empty map
        self.btn.text = 'Analyze Route' #replaces the text with the original text
        self.btn.background_color = hex('#83A55C')
        self.count = 0 #reverts count back to zero
        self.manager.current = 'menu' #goes back to menu screen
        vals = [0.0,0.0,0.0,0.0] #revert vals back to original list
        self.manager.transition.direction = 'down'
        
        

    # def switchC(self, instance):
    #     self.count = 0
    #     self.manager.current = 'choice'
    #     self.manager.transition.direction = 'right'


class TrasholdApp(App):
    def build(self):
        self.icon = 'icon.png' #create custom kivy icon
        sm = ScreenManager() #use screen manager to easily switch between screens
        i = InputScreen(name='input')
        s = MapScreen(name='map')
        c = ChoiceScreen(name='choice')
        m = MenuScreen(name='menu')
        l = LocationScreen(name='location')
        sm.add_widget(i)
        sm.add_widget(s)
        sm.add_widget(c)
        sm.add_widget(m)
        sm.add_widget(l)
        sm.current = 'menu'
        return sm
    
TrasholdApp().run()
