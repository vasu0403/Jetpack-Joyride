from board_obj import Board_obj
from speed import Speed
from colorama import Fore, Back, Style
from playarea import Playarea
class SpeedBoost:
    def __init__(self, middle_row, start_column, grid, num):
        self.__coordinates = {
            middle_row - 2 : [start_column, start_column + 1, start_column + 4, start_column + 5],
            middle_row - 1 : [start_column + 1, start_column + 2, start_column + 5, start_column + 6],
            middle_row     : [start_column + 2, start_column + 3, start_column + 6, start_column + 7],
            middle_row + 1 : [start_column + 1, start_column + 2, start_column + 5, start_column + 6],
            middle_row + 2 : [start_column, start_column + 1, start_column + 4, start_column + 5],
        }
        for i in self.__coordinates:
            for j in self.__coordinates[i]:
                grid[i][j] = Speed(num)

    def self_destruct(self, grid):
        for i in self.__coordinates:
            for j in self.__coordinates[i]:
                grid[i][j] = Playarea()
