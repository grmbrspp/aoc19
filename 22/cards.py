deckSize = 10007
#deckSize = 119315717514047
deck = [i for i in range(deckSize)]

def cut(deck, s, n):
	offset = (s+n) % s
	return deck[offset:] + deck[:offset]

def deal(deck, s, n):
	newDeck = deck.copy()
	i = 0
	while deck:
		newDeck[i] = deck.pop(0)
		i = (i+n) % s
	return newDeck

def shuffle(deck, instr):	
	for i in instr:
		n = i.split(" ")[-1]
		if "stack" in i: deck = deck[::-1]
		elif "cut" in i: deck = cut(deck, deckSize, int(n))
		elif "increment" in i: deck = deal(deck, deckSize, int(n))
	return deck

lines = open('input.txt').read().split("\n")

part1 = shuffle(deck.copy(), lines)
print("Part 1: " + str(part1.index(2019)))


# convert rules to linear polynomial.
# (g∘f)(x) = g(f(x))
def parse(size, instr):
	a, b = 1, 0
	for i in instr[::-1]:
		n = i.split(" ")[-1]
		if "stack" in i:
			a = -a
			b = size - b - 1
			
		elif "cut" in i:
			b = (b + int(n)) % size
			
		elif "increment" in i:
			z = pow(int(n), size-2, size)
			a = a*z % size
			b = b*z % size
			
	return a, b

# modpow the polynomial: (ax+b)^m % n
# f(x) = ax+b
# g(x) = cx+d
# f^2(x) = a(ax+b)+b = aax + ab+b
# f(g(x)) = a(cx+d)+b = acx + ad+b
def polypow(a, b, m, n):
	if m == 0:
		return 1, 0
	if m%2 == 0:
		return polypow(a*a % n, (a*b + b) % n, m//2, n)
	
	c, d = polypow(a, b, m-1, n)
	return a*c % n, (a*d + b) % n

def shuffle2(size, times, pos, instr):
	a, b = parse(size, instr)
	a, b = polypow(a, b, times, size)
	return (pos*a + b) % size

deckSize = 119315717514047
times = 101741582076661
pos = 2020

part2 = shuffle2(deckSize, times, pos, lines)
print("Part 2: " + str(part2))