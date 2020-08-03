class intcpu:
	def __init__(self, prog):
		self.prog = prog + [0]*1024*8

		self.pos = 0
		self.base = 0

		self.inp = []
		self.out = []

		self.halted = False
		self.waiting = False

	def setNoun(self, noun):
		prog[1] = noun

	def setVerb(self, verb):
		prog[2] = verb

	def provide(self, inp):
		self.waiting = False
		self.inp.append(inp)

	def getNext(self):
		self.compute()
		return self.out[-1]

	def getFinal(self):
		while not self.halted:
			self.compute()
		return self.out[-1]
		
	def getAll(self):
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
			opcode = self.prog[self.pos]%100
			params = [int(p) for p in list(str(self.prog[self.pos]))[:-2]]
	
			if opcode == 99:
				self.halted = True
				return 

			while len(params) < 3:
				params.insert(0, 0)
			
			arr = []
			for i in range(3):
				if params[2-i] == 0: p = self.prog[self.pos+i+1]
				elif params[2-i] == 1: p = self.pos+i+1
				elif params[2-i] == 2: p = self.base + self.prog[self.pos+i+1]
				arr.append(p)

			x, y, t = arr[0], arr[1], arr[2]
			if opcode in [3,4,9]: 
				t = x		

			if opcode == 1:	self.prog[t] = self.prog[x] + self.prog[y]
			elif opcode == 2: self.prog[t] = self.prog[x] * self.prog[y]
			elif opcode == 3: 
				if self.inp:
					self.prog[t] = self.inp.pop(0)
				else:
					self.waiting = True
					return
			elif opcode == 4: 
				self.out.append(self.prog[t])
				self.pos += 2
				return
			elif opcode == 5: self.pos = self.prog[y]-3	if self.prog[x] != 0 else self.pos
			elif opcode == 6: self.pos = self.prog[y]-3 if self.prog[x] == 0 else self.pos
			elif opcode == 7: self.prog[t] = 1 if self.prog[x] < self.prog[y] else 0
			elif opcode == 8: self.prog[t] = 1 if self.prog[x] == self.prog[y] else 0		
			elif opcode == 9: self.base += self.prog[t]
			else:
				print("Error - Bad opcode")
				break;

			steps = [0,4,4,2,2,3,3,4,4,2]
			self.pos += steps[opcode]


