import time
import signal
import os
import sys
import random
import math

from board import Board
from config import *
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from colorama import Fore, Back, Style
from mando import Mando
from beam import Beam
from coins import Coin
from speedBoost import SpeedBoost
from gunShot import GunShot
from dragon import Dragon
from iceBall import IceBall
from magnet import Magnet
from playarea import Playarea

def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.04):
	''' input method '''
	signal.signal(signal.SIGALRM, alarmhandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)

	try:
		text = getChar()()
		signal.alarm(0)
		# print(text)
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''

game_board = Board(rows, columns, num_column)
game_board.create_grid()
print('\033c')
prev_time = time.time()

game_board.insert_boundary()
game_board.insert_playarea()
mandalorian = Mando()
mandalorian.insert_into_grid(game_board.grid)
game_board.grid[6][columns - 36].disp = 'X'

fire_beams = []
beam_num = 0

speedBoost_num = 0
speedBoosts = []

time_diff = 0.13
change_time = 0
time_of_change = time.time()
make_fast = 0

shield_cooloff_time = 0
shield_remaining_time = 0
prev_shield_time = 0;

gun_shots = []
gun_shot_num = 0

gravity_time = 0

boss = Dragon(columns)
boss.insert(game_board.grid)
ice_balls = []
ice_ball_num = 0
prev_ice_ball_shoot = time.time()

time_left = 70
prev_time_left = time.time()
game_end = 0

for i in range(40, columns - 181, 70):             # adding fire beams on the board
	random.shuffle(Rstart_pos1)
	random.shuffle(Rstart_pos2)
	random.shuffle(Rlength1)
	random.shuffle(Rorientation)
	random.shuffle(num_fire_beams)
	random.shuffle(Rstart_pos1_2beams)
	random.shuffle(Rstart_pos2_2beams)
	random.shuffle(Rlength1_2beams)
	random.shuffle(Rstart_pos3_2beams)

	num_beams = num_fire_beams[0]
	if num_beams == 1:
		start_pos_i = Rstart_pos1[0]
		start_pos_j = i + Rstart_pos2[0]
		length = Rlength1[0]
		orientation = Rorientation[0]
		if orientation[0] == 0:
			length += 6
		fire_beams.append(Beam(start_pos_i, start_pos_j, length, orientation, game_board.grid, beam_num))
		beam_num = beam_num + 1
	else:
		orientation1 = Rorientation[0]
		orientation2 = Rorientation[1]
		if (orientation1 == [1, 1] or orientation1 == [1, -1]):
			orientation2 = [1, 0]
		if (orientation1 == [1, 0]):
			orientation2 = [1, 1]
		start_pos_j1 = i + Rstart_pos3_2beams[0]
		start_pos_j2 = i + Rstart_pos3_2beams[1]
		start_pos_i1 = Rstart_pos1_2beams[0]
		start_pos_i2 = Rstart_pos2_2beams[0]
		length1 = Rlength1_2beams[0]
		length2 = Rlength1_2beams[1]
		if orientation1[0] == 0:
			length1 += 5
		if orientation2[0] == 0:
			length2 += 5
		fire_beams.append(Beam(start_pos_i1, start_pos_j1, length1, orientation1, game_board.grid, beam_num))
		beam_num = beam_num + 1
		fire_beams.append(Beam(start_pos_i2, start_pos_j2, length2, orientation2, game_board.grid, beam_num))
		beam_num = beam_num + 1
for i in range(65, columns - 181, 70):					# adding coins, speed boost and magnets
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

	elif object_type == 3:
		Magnet(object_middle_row, i, game_board.grid)
prev_ice_ball_shoot = time.time()
while True:
	char = user_input()
	cur_time = time.time()
	if cur_time - prev_time_left >= 1:
		time_left -= 1
		prev_time_left = cur_time
		if time_left <= 0:
			mandalorian.game_over()
	if cur_time - prev_shield_time >= 1:
		prev_shield_time = cur_time
		if shield_remaining_time > 0:
			shield_remaining_time -= 1
		if shield_cooloff_time > 0:
			shield_cooloff_time -= 1

	if shield_remaining_time <= 0 and mandalorian.shield == 1:
		mandalorian.shield = 0

	if char == 'q':
		break

	elif char == 'd':
		player_column, change_time = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
		game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)

	elif char == 'a':
		player_column, change_time = mandalorian.move_mando(player_column, [0, -1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
		game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)


	elif char == 'w':
		player_column, change_time = mandalorian.move_mando(player_column, [-1, 0], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
		game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)
		boss.move([-1, 0], game_board.grid)
		gravity_time = 0

	elif char == 's':
		player_column, change_time = mandalorian.move_mando(player_column, [1, 0], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
		game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)
		boss.move([1, 0], game_board.grid)

	elif char == 'e':
		gun_shots.append(GunShot(gun_shot_num, mandalorian.player_cords, game_board.grid))
		game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)


	elif len(char) > 0 and ord(char) == 32:
		if shield_cooloff_time <= 0:
			mandalorian.shield = 1
			shield_cooloff_time = 60
			shield_remaining_time = 10
			prev_shield_time = time.time()
			game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)

	do_attract = 0
	attract_toi = -1
	attract_toj = -1
	# print(mandalorian.Mcenter_i, mandalorian.Mcenter_j)
	for i in range(mandalorian.Mcenter_i - 10, mandalorian.Mcenter_i + 10):
		if i < 0 or i >=rows:
			continue
		for j in range(mandalorian.Mcenter_j - 15, mandalorian.Mcenter_j + 15):
			if j < 0 or j >=columns:
				continue
			if game_board.grid[i][j].attr == 1:
				do_attract = 1
				attract_toi = game_board.grid[i][j].centre_i
				attract_toj = game_board.grid[i][j].centre_j

	player_lower_coord_list = list(mandalorian.player_cords.keys())
	player_lower_coord_list.sort()
	player_lower_coord = player_lower_coord_list[4]

	if player_lower_coord == rows - 4 or char == 'w' or do_attract == 1:
		gravity_time = 0
	else:
		gravity_time += 1
		gravity_times = math.ceil((0.5 * 9.8 * gravity_time * gravity_time) / 2000)
		for i in range(gravity_times):
			player_column, change_time = mandalorian.gravity(player_column, game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
			boss.move([1, 0], game_board.grid)
			if change_time == 1:
				change_time = 0
				time_diff = 0.05
				time_of_change = time.time()


	if change_time == 1:
		change_time = 0
		time_diff = 0.05
		time_of_change = time.time()

	if cur_time - time_of_change >= 10:
		time_diff = 0.13

	if cur_time - prev_time >= time_diff:
		if do_attract == 1:
			if mandalorian.Mcenter_i < attract_toi:
				player_column, change_time = mandalorian.move_mando(player_column, [1, 0], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
			else:
				player_column, change_time = mandalorian.move_mando(player_column, [-1, 0], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
			if change_time == 1:
				change_time = 0
				time_diff = 0.05
				time_of_change = time.time()

			if mandalorian.Mcenter_j < attract_toj:
				player_column, change_time = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
			else:
				player_column, change_time = mandalorian.move_mando(player_column, [0, -1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
				player_column, change_time = mandalorian.move_mando(player_column, [0, -1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)

			if change_time == 1:
				change_time = 0
				time_diff = 0.05
				time_of_change = time.time()

		for shots in gun_shots:
			game_over = shots.move(game_board.grid, fire_beams, game_board.pos, game_board.num_column, mandalorian, columns, ice_balls, boss)
			if game_over == 1:
				game_end = 1
				break
		if game_end == 1:
			break

		for balls in ice_balls:
			balls.move(game_board.grid, game_board.pos, mandalorian)
		prev_time = cur_time

		if change_time == 1:
			change_time = 0
			time_diff = 0.05
			time_of_change = time.time()

		if game_board.pos <= columns - num_column - 1:
			game_board.pos = game_board.pos + 1
			player_column, change_time = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
			if change_time == 1:
				change_time = 0
				time_diff = 0.05
				time_of_change = time.time()

		if game_board.pos > columns - num_column - 1:
			if time.time() - prev_ice_ball_shoot >= 1.5:
				prev_ice_ball_shoot = time.time()
				ice_balls.append(IceBall(ice_ball_num, boss.upper_coordinate + 1, columns - 39, game_board.grid))
				ice_ball_num += 1
				ice_balls.append(IceBall(ice_ball_num, boss.upper_coordinate + 5, columns - 39, game_board.grid))
				ice_ball_num += 1
				ice_balls.append(IceBall(ice_ball_num, boss.upper_coordinate + 9, columns - 39, game_board.grid))
				ice_ball_num += 1

		if game_board.pos >= player_column:
			player_column, change_time = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 1)
			if change_time == 1:
				change_time = 0
				time_diff = 0.05
				time_of_change = time.time()
		game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)
if game_end == 1:
	print('\033c')
	for i in range(game_board.rows):
		for j in range(game_board.pos, game_board.pos + game_board.num_column):
			if game_board.grid[i][j].playarea != 1 and game_board.grid[i][j].blocking != 1 and game_board.grid[i][j].player != 1:
				game_board.grid[i][j] = Playarea()

	game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)
	time.sleep(2)

	while(True):
		player_column, change_time = mandalorian.move_mando(player_column, [1, 0], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
		player_column, change_time = mandalorian.move_mando(player_column, [0, 1], game_board.pos, game_board.grid, fire_beams, speedBoosts, num_column, ice_balls, 0)
		game_board.display(mandalorian.life, mandalorian.score, mandalorian.shield, shield_remaining_time, shield_cooloff_time, boss.life, time_left)
		time.sleep(0.01)
		print(columns, mandalorian.Mcenter_j)
		if mandalorian.Mcenter_j > columns - 7:
			break
	mandalorian.game_won()
