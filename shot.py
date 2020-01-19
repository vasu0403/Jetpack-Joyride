from board_obj import Board_obj
from colorama import Fore, Back, Style

class Shot:
    def __init__(self, disp):
        Board_obj.__init__(self)
        self.shot = 1
        self.disp = disp
