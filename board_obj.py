from colorama import Fore, Back, Style

class Board_obj:
	def __init__(self):
		self.fire = 0
		self.playarea = 0
		self.blocking = 0
		self.points = 0
		self.magnet = 0
		self.player = 0
		self.disp = Back.BLUE + " " + Style.RESET_ALL
