def buildAdj(part):
	adjList = {}
	for x in range (5):
		for y in range(5):
			adjList[(x,y)] = set()
	
	for k in adjList:
		for n in [(0,1),(1,0),(0,-1),(-1,0)]:
			nx, ny = k[0]+n[0], k[1]+n[1]
			if nx < 0 or ny < 0 or nx > 4 or ny > 4: continue
			adjList[k].add( (nx,ny,0) )

	if part == 1:
		return adjList

	for k in adjList:
		for n in [(0,1),(1,0),(0,-1),(-1,0)]:
			nx, ny = k[0]+n[0], k[1]+n[1]
			if nx == -1: adjList[k].add( (1, 2, -1) )
			elif nx == 5: adjList[k].add( (3, 2, -1) )			
			elif ny == -1: adjList[k].add( (2, 1, -1) )
			elif ny == 5: adjList[k].add( (2, 3, -1) )
		if (2,2,0) in adjList[k]: adjList[k].remove((2,2,0))

	adjList[(1,2)].update({(0, i, 1) for i in range(5)})
	adjList[(3,2)].update({(4, i, 1) for i in range(5)})
	adjList[(2,1)].update({(i, 0, 1) for i in range(5)})
	adjList[(2,3)].update({(i, 4, 1) for i in range(5)})
	
	return adjList


def getNextGen(bugs, dic):

	grid = set()
	for b in bugs:
		for n in dic[(b[0],b[1])]:
			grid.add( (n[0],n[1],n[2]+b[2]) )

	newBugs = set()

	for p in grid:

		counter = 0
		for n in dic[(p[0],p[1])]:
			n = (n[0],n[1],n[2]+p[2])
			if n in bugs:
				counter += 1

		if counter not in {1,2}:
			continue

		if counter == 2 and p in bugs:
			continue

		newBugs.add(p)

	return newBugs


def getRating(bugs):
	r = 0
	for b in bugs:
		x, y, _ = b
		exp = y*5 + x
		r += pow(2,exp)
	return r
	

lines = open("input.txt").read().split("\n")

bugs = set()
for y, line in enumerate(lines):
	for x, char in enumerate(line):
		if char == "#":
			bugs.add( (x,y,0) )


p1Bugs = bugs.copy()
adjList = buildAdj(1)
allRatings = set()
while True:
	rating = getRating(p1Bugs)
	if rating in allRatings: break
	allRatings.add(rating)
	p1Bugs = getNextGen(p1Bugs, adjList)

print("Part 1: " + str(rating))


p2Bugs = bugs.copy()
adjList = buildAdj(2)
for _ in range(200):
	p2Bugs = getNextGen(p2Bugs, adjList)

print("Part 2: " + str( len(p2Bugs) ))