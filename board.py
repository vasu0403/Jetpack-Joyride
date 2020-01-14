import numpy as np
from board_obj import Board_obj
from boundary import Boundary
from playarea import Playarea
from player import Player
from config import *

class Board:
	def __init__(self, rows, columns, num_column):
		self.rows = rows
		self.columns = columns
		self.num_column = num_column
		self.pos = 0

	def create_grid(self):
		self.grid = np.full((self.rows, self.columns), Board_obj())

	def insert_boundary(self):
		for i in range(self.columns):
			self.grid[0][i] = Boundary()
			self.grid[1][i] = Boundary()
			self.grid[2][i] = Boundary()
			self.grid[self.rows-1][i] = Boundary()
			self.grid[self.rows-2][i] = Boundary()
			self.grid[self.rows-3][i] = Boundary()

	def insert_playarea(self):
		for i in range(3, self.rows - 3):
			for j in range(self.columns):
				self.grid[i][j] = Playarea()

	def display(self):
		print("\033[0;0H")
		print()
		for i in range(self.rows):
			for j in range(self.pos, self.pos + self.num_column):
				print(self.grid[i][j].disp, end = "")
			print()