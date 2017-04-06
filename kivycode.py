from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.togglebutton import ToggleButton
from firebase import firebase

token='0lYSxo2k1Jrr3i3rxhyb3IFy3kTKEAsXP39n3mpV'
url='https://iot-dw-1d-2017.firebaseio.com/'
firebase=firebase.FirebaseApplication(url,token)

class GuiKivy(App):
	def build(self):
		self.count = 0
		firebase.put('/','States','off')
		layout=GridLayout(cols=2)
		layout.add_widget(Label(text='Yellow LED',haligh='left'))
		self.yellowb=ToggleButton(text='Off', group='lights', on_press=self.updateStatus)
		layout.add_widget(self.yellowb)
		self.redb=ToggleButton(text='Off', group='lights', on_press=self.updateStatus)
		layout.add_widget(Label(text='Red LED',haligh='left'))
		layout.add_widget(self.redb)
		return layout

	def updateStatus(self,instance):
		print self.count
		if self.count == 0:
			if instance == self.yellowb:
				self.count = 1
				self.yellowb.text = 'On'
				self.redb.text = 'Off'
				firebase.put('/','States','yellow')
			elif instance == self.redb:
				self.count = 2
				self.redb.text = 'On'
				self.yellowb.text = 'Off'
				firebase.put('/','States','red')

		elif self.count == 1:
			if instance == self.yellowb:
				self.count = 0
				self.yellowb.text = 'Off'
				self.redb.text = 'Off'
				firebase.put('/','States','off')
			if instance == self.redb:
				self.count = 2
				self.yellowb.text = 'Off'
				self.redb.text = 'On'
				firebase.put('/','States','red')

		elif self.count == 2:
			if instance == self.yellowb:
				self.count = 1
				self.yellowb.text = 'On'
				self.redb.text = 'Off'
				firebase.put('/','States','yellow')
			if instance == self.redb:
				self.count = 0
				self.yellowb.text = 'Off'
				self.redb.text = 'Off'
				firebase.put('/','States','off')






GuiKivy().run()