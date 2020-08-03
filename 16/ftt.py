def getPatterns(length):
	base = [0,1,0,-1]
	patterns = []	

	for k in range(length):
		p = []
		for e in base:
			p += (k+1)*[e]

		while len(p) < length+1:
			p += p
		
		patterns.append(p[1:])
	return patterns


def getSignal(sig, n):
	length = len(sig)
	patterns = getPatterns(length)

	for phase in range(n):
		
		digits = [int(i) for i in list(sig)]
		
		sig = ""
		for i in range(length):
			res = 0
			pattern = patterns[i]
			for j in range(length):
				res += digits[j]*pattern[j]
			sig += str(res)[-1]
	return sig


def getSignalEff(sig, n, offset):
	
	digits = [int(i) for i in list(sig)] *10000
	length = len(digits)

	for phase in range(n):
		partialSum = sum(digits[offset:])
		for i in range(offset, length):
			res = partialSum
			partialSum -= digits[i]
			digits[i] = abs(res) % 10

	return "".join([ str(d) for d in digits[offset:offset+8] ])


signal = str( 59758034323742284979562302567188059299994912382665665642838883745982029056376663436508823581366924333715600017551568562558429576180672045533950505975691099771937719816036746551442321193912312169741318691856211013074397344457854784758130321667776862471401531789634126843370279186945621597012426944937230330233464053506510141241904155782847336539673866875764558260690223994721394144728780319578298145328345914839568238002359693873874318334948461885586664697152894541318898569630928429305464745641599948619110150923544454316910363268172732923554361048379061622935009089396894630658539536284162963303290768551107950942989042863293547237058600513191659935 )

part1 = getSignal(signal, 100)[:8]
print("Part 1: " + part1)

msgOffset = int(signal[:7])
part2 = getSignalEff(signal, 100, msgOffset)        
print("Part 2: " + part2)