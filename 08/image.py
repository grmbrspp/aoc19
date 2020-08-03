from collections import Counter

inp = open('input.txt').read().strip()

layers = []
x, y = 25, 6
layerSize = x*y

while inp:
	layers.append( [int(n) for n in inp[:layerSize]] )
	inp = inp[layerSize:]

minLayer = None
for layer in layers:	
	if not minLayer or Counter(layer)[0] < minLayer[0]: 
		minLayer = Counter(layer)
	
part1 = minLayer[1]* minLayer[2]
print("Part 1: " + str(part1))

final = [2 for x in range(layerSize)]

for layer in reversed(layers):
	layer = list(layer)
	for i in range(len(layer)):
		px = int(layer[i])
		if px < 2:
			final[i] = px

print("Part 2:")
while final:
	line = " ".join([str(char) for char in final[:x]])
	print (" " + line.replace("0", " ").replace("1", "#") )
	final = final[x:]