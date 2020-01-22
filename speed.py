from board_obj import Board_obj
from colorama import Fore, Back, Style

class Speed:
    def __init__(self, boostNum):
        Board_obj.__init__(self)
        self.__boostNum = boostNum
        self.disp = Fore.WHITE + ">" + Style.RESET_ALL
        self.boost = 1

    @property
    def boostNum(self):
        return self.__boostNum
    @boostNum.setter
    def boostNum(self, a):
        self.__boostNum = a
