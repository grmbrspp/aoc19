from intcpu import intcpu

def getBeam(size):
	beam = set()
	lowerY = 0
	for x in range(size):
		beamFound = False
		for y in range(lowerY, size):

			drone.provide(x)
			drone.provide(y)
			status = drone.getNext()
			drone.reset()

			if status == 0:
				if beamFound: break
				else: continue	

			beam.add((x,y))

			if beamFound: continue

			beamFound = True
			lowerY = y

	return beam


program = [int(string) for string in open('input.txt').read().split(",")]
drone = intcpu(program) 
beam = getBeam(50)

print("Part 1: " + str(len(beam)))

beam = getBeam(1200)
squares = set()

for p in beam:
	if (p[0]+99, p[1]) not in beam:	continue
	if (p[0], p[1]+99) not in beam: continue
	squares.add(p)

res = sorted(squares)[0]

print("Part 2: " + str(10000 * res[0] + res[1]) )