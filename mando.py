from board_obj import Board_obj
from player import Player
from playarea import Playarea
import sys
from colorama import Fore, Back, Style

class Mando:
	player_cords = {
		12: [13, 14, 15],
		13: [11, 12, 13, 14, 15],
		14: [11, 12, 13, 14, 15],
		15: [11, 13, 14, 15],
		16: [13, 15],
	}
	player_disp = {
		0: ["<", ")", ")"],
		1: [Back.RED + " " + Style.RESET_ALL, Back.RED + " " + Style.RESET_ALL, "<", ")", ")"],
		2: [Back.RED + " " + Style.RESET_ALL, Back.RED + " " + Style.RESET_ALL, Back.CYAN + " " + Style.RESET_ALL, Back.CYAN + " " + Style.RESET_ALL, Back.CYAN + " " + Style.RESET_ALL],
		3: [Back.YELLOW + "|" + Style.RESET_ALL, Back.CYAN + " " + Style.RESET_ALL, Back.CYAN + " " + Style.RESET_ALL, Back.CYAN + " " + Style.RESET_ALL],
		4: [Back.BLUE + " " + Style.RESET_ALL, Back.BLUE + " " + Style.RESET_ALL],
	}
	player_disp_with_shield = {
		0: [Fore.RED + "<" + Style.RESET_ALL, Fore.RED + ")" + Style.RESET_ALL, Fore.RED + ")" + Style.RESET_ALL],
		1: [Back.RED + " " + Style.RESET_ALL, Back.RED + " " + Style.RESET_ALL,Fore.RED + "<" + Style.RESET_ALL, Fore.RED + ")" + Style.RESET_ALL, Fore.RED + ")" + Style.RESET_ALL],
		2: [Back.RED + " " + Style.RESET_ALL, Back.RED + " " + Style.RESET_ALL, Back.MAGENTA + " " + Style.RESET_ALL, Back.MAGENTA + " " + Style.RESET_ALL, Back.MAGENTA + " "+ Style.RESET_ALL],
		3: [Back.YELLOW + "|" + Style.RESET_ALL, Back.MAGENTA + " " + Style.RESET_ALL, Back.MAGENTA + " " + Style.RESET_ALL, Back.MAGENTA + " " + Style.RESET_ALL],
		4: [Back.RED + " " + Style.RESET_ALL, Back.RED + " " + Style.RESET_ALL],
	}
	life = 1
	score = 0
	shield = 0
	Mcenter_i = 14
	Mcenter_j = 13
	cnt = 0
	__game_over_disp = {}
	with open('endgame.txt', 'r') as file:
		data = file.readlines()
		for l in data:
			li = list(l)
			__game_over_disp[cnt] = li
			__game_over_disp[cnt].pop()
			for k in range(15):
				__game_over_disp[cnt].insert(0, ' ')
			for k in range(len(__game_over_disp[cnt])):
				__game_over_disp[cnt][k] = Style.BRIGHT + Fore.RED + __game_over_disp[cnt][k] + Style.RESET_ALL
			cnt += 1

	def game_over(self):
		print('\033c')
		for i in range(24):
			for j in range(len(self.__game_over_disp[i])):
				print(self.__game_over_disp[i][j], end = '')
			print()
		print()
		print()
		print()
		print()
		print()
		print()
		for i in range(95):
			print(" ", end = '')
		print(Style.BRIGHT + Fore.YELLOW + 'Your Score: ' + str(self.score) + Style.RESET_ALL)
		for i in range(20):
			print()
		sys.exit()

	def insert_into_grid(self, grid):
		cnt1 = 0
		for i in self.player_cords:
			cnt2 = 0
			for j in self.player_cords[i]:
				grid[i][j] = Player(self.player_disp[cnt1][cnt2])
				cnt2 += 1
			cnt1 += 1
	def move_mando(self, player_column, movement, pos, grid, fire_beams, speedBoosts, num_column, ice_balls, override):
		new_player_cords = {}
		new_player_coords_shield = {}
		change_time = 0
		for i in self.player_cords:
			new_player_cords[i + movement[0]] = []
			for j in self.player_cords[i]:
				new_player_cords[i + movement[0]].append(j + movement[1])

		player_column = player_column + movement[1]
		if player_column <= pos or (player_column + 4) >= pos + num_column - 2:
			return player_column - movement[1], change_time

		if override == 0:										# override is to check for magnet
			for i in new_player_cords:
				for j in new_player_cords[i]:
					if grid[i][j].blocking == 1:
						return player_column - movement[1], change_time

		self.Mcenter_i += movement[0]
		self.Mcenter_j += movement[1]

		for i in new_player_cords:
			for j in new_player_cords[i]:
				if grid[i][j].fire == 1:
					if self.shield == 1:
						num = grid[i][j].beam_num
						fire_beams[num].self_destruct(grid)
						self.shield = 0
					elif self.life == 1:
						self.game_over()
					else:
						self.life = self.life - 1
						num = grid[i][j].beam_num
						fire_beams[num].self_destruct(grid)
				if grid[i][j].ice == 1:
					num = grid[i][j].ice_num
					ice_balls[num].self_destruct(grid)
					if self.shield == 1:
						self.shield = 0
					else:
						self.life -= 1
					if self.life == 0:
						self.game_over()


		for i in self.player_cords:
			for j in self.player_cords[i]:
				grid[i][j] = Playarea()

		self.player_cords.clear()
		cnt1 = 0
		for i in new_player_cords:
			self.player_cords[i] = []
			cnt2 = 0
			for j in new_player_cords[i]:
				if grid[i][j].points != 0:
					self.score += 1
				if grid[i][j].boost == 1:
					speedBoosts[grid[i][j].boostNum].self_destruct(grid)
					change_time = 1
				if self.shield == 1:
					grid[i][j] = Player(self.player_disp_with_shield[cnt1][cnt2])
				else:
					grid[i][j] = Player(self.player_disp[cnt1][cnt2])
				cnt2 += 1
				self.player_cords[i].append(j)
			cnt1 += 1
		return player_column, change_time

	def gravity(self, player_column, pos, grid, fire_beams, speedBoosts, num_column, ice_balls, override):
		return self.move_mando(player_column, [1, 0], pos, grid, fire_beams, speedBoosts, num_column, ice_balls, override)
