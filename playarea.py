from board_obj import Board_obj
from colorama import Fore, Back, Style

class Playarea(Board_obj):
	def __init__(self):
		Board_obj.__init__(self)
		self.disp = Back.BLUE + " " + Style.RESET_ALL