from board_obj import Board_obj
from colorama import Fore, Back, Style

class Boundary(Board_obj):
	def __init__(self):
		Board_obj.__init__(self)
		self.disp = Back.GREEN + " " + Style.RESET_ALL
		self.blocking = 1