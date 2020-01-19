from board_obj import Board_obj
from colorama import Fore, Back, Style

class Fire(Board_obj):
	def __init__(self, beam_num, disp):
		Board_obj.__init__(self)
		self.disp = disp
		self.beam_num = beam_num
		self.fire = 1
