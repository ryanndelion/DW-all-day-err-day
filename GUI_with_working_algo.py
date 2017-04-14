# -*- coding: utf-8 -*-
"""
Created on Sat Apr 8 05:16:08 2017

@author: Rei
"""

import numpy as np
from sklearn import linear_model
from scipy import stats
from sklearn.metrics import r2_score
class LinearRegression(linear_model.LinearRegression):
    """
    LinearRegression class after sklearn's, but calculate t-statistics
    and p-values for model coefficients (betas).
    Additional attributes available after .fit()
    are `t` and `p` which are of the shape (y.shape[1], X.shape[1])
    which is (n_features, n_coefs)
    This class sets the intercept to 0 by default, since usually we include it
    in X.
    """

    def _init_(self, *args, **kwargs):
        if not "fit_intercept" in kwargs:
            kwargs['fit_intercept'] = False
        super(LinearRegression, self)\
                ._init_(*args, **kwargs)

    def fit(self, X, y, n_jobs=1):
        self = super(LinearRegression, self).fit(X, y, n_jobs)

        sse = np.sum((self.predict(X) - y) ** 2, axis=0) / float(X.shape[0] - X.shape[1])
        se = np.array([np.sqrt(np.diagonal(sse * np.linalg.inv(np.dot(X.T, X))))])
        self.t = self.coef_ / se
        self.p = 2 * (1 - stats.t.cdf(np.abs(self.t), y.shape[0] - X.shape[1]))
        return self
def exponent(x,n):
    for i in range(len(x)):
        # if x[i] < 0 and n%2 == 0:
        #     x[i] = -x[i]**n
        # else:
        x[i] = x[i]**n
    return x
x = [[-4,2,-1,12,15,-5,-3,1,-5,25],[1.834,400,1.834,220,1.834,250,150,400,320,0]]
y = [1.8666666666666667,3.533333333333333,1.3333333333333335,4.0,0.8666666666666667,3.6,3.4,3.533333333333333,3.2,0]
#x.append(exponent(x[0],2))
x.append(x[0])
x.append(x[1])

x_list = np.array(x)
y_list = np.array(y)
x_list[0] = exponent(x_list[0],2)
x_list[1] = exponent(x_list[1],2)
clf = LinearRegression()
clf.fit(np.transpose(x_list), np.transpose(y_list))

#print clf.coef_

points = []
R1 = 0
for j in range(len(x_list[0])):
    for i in range(len(clf.coef_)):
        R1 += clf.coef_[i]*x_list[i][j]
    points.append(R1)
    R1 = 0
def R_squared(x,y):
    slope,intercept,r_value,p_value,std_err = stats.linregress(x,y)
    return r_value**2
#print R_squared(points,y_list)

def algo(x,y):
    return clf.coef_[0]*x*2-clf.coef_[2]*x+clf.coef_[1]*y*2+clf.coef_[3]*y

P_A = algo(15,200)
P_B = algo(15,0)
P_C = algo(0,0)

dict_routes = {}

print P_A,P_B,P_C

P_BAC = 1/((6*P_B+15*P_A+28*P_C)*34)
P_ABC = 1/((12*P_A+21*P_B+34*P_C)*40)
P_BCA = 1/((6*P_B+20*P_C+33*P_A)*39)
P_ACB = 1/((12*P_A+25*P_C+38*P_B)*39)
P_CBA = 1/((12*P_C+25*P_B+34*P_A)*40)
P_CAB = 1/((12*P_C+24*P_A+33*P_B)*36)

dict_routes['BAC'] = P_BAC
dict_routes['CAB'] = P_CAB
dict_routes['CBA'] = P_CBA
dict_routes['ACB'] = P_ACB
dict_routes['BCA'] = P_BCA
dict_routes['ABC'] = P_ABC


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
    
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.innerlayout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.image = Image(source='TrashHold.png',allow_stretch=True)
        self.btn = Button(background_normal='start.png', on_press=self.switchA)
        self.btn2 = Button(background_normal='quit.png', on_press=self.quitApp)
        self.layout.add_widget(self.image)
        self.innerlayout.add_widget(self.btn)
        self.innerlayout.add_widget(self.btn2)
        self.layout.add_widget(self.innerlayout)
        self.add_widget(self.layout)
    def switchA(self,instance):
        self.manager.current = 'choice'
        self.manager.transition.direction = 'left'
    def quitApp(self,instance):
        App.get_running_app().stop()
        
class ChoiceScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout = GridLayout(cols=2)
        self.bt1 = Button(background_normal='bugis.png', on_press=self.switchC)
        self.bt2 = Button(background_normal='clementi.png', on_press=self.switchC)
        self.bt3 = Button(background_normal='hougang.png', on_press=self.switchC)
        self.bt4 = Button(background_normal='pasirris.png', on_press=self.switchC)
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
        self.route = keywithmaxval(dict_routes)
        self.count = 0
        self.layout = BoxLayout(orientation='vertical')
        self.image = Image(source='Map.png', size_hint=(1, 1))
        self.btn = Button(background_normal='analyze.png', size_hint=(1, 0.1), on_press=self.path)
        self.btn2 = Button(background_normal='return.png', size_hint=(1, 0.1), on_press=self.switchM)
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.btn2)
        self.add_widget(self.layout)
    def path(self, instance):
        self.count += 1
        if self.route == 'ABC':
            if self.count == 1:
                self.image.source = 'ADA.png'
                self.btn.background_normal = 'Nextpath.png'
            elif self.count == 2: 
                self.image.source = 'AAB.png'
            elif self.count == 3: 
                self.image.source = 'ABC.png'
            elif self.count >= 4: 
                self.image.source = 'ACD.png'
                self.btn.background_normal = 'Allclear.png'
        if self.route == 'ACB':
            if self.count == 1:
                self.image.source = 'ADA.png'
                self.btn.background_normal = 'Nextpath.png'
            elif self.count == 2: 
                self.image.source = 'AAC.png'
            elif self.count == 3: 
                self.image.source = 'ACB.png'
            elif self.count >= 4: 
                self.image.source = 'ABD.png'
                self.btn.background_normal = 'Allclear.png'
        if self.route == 'BAC':
            if self.count == 1:
                self.image.source = 'ADB.png'
                self.btn.background_normal = 'Nextpath.png'
            elif self.count == 2: 
                self.image.source = 'ABA.png'
            elif self.count == 3: 
                self.image.source = 'AAC.png'
            elif self.count >= 4: 
                self.image.source = 'ACD.png'
                self.btn.background_normal = 'Allclear.png'
        if self.route == 'BCA':
            if self.count == 1:
                self.image.source = 'ADB.png'
                self.btn.background_normal = 'Nextpath.png'
            elif self.count == 2: 
                self.image.source = 'ABC.png'
            elif self.count == 3: 
                self.image.source = 'ACA.png'
            elif self.count >= 4: 
                self.image.source = 'AAD.png'
                self.btn.background_normal = 'Allclear.png'
        if self.route == 'CAB':
            if self.count == 1:
                self.image.source = 'ADC.png'
                self.btn.background_normal = 'Nextpath.png'
            elif self.count == 2: 
                self.image.source = 'ACA.png'
            elif self.count == 3: 
                self.image.source = 'AAB.png'
            elif self.count >= 4: 
                self.image.source = 'ABD.png'
                self.btn.background_normal = 'Allclear.png'
        if self.route == 'CBA':
            if self.count == 1:
                self.image.source = 'ADC.png'
                self.btn.background_normal = 'Nextpath.png'
            elif self.count == 2: 
                self.image.source = 'ACB.png'
            elif self.count == 3: 
                self.image.source = 'ABA.png'
            elif self.count >= 4: 
                self.image.source = 'AAD.png'
                self.btn.background_normal = 'Allclear.png'
    def switchM(self,instance):
        self.image.source = 'Map.png'
        self.btn.background_normal = 'analyze.png'
        self.count = 0
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