from board_obj import Board_obj
from colorama import Fore, Back, Style

class Player(Board_obj):
	def __init__(self):
		Board_obj.__init__(self)
		self.disp = Back.RED + " " + Style.RESET_ALL
		self.player = 1