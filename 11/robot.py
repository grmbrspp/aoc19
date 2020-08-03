from intcpu import intcpu 

def runRobot(prog, startColor):
	movements = [(0,1),(-1,0),(0,-1),(1,0)] # up, left, down, right
	
	panels = {(0,0): startColor}
	position = (0,0)
	direction = 0
	
	brain = intcpu(prog)
	while not brain.halted:
		inp = 0 if position not in panels else panels[position]
		brain.provide(inp)
		panels[position] = brain.getNext()
		direction += 1 if brain.getNext() == 0 else -1
		direction = direction if direction < 4 else 0
		direction = direction if direction >=0 else 3
		x = position[0] + movements[direction][0]
		y = position[1] + movements[direction][1]
		position = (x,y)
	
	return panels
	
program = [int(string) for string in open('input2.txt').read().split(",")]

part1 = runRobot(program.copy(), 0)
print("Part 1: " + str(len(part1)))

part2 = runRobot(program.copy(), 1)
print("Part 2:" + "\n")

maxX, maxY = 0, 0
for point in part2.keys():
	maxX = point[0] if point[0] > maxX else maxX
	maxY = point[1]*-1 if point[1]*-1 > maxY else maxY

grid = [[" " for x in range(maxX+1)] for y in range(maxY+1)	]

for point, color in part2.items():
	if color == 1:
		x, y = point[0], point[1]*-1
		grid[y][x] = "#"
		
for y in grid:
	line = "" 
	for x in y:
		line += x
	print(line)