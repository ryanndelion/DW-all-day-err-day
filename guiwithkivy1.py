from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.togglebutton import ToggleButton
from firebase import firebase

token=None
url=None
firebase=firebase.FirebaseApplication(url,token)

class GuiKivy(App):
	def build(self):
		layout=GridLayout(cols=2)
		layout.add_widget(Label(text='Yellow LED',haligh='left'))
		self.yellowb=ToggleButton(text='Off', group='lights', on_press=self.updateStatus)
		layout.add_widget(self.yellowb)
		self.redb=ToggleButton(text='Off', group='lights', on_press=self.updateStatus)
		layout.add_widget(Label(text='Red LED',haligh='left'))
		layout.add_widget(self.redb)
		return layout

	def updateStatus(self,instance):
		if instance == self.yellowb:
			self.yellowb.text = 'On'
			self.redb.text = 'Off'
		elif instance == self.redb:
			self.redb.text = 'On'
			self.yellowb.text = 'Off'

GuiKivy().run()
