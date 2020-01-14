from board_obj import Board_obj
from fire import Fire
from colorama import Fore, Back, Style
from playarea import Playarea
class Beam:
	alive = 1
	def __init__(self, i, j, length, orientation, grid, beam_num):
		self.x = i
		self.y = j
		self.alive = 1
		self.orientation = orientation
		self.length = length
		for t in range(length):
			i1 = i + orientation[0]*t
			i2 = j + orientation[1]*t
			grid[i1][i2] = Fire(beam_num)

	def self_destruct(self, grid):
		for t in range(self.length):
			i1 = self.x + self.orientation[0]*t
			i2 = self.y + self.orientation[1]*t
			grid[i1][i2] = Playarea()