from board_obj import Board_obj

class Attraction(Board_obj):
    def __init__(self, blocking, disp, i, j):
        Board_obj.__init__(self)
        if blocking == 1:
            self.blocking = 1
        self.disp = disp
        self.__centre_i = i
        self.__centre_j = j
        self.attr = 1

    @property
    def centre_i(self):
        return self.__centre_i
    @centre_i.setter
    def centre_i(self, a):
        self.__centre_i = a

    @property
    def centre_j(self):
        return self.__centre_j
    @centre_j.setter
    def centre_j(self, a):
        self.__centre_j = a
