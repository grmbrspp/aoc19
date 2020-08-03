inp = open('input.txt').read().split("\n")
inp.pop()

asteroids = []

for y in range(len(inp)):
	for x in range(len(inp[y])):
		if inp[y][x] == "#":
			asteroids.append((x,y))

best = [None, 0]
for a in asteroids:
	posGrads, negGrads = {}, {}
	for b in asteroids:
		if a is b:
			continue
		
		y = (b[0]-a[0])
		x = (b[1]-a[1])
		
		if y == 0:
			gradient = float("-inf") 
		else: 
			gradient = x/y

		if y == 0:
			y -= x

		if y < 0:
			if gradient in negGrads.keys():
				negGrads[gradient] += [b]
			else: 
				negGrads[gradient] = [b]
		else:
			if gradient in posGrads.keys():
				posGrads[gradient] += [b]
			else: 
				posGrads[gradient] = [b]

	
	los = len(posGrads) + len(negGrads)
	if los > best[1]:
		best = [a, los]

		targetList = []
		for key in sorted(posGrads):
			targetList.append(posGrads[key])
		for key in sorted(negGrads):
			targetList.append(negGrads[key])

print("Part 1: " + str(best[1]))

c = 0
x,y = best[0][1], best[0][0]

while True:
	for i in range(len(targetList)):
		if not targetList[i]:
			continue
		dist = [abs(tup[0]-x)+abs(tup[1]-y) for tup in targetList[i]]
		idx = dist.index(min(dist))
		target = targetList[i].pop(idx)
		c += 1
		if c == 200:
			print("Part 2: " + str(target[0]*100+target[1]))
	if c > 200: break

