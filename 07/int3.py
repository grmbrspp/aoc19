import itertools
from intcpu import intcpu

program = [int(string) for string in open('input.txt').read().split(",")]

outputs=[]
for phaseSetting in itertools.permutations(range(5)):
	value = 0
	for phase in phaseSetting:
		amp = intcpu(program.copy())
		amp.provide(phase)
		amp.provide(value)
		value = amp.getNext()
	outputs.append(value)

print("Part 1: " + str( max(outputs) ))

outputs=[]
for phaseSetting in itertools.permutations(range(5,10)):
	amps = []
	for i in range(5):
		amp = intcpu(program.copy())
		amp.provide(phaseSetting[i])
		amps.append(amp)
	currentAmp = 0
	value = 0
	while not amps[-1].halted:
		amps[currentAmp].provide(value)
		value = amps[currentAmp].getNext()
		currentAmp = currentAmp + 1 if currentAmp < 4 else 0
	outputs.append(value)
print("Part 2: " + str( max(outputs) ))	
