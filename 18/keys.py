import networkx as nx
import string
import heapq
import timeit

def getArray(lines):
	res = []
	for line in lines:
		row = []
		for char in line:
			row.append(char)
		if row: res.append(row)
	return res

def getPoints(arr):
	path = set()
	keys, doors = {}, {}

	starts = ["@", "!", "§", "$"]

	for y, row in enumerate(arr):
		for x, char in enumerate(row):
			if char == "#":
				continue

			elif char == ".":
				pass

			elif char in string.ascii_lowercase:
				keys[char] = (x,y)

			elif arr[y][x] in string.ascii_uppercase:
				doors[char] = (x,y)
				#continue

			elif char == "@":
				name = starts.pop(0)
				keys[name] = (x,y)
			
			path.add((x,y))

	return (path, keys, doors)

def buildGraph(path):
	res = nx.Graph()
	for p in path:
		res.add_node(p)
		n = (p[0]+1, p[1])
		if n in path: res.add_edge(p, n)
		n = (p[0], p[1]+1)
		if n in path: res.add_edge(p, n)

	return res
	

def getDistances(keys, graph):
	res = {}
	for a in keys:
		res[a] = {}
		
		for b in keys:
			s = set()
			if a == b: 
				continue
			if not nx.has_path(g,keys[a],keys[b]): 
				continue
			dist = nx.shortest_path_length(g,keys[a],keys[b])
			path = nx.shortest_path(g,keys[a],keys[b])
			
			for k, v in keys.items():
				if v in path[1:-2]:
					s.add(k)
			res[a][b] = (dist, s)
	return res

def getRequirements(keys, doors, path, start, g):
	res = {}
	for k, v in keys.items():
		s = set()
		if not nx.has_path(g,keys[start],v): 
			continue
		path = nx.shortest_path(g,keys[start],v)
		for d, v in doors.items():
			if v in path:
				s.add(d.lower())
		res[k] = s
	return res

def getNeighbours(point, collected):
	
	res = set()
	for k, v in distances[point].items():
		if k in collected:
			continue
		for p in v[1]:
			if p not in collected:
				break
		else:			
			for r in require[point]:
				if r not in collected:
					break
			else:
				res.add( (k,v[0]) )
	return res

def dijkstra(q, nKeys):
	visited = set()
	visits = 0
	while q:

		dist, a,b,c,d, collected = heapq.heappop(q)
		#print(dist, a,b,c,d, collected)
		collected = set(collected)
		collected.update([a,b,c,d])
		collected = ''.join(sorted(collected))

		if (a,b,c,d, collected) in visited:
			continue

		visited.add((a,b,c,d, collected))
		visits += 1

		if len(collected) == nKeys:
			return dist

		for bot in [a,b,c,d]:
			for n, nDist in getNeighbours(bot, collected):
				nDist += dist
				if bot == a: heapq.heappush(q, (nDist, n,b,c,d, collected))
				elif bot == b: heapq.heappush(q, (nDist, a,n,c,d, collected))
				elif bot == c: heapq.heappush(q, (nDist, a,b,n,d, collected))
				elif bot == d: heapq.heappush(q, (nDist, a,b,c,n, collected))

starts = ["@", "!", "§", "$"]


lines = open('p2.txt').read().split("\n")

arr = getArray(lines)

path, keys, doors = getPoints(arr)

g = buildGraph(path)

distances = getDistances(keys, g)

#require = getRequirements(keys, doors, path, s, g)



q = []
require = {}
for st in starts:
	require.update(getRequirements(keys, doors, path, st, g))
heapq.heappush(q, (0, "@", "!", "§", "$", ""))
	
n = len(keys) 

#start = timeit.default_timer()

part1 = dijkstra(q,n)
print(f"Part1: {part1}")

#stop = timeit.default_timer()
#print('Time: ', stop - start)




### OLD TRIES

# def backtrack(current, pending, oldRoute, best):

	
# 	pending.pop(current)
	
# 	if not pending:
# 		return oldRoute

# 	if best and oldRoute["length"] > best["length"]:
# 		return {}

# 	for key in pending:

# 		route = oldRoute.copy()
		
# 		for req in require[key]:
# 			if req not in route["steps"]:
# 				break
# 		else: 

# 			route["length"] += distances[current][key]
# 			route["steps"] += key

# 			route = backtrack(key, pending.copy(), route, best)
# 			if not route:
# 				continue
# 			if not best or route["length"] < best["length"]:
# 				best = route

# 	return best


# def getNeighbours(node):
# 	x,y,z = node
# 	adjList = []
# 	for n in [(0,1),(0,-1),(1,0),(-1,0)]:
# 		_x = x + n[0]
# 		_y = y + n[1]
# 		if (_x, _y) in path:
# 			adjList.append((x+n[0],y+n[1],z))
# 			continue
# 		point = arr[y+n[1]][x+n[0]]
# 		if point in string.ascii_uppercase and point.lower() in z:
# 			adjList.append((x+n[0],y+n[1],z))
# 	return adjList
		

# def bfs(start, n):
# 	q = deque()
# 	visited = set()

	
# 	q.append(start)

# 	while q:
# 		v = q.popleft()
# 		p = arr[v[1]][v[0]]
# 		if p in string.ascii_lowercase and p not in v[2]:
# 			v = (v[0], v[1], v[2] + p)
# 		if len(v[2]) == n:
# 			return v[2]
# 		visited.add(v)
# 		for w in getNeighbours(v):
# 			if w not in visited:
# 				q.append(w)
# 		print(v[2])