from board_obj import Board_obj
from player import Player
from playarea import Playarea
import sys
from colorama import Fore, Back, Style
from attraction import Attraction

class Magnet:
    def __init__(self, row, start_column, grid):
        grid[row][start_column] = Attraction(1, Style.BRIGHT + Fore.RED + "_" + Style.RESET_ALL, row, start_column)
        grid[row][start_column-1] = Attraction(1, Style.BRIGHT + Fore.RED + "|" + Style.RESET_ALL, row, start_column)
        grid[row][start_column+1] = Attraction(1, Style.BRIGHT + Fore.RED + "|" + Style.RESET_ALL, row, start_column)
        grid[row-1][start_column-1] = Attraction(1, Style.BRIGHT + Fore.YELLOW + "|" + Style.RESET_ALL, row, start_column)
        grid[row-1][start_column+1] = Attraction(1, Style.BRIGHT + Fore.YELLOW + "|" + Style.RESET_ALL, row, start_column)
