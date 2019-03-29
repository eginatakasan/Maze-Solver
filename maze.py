from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from backend import *


Window.clearcolor = (0.9, 0.9, 0.9, 0.9)

characters = 0
lines = 0
astar_result = []
bfs_result = []
flag = 0

class MazeDisplay(BoxLayout):
	computed_astar = False
	computed_bfs = False
	matrix = []
	visited = []
	def __init__(self):
		self.generate_maze()
	def generate_maze(self):
		global lines
		global characters
		global flag
		self.matrix = readMaze(self.textinput.text)
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
			computed_astar = False
			computed_bfs = False
			print(self.matrix)
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
	def reset_visited_list(self):
		self.visited = [[False for x in range (len(self.matrix[0]))] for y in range (len(self.matrix))]
		for i in range (0, len(self.visited)-1):
			for j in range (0, len(self.visited[0])-1):
				if(self.matrix[i][j]=='1'):
					self.visited[i][j]=True
	def compute_astar(self):
		if (not self.computed_astar):
			global astar_result
			computed_astar = True
			self.reset_visited_list()
			queue = []
			astar(self.matrix, self.visited, queue, 1, 0, 9, 10)
			self.show_astar_route()
		else:
			self.show_astar_route()
	def show_astar_route(self):
		pass
	def compute_bfs(self):
		if (not self.computed_bfs):
			global bfs_result
			computed_bfs = True
			queue = []
			self.reset_visited_list()
			bfs_result = bfs(self.matrix, self.visited, queue, 1, 0, 9, 10)
			self.show_bfs_route()
		else:
			self.show_bfs_route()
	def show_bfs_route(self):
		print(bfs_result)
	
class MazeSolverApp(App):
	def build(self):
		return MazeDisplay()

if __name__ == "__main__":
	MazeSolverApp(kv_file="MazeSolver.kv").run()