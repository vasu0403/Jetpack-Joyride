from board_obj import Board_obj
from colorama import Fore, Back, Style

class Ice(Board_obj):
	def __init__(self, ice_num, disp):
		Board_obj.__init__(self)
		self.disp = disp
		self.__ice_num = ice_num
		self.ice = 1

	@property
	def ice_num(self):
	    return self.__ice_num
	@ice_num.setter
	def ice_num(self, a):
	    self.__ice_num = a
