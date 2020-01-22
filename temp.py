cnt = 0
disp = {}
with open('endgame.txt', 'r') as file:
	data = file.readlines()
	for l in data:
		li = list(l)
		disp[cnt] = li
		disp[cnt].pop()
		cnt += 1
l = list(disp.keys())
print(len(l))
