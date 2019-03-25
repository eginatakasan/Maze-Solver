from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


Window.clearcolor = (0.9, 0.9, 0.9, 0.9)

characters = 0
lines = 0
flag = 0

class MazeDisplay(BoxLayout):
	def start(self):
		pass
	def generate_maze(self):
		global lines
		global characters
		global flag
		list_of_char = []
		if (flag == 0):
			flag = 1
			self.remove_widget(self.infolbl)
			file = open(self.textinput.text, "r")
			for x in file:
				characters = len(x)
				lines = lines + 1
				for y in range(len(x)):
					list_of_char.append(list(x)[y])
					
			self.g = GridLayout(rows = lines, cols = characters)
			self.add_widget(self.g)

			for i in range(len(list_of_char)):
					if (list_of_char[i] == '1'):
						b = Button(background_normal = '' , background_color = (0,0,0,10))
						self.g.add_widget(b)
					elif (list_of_char[i] == '0'):
						b = Button(background_normal = '')
						self.g.add_widget(b)
		else:
			pass
		
	def clear(self):
		global flag
		if (flag == 0):
			pass
		else :
			self.remove_widget(self.g)
			self.infolbl = Label(markup = True, text ='[color=0f0c0c]Insert maze file in text input')
			self.add_widget(self.infolbl)
			flag = 0
	

class MazeSolverApp(App):
	def build(self):
		return MazeDisplay()

if __name__ == "__main__":
	MazeSolverApp().run()