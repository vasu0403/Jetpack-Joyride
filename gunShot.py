from board_obj import Board_obj
from shot import Shot
from colorama import Fore, Back, Style
from playarea import Playarea

class GunShot:
    def __init__(self, gun_shot_num, player_coords, grid):
        self.__alive = 1
        rows = list(player_coords.keys())
        rows.sort()
        row1 = int(rows[3])
        column1 = int(player_coords[row1][3]) + 3
        self.__coordinates = {
            # row1 -1 : [column1 + 1, column1 + 2],
            row1 : [column1, column1 + 1, column1 + 2, column1 + 3]
        }
        self.__display = {
            0 : ['|', '-', '-', '>']
        }
        t1 = 0
        for i in self.__coordinates:
            t2 = 0
            for j in self.__coordinates[i]:
                grid[i][j] = Shot(self.__display[t1][t2])
                t2 += 1
            t1 += 1

    def move(self, grid, fire_beams, pos, num_column, mandalorian, columns):
        if self.__alive == 0:
            return
        temp = {}
        for i in self.__coordinates:
            temp[i] = []
            for j in self.__coordinates[i]:
                if grid[i][j].shot == 1:
                    grid[i][j] = Playarea()
                temp[i].append(j + 6)

        for i in self.__coordinates:
            for j in self.__coordinates[i]:
                for k in range(0, 7):
                    if (j + k) < columns and grid[i][j + k].fire == 1:
                        mandalorian.score += 2
                        self.__alive = 0
                        num = grid[i][j + k].beam_num
                        fire_beams[num].self_destruct(grid)
                        return
                    if (j + k) >= pos + num_column:
                        self.__alive = 0

        if self.__alive == 0:
            return

        self.__coordinates.clear()
        t1 = 0
        for i in temp:
            t2 = 0
            self.__coordinates[i] = []
            for j in temp[i]:
                self.__coordinates[i].append(j)
                if grid[i][j].points == 0 and grid[i][j].magnet == 0 and grid[i][j].boost == 0:
                    grid[i][j] = Shot(self.__display[t1][t2])
                t2 += 1
            t1 += 1
