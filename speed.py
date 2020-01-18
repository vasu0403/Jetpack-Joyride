from board_obj import Board_obj
from colorama import Fore, Back, Style

class Speed:
    def __init__(self, boostNum):
        Board_obj.__init__(self)
        self.boostNum = boostNum
        self.disp = Fore.WHITE + ">" + Style.RESET_ALL
        self.boost = 1
