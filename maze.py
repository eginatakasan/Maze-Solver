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
	reset = True
	matrix = []
	visited = []
	list_of_char = []
	def generate_maze(self):
		global lines
		global characters
		global flag
		self.matrix = readMaze(self.textinput.text)
		if (flag == 0):
			flag = 1
			self.remove_widget(self.infolbl)
			if (self.reset) :
				self.reset_list_of_char()
			self.g = GridLayout(rows = lines, cols = characters)
			self.add_widget(self.g)

			for i in range(len(self.list_of_char)):
					if (self.list_of_char[i] == '1'):
						b = Button(background_normal = '' , background_color = (0,0,0,1))
					elif (self.list_of_char[i] == '0'):
						b = Button(background_normal = '')
					elif (self.list_of_char[i] == '2'):
						b = Button(background_normal = '' , background_color = (0.8,0.6,0.6,0.8))
					self.g.add_widget(b)
			computed_astar = False
			computed_bfs = False
		else:
			pass
	def reset_list_of_char(self):
		global lines
		global characters
		self.list_of_char = []
		file = open(self.textinput.text, "r")
		for x in file:
			characters = len(x)
			lines = lines + 1
			for y in range(len(x.strip())):
				self.list_of_char.append(list(x.strip())[y])
	def replace_list_of_char(self, list_of_point):
		global characters
		self.reset_list_of_char()
		for point in list_of_point:
			x = point[0]
			y = point[1]
			self.list_of_char[x*characters+y] = '2'
		self.clear()
		self.reset = False
		self.generate_maze()
	def clear(self):
		global flag
		if (flag == 0):
			pass
		else :
			self.remove_widget(self.g)
			self.infolbl = Label(markup = True, text ='[color=0f0c0c]Insert maze file in text input')
			self.add_widget(self.infolbl)
			self.reset = True
			flag = 0
	def reset_visited_list(self):
		self.visited = [[False for x in range (len(self.matrix[0]))] for y in range (len(self.matrix))]
		for i in range (0, len(self.visited)):
			for j in range (0, len(self.visited[0])):
				if(self.matrix[i][j]=='1'):
					self.visited[i][j]=True
	def compute_astar(self):
		if (not self.computed_astar):
			global astar_result
			computed_astar = True
			self.reset_visited_list()
			start_x, start_y = searchStart(self.matrix)
			finish_x, finish_y = searchFinish(self.matrix)
			astar_result = astar(self.matrix, self.visited, start_x, start_y, finish_x, finish_y)
		self.replace_list_of_char(astar_result)
	def compute_bfs(self):
		if (not self.computed_bfs):
			global bfs_result
			computed_bfs = True
			self.reset_visited_list()
			start_x, start_y = searchStart(self.matrix)
			finish_x, finish_y = searchFinish(self.matrix)
			bfs_result = bfs(self.matrix, self.visited, start_x, start_y, finish_x, finish_y)
		self.replace_list_of_char(bfs_result)
	
class MazeSolverApp(App):
	def build(self):
		return MazeDisplay()

if __name__ == "__main__":
	MazeSolverApp(kv_file="MazeSolver.kv").run()