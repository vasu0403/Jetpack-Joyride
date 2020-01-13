from boundary import Boundary

def create_sky(game_board):
	l1 = []
	l2 = []
	for i in range(game_board.columns):
		l1.append("*")
	for i in range(game_board.columns):
		l2.append("-")
	for i in range(game_board.columns):
		game_board.grid[0][i] = Boundary(l1[i])
		game_board.grid[1][i] = Boundary(l1[i])
	for i in range(game_board.columns):
		game_board.grid[2][i] = Boundary(l2[i])