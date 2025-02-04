from board_obj import Board_obj
from fire import Fire
from colorama import Fore, Back, Style
from playarea import Playarea

class Beam:
	__alive = 1
	def __init__(self, i, j, length, orientation, grid, beam_num):
		self.__x = i
		self.__y = j
		last_i = i
		last_j = j
		self.__alive = 1
		self.__orientation = orientation
		self.__length = length
		for t in range(length):
			i1 = i + orientation[0]*t
			i2 = j + orientation[1]*t
			if i1 > 2 and i1 < 37:
				last_i = i1
				last_j = i2
			if i1 > 2 and i1 < 37 and grid[i1][i2].playarea == 1:
				grid[i1][i2] = Fire(beam_num, Fore.YELLOW + Style.BRIGHT + "F" + Style.RESET_ALL)
			if i1 > 2 and i1 < 37 and grid[i1][i2 + 1].playarea == 1:
				grid[i1][i2+1] = Fire(beam_num,  Fore.YELLOW + Style.BRIGHT + "F" + Style.RESET_ALL)
		grid[i][j] = Fire(beam_num, Back.YELLOW + Style.BRIGHT + " " + Style.RESET_ALL)
		grid[i][j + 1] = Fire(beam_num, Back.YELLOW + Style.BRIGHT + " " + Style.RESET_ALL)
		grid[last_i][last_j] = Fire(beam_num, Back.YELLOW + Style.BRIGHT + " " + Style.RESET_ALL)
		grid[last_i][last_j + 1] = Fire(beam_num, Back.YELLOW + Style.BRIGHT + " " + Style.RESET_ALL)
	def self_destruct(self, grid):
		self.__alive = 0
		for t in range(self.__length):
			i1 = self.__x + self.__orientation[0]*t
			i2 = self.__y + self.__orientation[1]*t
			if i1 > 2 and i1 < 37 and grid[i1][i2].fire == 1:
				grid[i1][i2] = Playarea()
			if i1 > 2 and i1 < 37 and grid[i1][i2 + 1].fire == 1:
				grid[i1][i2+1] = Playarea()
