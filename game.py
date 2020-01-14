from board import Board
from config import *
from scenery import *
import time
import signal
import os
import sys
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from colorama import Fore, Back, Style
from mando import Mando
from beam import Beam
import random
game_board = Board(rows, columns, num_column)

game_board.create_grid()
sys.stderr.write("\x1b[2J\x1b[H")
def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.15):
	''' input method '''
	signal.signal(signal.SIGALRM, alarmhandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	
	try:
		text = getChar()()
		signal.alarm(0)
		print(text)
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''

prev_time = time.time()
game_board.insert_boundary()
game_board.insert_playarea()
mandalorian = Mando()
mandalorian.insert_into_grid(game_board.grid)
fire_beams = []
beam_num = 0
for i in range(40, columns - 151, 45):
	random.shuffle(Rstart_pos1)
	random.shuffle(Rstart_pos2)
	random.shuffle(Rlength1)
	random.shuffle(Rorientation)
	start_pos_i = Rstart_pos1[0]
	start_pos_j = i + Rstart_pos2[0]
	length = Rlength1[0]
	orientation = Rorientation[0]
	fire_beams.append(Beam(start_pos_i, start_pos_j, length, orientation, game_board.grid, beam_num))
	beam_num = beam_num + 1

while True:
	char = user_input()
	if char == 'q':
		break
	elif char == 'd':
		player_column = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams)
		game_board.display(mandalorian.life)
	elif char == 'a':
		player_column = mandalorian.move_mando(player_column, [0, -1], game_board.pos, game_board.grid, fire_beams)
		game_board.display(mandalorian.life)
	elif char == 'w':
		player_column = mandalorian.move_mando(player_column, [-1, 0], game_board.pos, game_board.grid, fire_beams)
		game_board.display(mandalorian.life)
	elif char == 's':
		player_column = mandalorian.move_mando(player_column, [1, 0], game_board.pos, game_board.grid, fire_beams)
		game_board.display(mandalorian.life)
	cur_time = time.time()
	if cur_time - prev_time >= 0.15:
		prev_time = cur_time
		player_column = mandalorian.gravity(player_column, game_board.pos, game_board.grid, fire_beams)
		game_board.pos = game_board.pos + 1
		if game_board.pos == player_column:
			player_column = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams)
		game_board.display(mandalorian.life)