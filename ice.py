from board_obj import Board_obj
from colorama import Fore, Back, Style

class Ice(Board_obj):
	def __init__(self, ice_num, disp):
		Board_obj.__init__(self)
		self.disp = disp
		self.ice_num = ice_num
		self.ice = 1
