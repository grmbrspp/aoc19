from intcpu import intcpu 

def draw(arr):
	for n in arr:
		try:
			print(chr(n), end="")
		except: 
			pass



program = [int(string) for string in open('input.txt').read().split(",")]


droid = intcpu(program)

while True:
	res = droid.getAll()
	draw(res)
	droid.provideText(input())
	droid.provide(10)

