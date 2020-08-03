from intcpu import intcpu 
import itertools 

def getArray(arr):
	scaf = []
	row = []
	for e in arr:
		if e == 10: 
			scaf.append(row)
			row = []
		else:
			row.append(e)
	return scaf


def getSet(arr):
	path = set()
	for y in range(len(arr)):
		for x in range(len(arr[y])):
			if arr[y][x] == ord("#"): path.add( (x,y) )
	return path


def getIntersections(aSet):
	neighbours = [(0,1),(1,0),(0,-1),(-1,0)]
	intersections = []
	for point in aSet:
		flag = True
		for n in neighbours:
			x = point[0]+n[0]
			y = point[1]+n[1]
			if (x,y) not in aSet:
				flag = False

		if flag: intersections.append(point)
	return intersections


def findBot(arr):
	for y in range(len(arr)):
		for x in range(len(arr[y])):
			if arr[y][x] == ord("^"): 
				return (x,y)	

def draw(arr):
	for line in arr:
		string = ""
		for char in line:
			string += chr(char)
		print(string)

def getMoves(pos, path):
	visited = set()
	moves = []
	steps = 0
	dirs = {"up": (0,-1),"down": (0,1),"left": (-1,0),"right": (1,0)}
	turns = {"up": ("left","right"),"down": ("right","left"),"left": ("down", "up"),"right": ("up","down")}
	currentDir = "up"
	while len(path) > len(visited):
		
		
		x = pos[0] + dirs[currentDir][0]
		y = pos[1] + dirs[currentDir][1]
		if (x,y) not in path:
			moves.append(str(steps))
			steps = 0
			left = turns[currentDir][0]
			right = turns[currentDir][1]
			x = pos[0] + dirs[left][0]
			y = pos[1] + dirs[left][1]
			if (x,y) in path:
				currentDir = left
				moves.append("L")
			else:
				currentDir = right
				moves.append("R")
			continue
		pos = (x,y)
		steps += 1
		visited.add(pos)
		#print(pos)
	moves.append(str(steps))
	moves.pop(0)
	return moves

def getSubstr(string):
	substrings = set([string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) +1)] )
	for s in substrings.copy():
		if len(s) < 8 or len(s) > 20:
			substrings.remove(s)
		elif s[0] == "," or s[-1] != ",":
			substrings.remove(s)
		elif s[0] not in ["L","R"]:
			substrings.remove(s)

	for p in itertools.permutations(substrings, 3):
		if "" == string.replace(p[0],"").replace(p[1],"").replace(p[2],""):
			return [s[:-1] for s in p]	


toAscii = lambda string: [ord(char) for char in string]


program = [int(string) for string in open('input.txt').read().split(",")]

vacuumBot = intcpu(program)
view = vacuumBot.getAll()

asArray = getArray(view)
asSet = getSet(asArray)
intersections = getIntersections(asSet)

draw(asArray)

part1 = sum(i[0]*i[1] for i in intersections)
print("Part 1: " + str(part1))

botPosition = findBot(asArray)
moves = ",".join( getMoves(botPosition, asSet) ) + ","

functions = getSubstr(moves)
dic = {functions[0]: "A", functions[1]: "B", functions[2]: "C"}
routine = []

while moves:
	for fn in functions:
		if fn == moves[:len(fn)]:
			routine.append(dic[fn])
			moves = moves[len(fn)+1:]
			break
	else:		
		break



#print(routine)
print(functions)

# A - R,8,L,12,R,8,
# A - R,8,L,12,R,8,
# B - L,10,L,10,R,8,
# C - L,12,L,12,L,10,R,10,
# B - L,10,L,10,R,8,
# C - L,12,L,12,L,10,R,10,
# B - L,10,L,10,R,8,
# A - R,8,L,12,R,8,
# C - L,12,L,12,L,10,R,10,
# A - R,8,L,12,R,8

program[0] = 2
vacuumBot = intcpu(program)

movementRoutine = toAscii("A,A,B,C,B,C,B,A,C,A\n")
movementRoutine = toAscii(",".join(routine) + "\n")
movementA = toAscii("R,8,L,12,R,8\n")
movementA = toAscii(functions[0] + "\n")
movementB = toAscii("L,10,L,10,R,8\n")
movementB = toAscii(functions[1] + "\n")
movementC = toAscii("L,12,L,12,L,10,R,10\n")
movementC = toAscii(functions[2] + "\n")
videoFeed = toAscii("n\n")

for char in movementRoutine + movementA + movementB + movementC + videoFeed:
	vacuumBot.provide(char)

part2 = vacuumBot.getFinal()
print("Part 2: " + str(part2))
