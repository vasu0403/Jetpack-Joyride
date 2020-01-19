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
from coins import Coin
from speedBoost import SpeedBoost
from gunShot import GunShot
import random
game_board = Board(rows, columns, num_column)

game_board.create_grid()
sys.stderr.write("\x1b[2J\x1b[H")
def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.03):
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

speedBoost_num = 0
speedBoosts = []

time_diff = 0.15
change_time = 0
time_of_change = time.time()

gun_shots = []
gun_shot_num = 0
for i in range(40, columns - 151, 70):             # adding fire beams on the board
	random.shuffle(Rstart_pos1)
	random.shuffle(Rstart_pos2)
	random.shuffle(Rlength1)
	random.shuffle(Rorientation)
	start_pos_i = Rstart_pos1[0]
	start_pos_j = i + Rstart_pos2[0]
	length = Rlength1[0]
	orientation = Rorientation[0]
	if orientation[0] == 0:
		length += 6
	fire_beams.append(Beam(start_pos_i, start_pos_j, length, orientation, game_board.grid, beam_num))
	beam_num = beam_num + 1

for i in range(65, columns - 151, 70):					# adding coins, speed boost and magnets
	random.shuffle(Random_object)
	random.shuffle(Random_object_row)
	object_type = Random_object[0]
	object_middle_row = Random_object_row[0]			# containes the middle row of object to placed on board

	if object_type == 1:								# object_type 1 is for coins
		for j in range(-2, 3):
			for k in range(5):
				if is_coin[j + 2][k] == 1:
					game_board.grid[object_middle_row + j][i + k] = Coin()

	elif object_type == 2:								# object_type 2 is for spped boost
		speedBoosts.append(SpeedBoost(object_middle_row, i, game_board.grid, speedBoost_num))
		speedBoost_num += 1

while True:
	char = user_input()
	cur_time = time.time()
	if char == 'q':
		break

	elif char == 'd':
		player_column, change_time = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams, speedBoosts)
		game_board.display(mandalorian.life, mandalorian.score)

	elif char == 'a':
		player_column, change_time = mandalorian.move_mando(player_column, [0, -1], game_board.pos, game_board.grid, fire_beams, speedBoosts)
		game_board.display(mandalorian.life, mandalorian.score)

	elif char == 'w':
		player_column, change_time = mandalorian.move_mando(player_column, [-1, 0], game_board.pos, game_board.grid, fire_beams, speedBoosts)
		game_board.display(mandalorian.life, mandalorian.score)

	elif char == 's':
		player_column, change_time = mandalorian.move_mando(player_column, [1, 0], game_board.pos, game_board.grid, fire_beams, speedBoosts)
		game_board.display(mandalorian.life, mandalorian.score)

	elif char == 'e':
		gun_shots.append(GunShot(gun_shot_num, mandalorian.player_cords, game_board.grid))
		game_board.display(mandalorian.life, mandalorian.score)

	if change_time == 1:
		change_time = 0
		time_diff = 0.04
		time_of_change = time.time()

	if cur_time - time_of_change >= 10:
		time_diff = 0.15

	if cur_time - prev_time >= time_diff:
		for shots in gun_shots:
			shots.move(game_board.grid, fire_beams, game_board.pos, game_board.num_column)
		prev_time = cur_time
		player_column, change_time = mandalorian.gravity(player_column, game_board.pos, game_board.grid, fire_beams, speedBoosts)
		game_board.pos = game_board.pos + 1
		if game_board.pos == player_column:
			player_column, change_time = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams, speedBoosts)
		game_board.display(mandalorian.life, mandalorian.score)
		if change_time == 1:
			change_time = 0
			time_diff = 0.04
			time_of_change = time.time()
