input_text = []
with open ('03_input.txt','r') as f:
	for line in f:
		input_text.append(line.split(','))

path1 = input_text[0]
path2 = input_text[1]

locations1 = []
x_locations1 = []
y_locations1 = []
stepcount1 = 0
locations2 = []
x_locations2 = []
y_locations2 = []
stepcount2 = 0
def movement_one(xx):
	# xx is a string direction, eg. 'R8'
	direction = xx[0]
	count = int(xx[1:])
	x,y = cur_loc1
	global stepcount1
	for i in range(count):
		if direction == 'R':
			cur_loc1[0] += 1
			x += 1
		elif direction == 'D':
			cur_loc1[1] -= 1
			y -= 1
		elif direction == 'L':
			cur_loc1[0] -= 1
			x -= 1
		elif direction == 'U':
			cur_loc1[1] += 1
			y += 1
		else:
			print('unknown direction', direction)
		stepcount1 += 1
		locations1.append([x,y,stepcount1])
		x_locations1.append(x)
		y_locations1.append(y)

def movement_two(xx):
	# xx is a string direction, eg. 'R8'
	direction = xx[0]
	count = int(xx[1:])
	x,y = cur_loc2
	global stepcount2
	for i in range(count):
		if direction == 'R':
			cur_loc2[0] += 1
			x += 1
		elif direction == 'D':
			cur_loc2[1] -= 1
			y -= 1
		elif direction == 'L':
			cur_loc2[0] -= 1
			x -= 1
		elif direction == 'U':
			cur_loc2[1] += 1
			y += 1
		else:
			print('unknown direction', direction)
		stepcount2 += 1
		locations2.append([x,y,stepcount2])
		x_locations2.append(x)
		y_locations2.append(y)

cur_loc1 = [0,0]
cur_loc2 = [0,0]
for i in path1:
	movement_one(i)
for i in path2:
	movement_two(i)

x_set_locations1 = set(x_locations1)
x_set_locations2 = set(x_locations2)
x_crossovers = []
for i in x_set_locations1:
	for j in x_set_locations2:
		if i == j:
			x_crossovers.append(i)
print('x crossovers done',len(x_crossovers))

y_set_locations1 = set(y_locations1)
y_set_locations2 = set(y_locations2)
y_crossovers = []
for i in y_set_locations1:
	for j in y_set_locations2:
		if i == j:
			y_crossovers.append(i)
print('y crossovers done',len(y_crossovers))

crossovers = []
mini = 999999999999
for i in locations1:
	if i[2] > mini:
		break
	if i[0] not in x_crossovers or i[1] not in y_crossovers:
		continue
	for j in locations2:
		if j[2] > mini:
			continue
		if i[0] == j[0] and i[1] == j[1]:
			if i[2] + j[2] < mini:
				mini = i[2] + j[2]
				print(mini)