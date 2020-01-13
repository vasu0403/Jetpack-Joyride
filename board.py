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

	def insert_player(self):
		for i in range(12, 14):
			for j in range(10, 13):
				self.grid[i][j] = Player()
		for i in range(14, 16):
			self.grid[i][11] = Player()

	def gravity(self, player_cords):
		for i in player_cords:
			for j in player_cords[i]:
				if self.grid[i+1][j].blocking == 1:
					return
		new_player_cords = {}
		for i in player_cords:
			new_player_cords[i+1] = []
			for j in player_cords[i]:
				new_player_cords[i+1].append(j)
				self.grid[i][j] = Playarea()
		player_cords.clear();
		for i in new_player_cords:
			player_cords[i] = []
			for j in new_player_cords[i]:
				self.grid[i][j] = Player()
				player_cords[i].append(j)
		return

	def move_player(self, player_cords, player_column, movement, pos):
		new_player_cords = {}
		for i in player_cords:
			new_player_cords[i + movement[0]] = []
			for j in player_cords[i]:
				new_player_cords[i + movement[0]].append(j + movement[1])
		
		player_column = player_column + movement[1] 
		if player_column <= pos:
			return player_column - movement[1]
		for i in new_player_cords:
			for j in new_player_cords[i]:
				if self.grid[i][j].blocking == 1:
					return player_column							## Add condition for fire beams and enemies here
		
		for i in player_cords:
			for j in player_cords[i]:
				self.grid[i][j] = Playarea()

		player_cords.clear()
		for i in new_player_cords:
			player_cords[i] = []
			for j in new_player_cords[i]:
				self.grid[i][j] = Player()
				player_cords[i].append(j)
		
		return player_column
	def display(self):
		print("\033[0;0H")
		print()
		for i in range(self.rows):
			for j in range(self.pos, self.pos + self.num_column):
				print(self.grid[i][j].disp, end = "")
			print()