import numpy

positions = []
speeds = [[0 for x in range(3)] for y in range(4)]

for line in open('input.txt').read().split("\n"):
	arr = []
	if line:
		for coord in line.replace("<","").replace(">","").replace(",","").split(" "):
			arr.append(int(coord[2:]))
		positions.append(arr)

def simulate(pos, vel, steps):
	for _ in range(steps):

		for fst in range(len(vel)):
			for snd in range(fst+1, len(vel)):
				for axis in range(3):
					if pos[fst][axis] > pos[snd][axis]:
						vel[fst][axis] -= 1
						vel[snd][axis] += 1
					elif pos[fst][axis] < pos[snd][axis]:
						vel[fst][axis] += 1
						vel[snd][axis] -= 1

		for i in range(len(pos)):
			for axis in range(3):
				pos[i][axis] += vel[i][axis] 

def getEnergy(pos, vel):
	res = 0
	for i in range(len(pos)):
		pot, kin = 0, 0
		for v in range(3):
			pot += abs(pos[i][v])
			kin += abs(vel[i][v])
		res += pot * kin
	return res

n = 1000
simulate(positions, speeds, n)
energy = getEnergy(positions, speeds)
print("Part 1: " + str(energy))

arr = [0,0,0]
run = True
while run:
	simulate(positions, speeds, 1)
	n += 1
	for v in range(3):		
		for i in range(len(speeds)):
			if speeds[i][v] != 0:
				break
		else:
			if arr[v] == 0:
				arr[v] = n
				if not 0 in arr:
					run = False
			
part2 = 2* numpy.lcm.reduce(arr)
print("Part 2: " + str(part2))


