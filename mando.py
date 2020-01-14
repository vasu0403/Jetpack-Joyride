from board_obj import Board_obj
from player import Player
from playarea import Playarea

class Mando:
	player_cords = {
		12 : [10, 11, 12],
		13 : [10, 11, 12],
		14 : [11],
		15 : [11],
	}
	def insert_into_grid(self, grid):
		for i in self.player_cords:
			for j in self.player_cords[i]:
				grid[i][j] = Player()

	def move_mando(self, player_column, movement, pos, grid):
		new_player_cords = {}
		for i in self.player_cords:
			new_player_cords[i + movement[0]] = []
			for j in self.player_cords[i]:
				new_player_cords[i + movement[0]].append(j + movement[1])
		
		player_column = player_column + movement[1] 
		if player_column <= pos:
			return player_column - movement[1]
		for i in new_player_cords:
			for j in new_player_cords[i]:
				if grid[i][j].blocking == 1:
					return player_column							## Add condition for fire beams and enemies here
		
		for i in self.player_cords:
			for j in self.player_cords[i]:
				grid[i][j] = Playarea()

		self.player_cords.clear()
		for i in new_player_cords:
			self.player_cords[i] = []
			for j in new_player_cords[i]:
				grid[i][j] = Player()
				self.player_cords[i].append(j)
		return player_column
		
	def gravity(self, player_column, pos, grid):
		return self.move_mando(player_column, [1, 0], pos, grid)