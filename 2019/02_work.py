with open('02_input.txt','r') as f:
	input_text = f.read().split(',')
xx,og = [],[]
for i in range(len(input_text)):
	xx.append(int(input_text[i]))
	og.append(int(input_text[i]))

xx[1],xx[2] = 12,2
i = 0
while i < len(xx) - 3:
	if xx[i] == 99:
		i = 9999
	elif xx[i] == 1:
		xx[xx[i+3]] = xx[xx[i+1]] + xx[xx[i+2]]
	elif xx[i] == 2:
		xx[xx[i+3]] = xx[xx[i+1]] * xx[xx[i+2]]
	else:
		print('error |', i, xx[i])
	i += 4
print(xx[0])
print()

#part 2
xx = [j for j in og]
for a in range(100):
	for b in range(100):
		xx[1] = a
		xx[2] = b
		i = 0
		while i < len(xx) - 3:
			if xx[i] == 99:
				i = 9999
			elif xx[i] == 1:
				xx[xx[i+3]] = xx[xx[i+1]] + xx[xx[i+2]]
			elif xx[i] == 2:
				xx[xx[i+3]] = xx[xx[i+1]] * xx[xx[i+2]]
			else:
				print('error |', i, xx[i],xx)
			i += 4
		if xx[0] == 19690720:
			print((100*a) + b)
		xx = [j for j in og]