from board import Board
from config import *
from scenery import *
import time
game_board = Board(rows, columns, num_column)
game_board.create_grid()

game_board.insert_boundary()
game_board.insert_playarea()
game_board.insert_player()
# game_board.display()
while True:
	player_cords = game_board.gravity(player_cords)
	game_board.display()
	print(type(player_cords))
	time.sleep(0.15)
	game_board.pos = game_board.pos + 1