rows = 30
columns = 700
num_column = 150
player_column = 11

# shapes of object
is_coin = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]

# for generating random fire beams and objects
num_fire_beams = [1, 2]
Rstart_pos1 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
Rstart_pos2 = [1, 2, 3, 4, 5]
Rlength1 = [9, 10, 11]
Rstart_pos1_2beams = [8, 9]
Rstart_pos2_2beams = [20, 21]
Rstart_pos3_2beams = [1, 3, 5]
Rlength1_2beams = [9, 10, 11]
Rorientation = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
# Rorientation = [[-1, 0], [1, 0]]

Random_object = [1, 2]
Random_object_row = []
for i in range(8, 23):
    Random_object_row.append(i)
