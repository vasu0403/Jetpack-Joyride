from board_obj import Board_obj
from colorama import Fore, Back, Style

class Player(Board_obj):
	def __init__(self, disp):
		Board_obj.__init__(self)
		self.disp = disp
		self.player = 1
