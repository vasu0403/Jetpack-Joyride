from board_obj import Board_obj
from player import Player
from playarea import Playarea
import sys
from colorama import Fore, Back, Style
from boss import Boss
import time

class Dragon:
	def __init__(self, column):
		self.__dragon_disp = {}
		self.__life = 10
		cnt = 0
		with open('dragon.txt', 'r') as file:
			data = file.readlines()
			for l in data:
				li = list(l)
				for i in range(len(li)):
					if li[i] != ' ':
						li[i] = Back.RED + Fore.YELLOW + Style.BRIGHT + li[i] + Style.RESET_ALL
				self.__dragon_disp[cnt] = li
				self.__dragon_disp[cnt].pop()
				cnt += 1
		self.__dragon_coordinates = {}
		self.__upper_coordinate = 8
		for i in range(8, 20):
			self.__dragon_coordinates[i] = []
			for j in range(column - 37, column - 2):
				self.__dragon_coordinates[i].append(j)

	def self_destruct(self, grid):
		for i in self.__dragon_coordinates:
			for j in self.__dragon_coordinates[i]:
				grid[i][j] = Playarea()


	@property
	def life(self):
	    return self.__life
	@life.setter
	def life(self, a):
	    self.__life = a

	@property
	def upper_coordinate(self):
	    return self.__upper_coordinate
	@upper_coordinate.setter
	def upper_coordinate(self, a):
	    self.__upper_coordinate = a


	def insert(self, grid):
		i2 = 0
		j2 = 0
		for i in self.__dragon_coordinates:
			j2 = 0
			for j in self.__dragon_coordinates[i]:
				grid[i][j] = Boss(self.__dragon_disp[i2][j2])
				j2 += 1
			i2 += 1

	def move(self, movement, grid):
		new_dragon_cords = {}
		for i in self.__dragon_coordinates:
			new_dragon_cords[i + movement[0]] = []
			for j in self.__dragon_coordinates[i]:
				new_dragon_cords[i + movement[0]].append(j + movement[1])

		for i in new_dragon_cords:
			for j in new_dragon_cords[i]:
				if grid[i][j].blocking == 1:
					return
		li = list(self.__dragon_coordinates.keys())
		li.sort()
		self.upper_coordinate = li[0]
		for i in self.__dragon_coordinates:
			for j in self.__dragon_coordinates[i]:
				grid[i][j] = Playarea()

		self.__dragon_coordinates.clear()
		cnt1 = 0
		cnt2 = 0
		for i in new_dragon_cords:
			self.__dragon_coordinates[i] = []
			cnt2 = 0
			for j in new_dragon_cords[i]:
				grid[i][j] = Boss(self.__dragon_disp[cnt1][cnt2])
				self.__dragon_coordinates[i].append(j)
				cnt2 += 1
			cnt1 += 1
		return
