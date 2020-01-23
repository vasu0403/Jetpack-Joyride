from colorama import Fore, Back, Style

class Board_obj:
	def __init__(self):
		self.__fire = 0
		self.__playarea = 0
		self.__blocking = 0
		self.__points = 0
		self.__attr = 0
		self.__player = 0
		self.__disp = Back.BLUE + " " + Style.RESET_ALL
		self.__boost = 0
		self.__shot = 0
		self.__boss = 0
		self.__ice = 0

	@property
	def fire(self):
	    return self.__fire
	@fire.setter
	def fire(self, a):
	    self.__fire = a

	@property
	def playarea(self):
	    return self.__playarea
	@playarea.setter
	def playarea(self, a):
	    self.__playarea = a

	@property
	def blocking(self):
	    return self.__blocking
	@blocking.setter
	def blocking(self, a):
	    self.__blocking = a

	@property
	def points(self):
	    return self.__points
	@points.setter
	def points(self, a):
	    self.__points = a

	@property
	def attr(self):
	    return self.__attr
	@attr.setter
	def attr(self, a):
	    self.__attr = a

	@property
	def player(self):
	    return self.__player
	@player.setter
	def player(self, a):
	    self.__player = a

	@property
	def disp(self):
	    return self.__disp
	@disp.setter
	def disp(self, a):
	    self.__disp = a

	@property
	def boost(self):
	    return self.__boost
	@boost.setter
	def boost(self, a):
	    self.__boost = a

	@property
	def shot(self):
	    return self.__shot
	@shot.setter
	def shot(self, a):
	    self.__shot = a

	@property
	def boss(self):
	    return self.__boss
	@boss.setter
	def boss(self, a):
	    self.__boss = a

	@property
	def ice(self):
	    return self.__ice
	@ice.setter
	def ice(self, a):
	    self.__ice = a
