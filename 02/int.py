from intcpu import intcpu

def intcode(prog, noun, verb, step = 4):
	
	prog[1], prog[2] = noun, verb
	pos, opcode = 0, prog[0]

	while opcode != 99:
		x, y, target = prog[pos+1], prog[pos+2], prog[pos+3]
				
		if opcode == 1:
			prog[target] = prog[x] + prog[y]
		elif opcode == 2:
			prog[target] = prog[x] * prog[y]
		else:
			print("Error - Bad opcode")
			break;

		pos += step
		opcode = prog[pos]

	return prog


def getNV(cpu):
	for noun in range(100):
		for verb in range(100):
			cpu.reset()
			cpu.setNoun(noun)
			cpu.setVerb(verb)
			cpu.getFinal()
			if cpu.mem[0] == 19690720:
				return (noun, verb);

programs = []
with open('input.txt') as input_file:
		for line in input_file:
			programs.append([int(n) for n in line.split(",")])

prog = programs[-1]

cpu = intcpu(prog.copy())
cpu.setNoun(12)
cpu.setVerb(2)
cpu.getFinal()
print("Part 1: " + str(cpu.mem[0]))

part2 = getNV(cpu)
print("Part 2: " + str( 100*part2[0] + part2[1] ))