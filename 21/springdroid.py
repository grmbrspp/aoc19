from intcpu import intcpu 

def toAscii(string):
	return [ord(char) for char in string]

def draw(arr):
	for n in arr:
		try:
			print(chr(n), end="")
		except: 
			pass



program = [int(string) for string in open('input.txt').read().split(",")]

springscript = [
"NOT A T",
"NOT B J",
"OR T J",
"NOT C T",
"OR T J",
"NOT D T",
"NOT T T",
"AND T J",
"WALK"
]

droid = intcpu(program)

for instr in springscript:
	for n in toAscii(instr):
		droid.provide(n)
	droid.provide(10)

res = droid.getAll()
#draw(res)
print("Part 1: " + str(res[-1]))


droid.reset()

springscript = [
"NOT C J",
"AND D J",
"AND H J",
"NOT B T",
"AND D T",
"OR T J",
"NOT A T",
"OR T J",
"RUN"
]

for instr in springscript:
	for n in toAscii(instr):
		droid.provide(n)
	droid.provide(10)

res = droid.getAll()
#draw(res)
print("Part 2: " + str(res[-1]))