import networkx as nx

def getOrbit(graph, node):
	orbits = 0
	for succ in graph.successors(node):
		orbits += 1 + getOrbit(graph, succ)
	return orbits


graph = nx.DiGraph()
for line in [string for string in open('input.txt').read().split("\n")]:
	if line:
		edge = line.split(")")
		graph.add_edge(edge[0], edge[1])

orbSum = sum( getOrbit(graph, node) for node in graph.nodes )
pathLength = nx.shortest_path_length(graph.to_undirected(), source="YOU", target="SAN") - 2

print("Part 1: " + str(orbSum))
print("Part 2: " + str(pathLength))