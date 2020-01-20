from board_obj import Board_obj
from player import Player
from playarea import Playarea
import sys
from colorama import Fore, Back, Style
from ice import Ice

class IceBall:
    def __init__(self, num, upper_row, column, grid):
        self.alive = 1
        self.num = 0
        self.__coordinates = {
            upper_row: [column - 1],
            upper_row + 1: [column - 2, column],
            upper_row + 2: [column - 2, column - 1, column]
        }
        self.__disp = {
            0 : ['_'],
            1 : ['/', '\\'],
            2 : ['\\', '_', '/']
        }
        cnt1 = 0
        cnt2 = 0
        for i in self.__coordinates:
            cnt2 = 0
            for j in self.__coordinates[i]:
                grid[i][j] = Ice(num, self.__disp[cnt1][cnt2])
                cnt2 += 1
            cnt1 += 1

    def move(self, grid, pos):
        if self.alive == 0:
            # print("**")
            return
        new_coordinates = {}
        for i in self.__coordinates:
            new_coordinates[i] = []
            for j in self.__coordinates[i]:
                grid[i][j] = Playarea()
                new_coordinates[i].append(j - 3)
                if j - 3 <= pos:
                    self.alive = 0

        if self.alive == 0:
            return

        self.__coordinates = new_coordinates
        cnt1 = 0
        for i in new_coordinates:
            cnt2 = 0
            for j in new_coordinates[i]:
                grid[i][j] = Ice(self.num, self.__disp[cnt1][cnt2])
                cnt2 += 1
            cnt1 += 1
