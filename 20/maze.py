import networkx as nx
import string

def getPoint(x,y):
	neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
	for n in neighbours:
		try:
			if arr[y+n[1]][x+n[0]] == ".":
				return (x+n[0], y+n[1])
		except:
			pass
	return None

g = nx.Graph()

lines = open('input.txt').read().split("\n")

path = set()
portals = {}

arr = []
for line in lines:
	row = []
	for char in line:
		row.append(char)
	if row: arr.append(row)

for y, line in enumerate(arr):
	for x, char in enumerate(line):
		if char == ".":
			path.add((x,y))

		elif char in string.ascii_uppercase:
			p = getPoint(x,y)
			if not p: continue
			elif x < p[0]: portal = arr[y][x-1] + arr[y][x]
			elif x > p[0]: portal = arr[y][x] + arr[y][x+1]
			elif y < p[1]: portal = arr[y-1][x] + arr[y][x]
			elif y > p[1]: portal = arr[y][x] + arr[y+1][x]
			
			portals[portal] = portals.get(portal, []) + [p]
			

for p in path:
	n = (p[0]+1, p[1])
	if n in path: g.add_edge(p, n)
	n = (p[0], p[1]+1)
	if n in path: g.add_edge(p, n)

sameLevelEdges = g.edges()

for _, v in portals.items():
	if len(v) != 2:
		continue
	g.add_edge(v[0], v[1])



part1 = nx.shortest_path_length(g, source=portals["AA"][0], target=portals["ZZ"][0])
print("Part 1: " + str(part1))

h = nx.Graph()
levels = 32
xEdge, yEdge = {2, len(arr[0])-3}, {2, len(arr)-3}
source, target = None, None

for l in range(levels):
	
	for p in path:
		neighbours = [(p[0]+1, p[1]), (p[0], p[1]+1)]
		for n in neighbours:
			if n not in path: continue			
			p = (p[0], p[1], l)
			n = (n[0], n[1], l) 
			h.add_edge(p, n)

	#for e in sameLevelEdges:
	#	h.
		
	for k, v in portals.items():
		if len(v) != 2:
			if k == "AA": source = v[0][0], v[0][1], 0
			elif k == "ZZ": target = v[0][0], v[0][1], 0
			continue

		e, f = v[0], v[1]
		if f[0] in xEdge or f[1] in yEdge:
			e, f = f, e
		e = (e[0], e[1], l+1)
		f = (f[0], f[1], l)
		h.add_edge(e, f)	


part2 = nx.shortest_path_length(h, source=source, target=target)
print("Part 2: " + str(part2))