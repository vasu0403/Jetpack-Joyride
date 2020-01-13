from board import Board
from config import *
from scenery import *
import time
import signal
import os
import sys
from alarmexception import AlarmException
from getch import _getChUnix as getChar
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
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''

prev_time = time.time()
game_board.insert_boundary()
game_board.insert_playarea()
game_board.insert_player()
while True:
	char = user_input()
	if char == 'q':
		break
	elif char == 'd':
		player_column = game_board.move_player(player_cords, player_column, [0, 1], game_board.pos)
		game_board.display()
	elif char == 'a':
		player_column = game_board.move_player(player_cords, player_column, [0, -1], game_board.pos)
		game_board.display()
	elif char == 'w':
		player_column = game_board.move_player(player_cords, player_column, [-1, 0], game_board.pos)
		game_board.display()
	elif char == 's':
		player_column = game_board.move_player(player_cords, player_column, [1, 0], game_board.pos)
		game_board.display()
	cur_time = time.time()
	if cur_time - prev_time >= 0.15:
		prev_time = cur_time
		game_board.gravity(player_cords)
		game_board.pos = game_board.pos + 1
		if game_board.pos == player_column:
			player_column = game_board.move_player(player_cords, player_column, [0, 1], game_board.pos)
		game_board.display()