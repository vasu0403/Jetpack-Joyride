from board_obj import Board_obj
from shot import Shot
from colorama import Fore, Back, Style
from playarea import Playarea
from bullets import Bullet

class GunShot(Bullet):          # here
    def __init__(self, gun_shot_num, player_coords, grid):
        Bullet.__init__(self, gun_shot_num, player_coords, grid)           # here

    def move(self, grid, fire_beams, pos, num_column, mandalorian, columns, ice_balls, boss):
        return super().move(grid, fire_beams, pos, num_column, mandalorian, columns, ice_balls, boss)
