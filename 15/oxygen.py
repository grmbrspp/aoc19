from intcpu import intcpu 
import networkx as nx
import copy

movements = [1,2,3,4]
opposite = {1: 2, 2: 1, 3: 4, 4: 3}
coords = {1: [0,1], 2: [0,-1], 3: [-1,0], 4:[1,0]}
start = (0,0)
g = nx.Graph()

def scan(droid, pos):
	
	oxygen = None
	
	while True:		
		path = []

		for m in movements:
			
			droid.provide(m)
			res = droid.getNext()

			if res == 0:
				continue

			if res == 1:			
				newPos = (pos[0] + coords[m][0], pos[1] + coords[m][1])
				if newPos not in g.nodes:
					path.append(m)
					g.add_edge(pos, newPos)
			
			if res == 2:
				oxygen = (pos[0] + coords[m][0], pos[1] + coords[m][1])
				g.add_edge(pos, oxygen)

			droid.provide(opposite[m])
			droid.getNext()

		if not path:
			return oxygen

		this = path.pop()
		
		while path:
		 	other = path.pop()

		 	clone = copy.deepcopy(droid)
		 	clone.provide(other)
		 	clone.getNext()
			
		 	other_pos = (pos[0] + coords[other][0], pos[1] + coords[other][1])
		 	found = scan(clone, other_pos) 

		 	if found: 
		 		oxygen = found

		droid.provide(this)
		droid.getNext()

		pos = (pos[0] + coords[this][0], pos[1] + coords[this][1])
		

program = [int(string) for string in open('input.txt').read().split(",")]

droid = intcpu(program)
oxygen = scan(droid, start)		

part1 = nx.shortest_path_length(g, source=start, target=oxygen)
print("Part 1: " + str(part1))

part2 = max( [ nx.shortest_path_length(g, source=oxygen, target=node) for node in g.nodes ] )
print("Part 2: " + str(part2))