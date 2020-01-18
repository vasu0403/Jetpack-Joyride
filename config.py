rows = 30
columns = 1000
num_column = 150
player_column = 10

# shapes of object
is_coin = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]

# for generating random fire beams and objects
Rstart_pos1 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
Rstart_pos2 = [1, 2, 3, 4, 5]
Rlength1 = [7, 8, 9]
Rorientation = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
Random_object = [1, 2]
Random_object_row = []
for i in range(8, 23):
    Random_object_row.append(i)
