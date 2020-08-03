def getPath(inputString):
	xAxis = {"L": -1, "R": +1, "U": 0, "D": 0}
	yAxis = {"L": 0, "R": 0, "U": +1, "D": -1}
	
	path = []
	current = (0,0)

	for instr in inputString.split(","):
		direction = instr[0]
		length = int(instr[1:])
		
		for step in range(length):
			current = ( current[0] + xAxis[direction], current[1] + yAxis[direction] )
			path.append(current)

	return path

# Real Input
inputs = open('input.txt').read().split("\n")

# Example 1
#inputs = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
# Example 2
#inputs = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
# Example 3
#inputs = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

wires = [getPath(inputs[0]), getPath(inputs[1])]

intersections = set(wires[0]) & set(wires[1])

minDist = min( [ abs(xy[0]) + abs(xy[1]) for xy in intersections ] )
minPath = min( [ wires[0].index(xy) + wires[1].index(xy) + 2 for xy in intersections ] )

print("Part 1: " + str(minDist))
print("Part 2: " + str(minPath))