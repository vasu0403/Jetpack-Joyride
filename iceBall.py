from board_obj import Board_obj
from player import Player
from playarea import Playarea
import sys
from bullets import Bullet
from colorama import Fore, Back, Style
from ice import Ice
import time

class IceBall(Bullet):                                #here
    def __init__(self, num, upper_row, column, grid):
        # Bullet.__init__(self)                             #here
        self.__alive = 1
        self.__num = num
        self.__coordinates = {
            upper_row: [column - 1],
            upper_row + 1: [column - 2, column],
            upper_row + 2: [column - 2, column - 1, column]
        }
        self.__disp = {
            0 : [Fore.WHITE + Style.BRIGHT + '_' + Style.RESET_ALL],
            1 : [Fore.WHITE + Style.BRIGHT + '/' + Style.RESET_ALL, Fore.WHITE + Style.BRIGHT + '\\' + Style.RESET_ALL],
            2 : [Fore.WHITE + Style.BRIGHT + '\\' + Style.RESET_ALL, Fore.WHITE + Style.BRIGHT + '_' + Style.RESET_ALL, Fore.WHITE + Style.BRIGHT + '/' + Style.RESET_ALL]
        }
        cnt1 = 0
        cnt2 = 0
        for i in self.__coordinates:
            cnt2 = 0
            for j in self.__coordinates[i]:
                grid[i][j] = Ice(num, self.__disp[cnt1][cnt2])
                cnt2 += 1
            cnt1 += 1

    @property
    def alive(self):
        return self.__alive
    @alive.setter
    def alive(self, a):
        self.__alive = a

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, a):
        self.__num = a


    def move(self, grid, pos, mandalorian):
        if self.alive == 0:
            return
        new_coordinates = {}
        for i in self.__coordinates:
            new_coordinates[i] = []
            for j in self.__coordinates[i]:
                grid[i][j] = Playarea()
                new_coordinates[i].append(j - 3)
                if j - 3 <= pos:
                    self.alive = 0

        flag = 0
        for i in new_coordinates:
            for j in new_coordinates[i]:
                if grid[i][j].player == 1 or grid[i][j+1].player == 1 or grid[i][j+2].player == 1:
                    self.alive = 0
                    if mandalorian.shield == 1:
                        mandalorian.shield = 0
                    else:
                        mandalorian.life -= 1
                    if mandalorian.life == 0:
                        mandalorian.game_over()
                    flag = 1
                    break
            if flag == 1:
                break

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

    def self_destruct(self, grid):
        self.alive = 0
        for i in self.__coordinates:
            for j in self.__coordinates[i]:
                grid[i][j] = Playarea()
