from board_obj import Board_obj
from colorama import Fore, Back, Style

class Boss(Board_obj):
    def __init__(self, disp):
        Board_obj.__init__(self)
        if disp != ' ':
            self.boss = 1;
        self.disp = disp
