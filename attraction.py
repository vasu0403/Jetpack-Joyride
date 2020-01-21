from board_obj import Board_obj

class Attraction(Board_obj):
    def __init__(self, blocking, disp, i, j):
        Board_obj.__init__(self)
        if blocking == 1:
            self.blocking = 1
        self.disp = disp
        self.centre_i = i
        self.centre_j = j
        self.attr = 1
