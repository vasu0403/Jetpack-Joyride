import numpy as np
from board_obj import Board_obj
from boundary import Boundary
from playarea import Playarea
from player import Player
from config import *
from colorama import Fore, Back, Style
class Board:
	def __init__(self, rows, columns, num_column):
		self.__rows = rows
		self.__columns = columns
		self.__num_column = num_column
		self.__pos = 0

	@property
	def rows(self):
	    return self.__rows
	@rows.setter
	def rows(self, a):
	    self.__rows = a

	@property
	def columns(self):
	    return self.__columns
	@columns.setter
	def columns(self, a):
	    self.__columns = a

	@property
	def num_column(self):
	    return self.__num_column
	@num_column.setter
	def num_column(self, a):
	    self.__num_column = a

	@property
	def pos(self):
	    return self.__pos
	@pos.setter
	def pos(self, a):
	    self.__pos = a

	@property
	def grid(self):
	    return self.__grid
	@grid.setter
	def grid(self, a):
	    self.__grid = a

	def create_grid(self):
		self.__grid = np.full((self.rows, self.columns), Board_obj())

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

	def display(self, life, score, shield, shield_remaining_time, shield_cooloff_time, boss_life, time_left):
		print("\033[0;0H")
		if shield == 1:
			s = "\nLives left: " + str(life).zfill(2) + "  \t\t    Score: " + str(score) + "  \t\t    Shield remainig time: " + str(shield_remaining_time) + "  \t\t    Time left: " + str(time_left).zfill(2) + "  \t\t     Boss life remaining: " +  str(boss_life) + "    \n"
		if shield == 0:
			if shield_cooloff_time > 0:
				s = "\nLives left: " + str(life).zfill(2) + "  \t\t    Score: " + str(score) + Fore.RED + "  \t\t    Shield cooloff time: " + str(shield_cooloff_time) + Style.RESET_ALL + "  \t\t    Time left: " + str(time_left).zfill(2) +  "  \t\t    Boss life remaining: " + str(boss_life) + "    \n"
			else:
				s = "\nLives left: " + str(life).zfill(2) + "  \t\t    Score: " + str(score) + "  \t\t" + Fore.BLUE + "    SHIELD AVAILABLE !! " + Style.RESET_ALL + "  \t\t    Time left: " + str(time_left).zfill(2) +  "  \t\t    Boss life remaining: " + str(boss_life) + "   \n"
		# print("Lives left: " + str(life))
		for i in range(self.rows):
			for j in range(self.pos, self.pos + self.num_column):
				# print(self.grid[i][j].disp, end = "")
				s += self.grid[i][j].disp
			s += '\n'
		print(s)
