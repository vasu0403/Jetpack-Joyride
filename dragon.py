from board_obj import Board_obj
from player import Player
from playarea import Playarea
import sys
from colorama import Fore, Back, Style

class Dragon:
	def __init__(self, column):
		self.__dragon_disp = {}
		cnt = 0
		with open('dragon.txt', 'r') as file:
			data = file.readlines()
			for l in data:
				li = list(l)
				self.__dragon_disp[cnt] = li
				self.__dragon_disp[cnt].pop()
				cnt += 1
		self.__dragon_coordinates = {}
		for i in range(10, 22):
			self.__dragon_coordinates[i] = []
			for j in range(column - 37, column - 2):
				self.__dragon_coordinates[i].append(j)


	def insert(self, grid):
		i2 = 0
		j2 = 0
		for i in self.__dragon_coordinates:
			j2 = 0
			for j in self.__dragon_coordinates[i]:
				grid[i][j].disp = self.__dragon_disp[i2][j2]
				j2 += 1
			i2 += 1
