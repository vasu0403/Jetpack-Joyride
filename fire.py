from board_obj import Board_obj
from colorama import Fore, Back, Style

class Fire(Board_obj):
	def __init__(self, beam_num):
		Board_obj.__init__(self)
		self.disp = Back.YELLOW + " " + Style.RESET_ALL
		self.beam_num = beam_num
		self.fire = 1
