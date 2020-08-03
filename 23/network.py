from intcpu import intcpu

program = [int(string) for string in open('input.txt').read().split(",")]

network = []
for i in range(50):
	network.append(intcpu(program.copy()))
	network[-1].provide(i)

messages = [ [] for i in range(50) ]
natmem = []
prev = None

while True:
	idle = True
	for i, pc in enumerate(network):
		if not messages[i]:
			pc.provide(-1)
		while messages[i]:
			idle = False
			pc.provide( messages[i].pop(0) )
			
		out = pc.getAll()
		while out:
			idle = False
			a = out.pop(0)
			x = out.pop(0)
			y = out.pop(0)

			if a == 255:
				natmem += [x,y]
			else:
				messages[a].append(x)
				messages[a].append(y)

	if idle:
		network[0].provide(natmem[-2])
		network[0].provide(natmem[-1])

		if prev and prev == natmem[-1]:
			break
		prev = natmem[-1]



print(f"Part 1: {natmem[1]}")
print(f"Part 2: {natmem[-1]}")

