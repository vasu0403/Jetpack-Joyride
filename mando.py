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
	life = 3
	score = 0
	def insert_into_grid(self, grid):
		cnt1 = 0
		for i in self.player_cords:
			cnt2 = 0
			for j in self.player_cords[i]:
				grid[i][j] = Player(self.player_disp[cnt1][cnt2])
				cnt2 += 1
			cnt1 += 1
	def move_mando(self, player_column, movement, pos, grid, fire_beams, speedBoosts):
		new_player_cords = {}
		change_time = 0
		for i in self.player_cords:
			new_player_cords[i + movement[0]] = []
			for j in self.player_cords[i]:
				new_player_cords[i + movement[0]].append(j + movement[1])

		player_column = player_column + movement[1]
		if player_column <= pos:
			return player_column - movement[1], change_time

		for i in new_player_cords:
			for j in new_player_cords[i]:
				if grid[i][j].fire == 1:
					if self.life == 1:
						sys.exit()										# display some message maybe
					else:
						self.life = self.life - 1
						num = grid[i][j].beam_num
						fire_beams[num].self_destruct(grid)
		for i in new_player_cords:
			for j in new_player_cords[i]:
				if grid[i][j].blocking == 1:
					return player_column, change_time

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
				grid[i][j] = Player(self.player_disp[cnt1][cnt2])
				cnt2 += 1
				self.player_cords[i].append(j)
			cnt1 += 1
		return player_column, change_time

	def gravity(self, player_column, pos, grid, fire_beams, speedBoosts):
		return self.move_mando(player_column, [1, 0], pos, grid, fire_beams, speedBoosts)
