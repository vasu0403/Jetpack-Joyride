from board_obj import Board_obj
from colorama import Fore, Back, Style

class Coin(Board_obj):
	def __init__(self):
		Board_obj.__init__(self)
		self.disp = Fore.BLUE + "$" + Style.RESET_ALL
		self.points = 1
