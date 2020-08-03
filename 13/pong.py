from intcpu import intcpu 

program = [int(string) for string in open('input.txt').read().split(",")]

cpu = intcpu(program.copy())
game = cpu.getAll()

tileIDs = []
i = 2
while i < len(game):
	tileIDs.append(game[i])
	i += 3
	
part1 = tileIDs.count(2) 
print("Part 1: " + str(part1))

program[0] = 2
cpu = intcpu(program)
counter =0 
while not cpu.halted:
	counter += 1
	game = cpu.getQ()
	while game:
		x = game.popleft()
		y = game.popleft()
		id = game.popleft()
		if x == -1: 
			score = id
			continue
		if id == 3:
			paddle = x
		if id == 4:
			ball = x
	if paddle == ball: cpu.provide(0)
	if paddle < ball: cpu.provide(1)
	if paddle > ball: cpu.provide(-1)

print("Part 2: " + str(score))