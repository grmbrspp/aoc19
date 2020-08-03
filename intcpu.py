from collections import deque
from collections import defaultdict

class intcpu:
	def __init__(self, prog):
		self.prog = prog
		self.mem = defaultdict(int, enumerate(prog))

		self.pos = 0
		self.base = 0

		self.steps = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]

		self.inp = deque()
		self.out = deque()

		self.halted = False
		self.waiting = False

	def setNoun(self, noun):
		self.mem[1] = noun

	def setVerb(self, verb):
		self.mem[2] = verb

	def provide(self, inp):
		self.waiting = False
		self.inp.append(inp)

	def provideText(self, inp):
		self.waiting = False
		for char in inp:
			self.inp.append(ord(char))

	def getNext(self):
		self.compute()
		if not self.out:
			return 0
		return self.out[-1]

	def getFinal(self):
		while not self.halted:
			self.compute()
		if not self.out:
			return 0
		return self.out[-1]
	
	def getAll(self):
		while not self.halted and not self.waiting:
			self.compute()
		return list(self.out)

	def getQ(self):
		while not self.halted and not self.waiting:
			self.compute()
		return self.out

	def getPrev(self):
		try:
			return self.out[-2]
		except:
			return 0

	def compute(self):
		while True:	
			instr = self.mem[self.pos]		
			opcode = instr % 100
			params = str(instr//100)[::-1] + "00"			

			if opcode == 99:
				self.halted = True
				return 

			arr = [0,0,0]
			for i in range(3):
				cur = int(params[i])
				if cur == 0: arr[i] = self.mem[self.pos+i+1]
				elif cur == 1: arr[i] = self.pos+i+1
				elif cur == 2: arr[i] = self.base + self.mem[self.pos+i+1]

			x, y, t = arr		

			if opcode == 1:	self.mem[t] = self.mem[x] + self.mem[y]
			elif opcode == 2: self.mem[t] = self.mem[x] * self.mem[y]
			elif opcode == 3: 
				if not self.inp:
					self.waiting = True
					return
				self.mem[x] = self.inp.popleft()					
			elif opcode == 4: 
				self.out.append(self.mem[x])
				self.pos += 2
				return
			elif opcode == 5: self.pos = self.mem[y]-3	if self.mem[x] != 0 else self.pos
			elif opcode == 6: self.pos = self.mem[y]-3 if self.mem[x] == 0 else self.pos
			elif opcode == 7: self.mem[t] = 1 if self.mem[x] < self.mem[y] else 0
			elif opcode == 8: self.mem[t] = 1 if self.mem[x] == self.mem[y] else 0		
			elif opcode == 9: self.base += self.mem[x]
			else:
				print("Error - Bad opcode")
				self.halted = True
				return
			
			self.pos += self.steps[opcode]

	def reset(self):
		self.mem = defaultdict(int, enumerate(self.prog))

		self.pos = 0
		self.base = 0
		
		self.halted = False
		self.waiting = False