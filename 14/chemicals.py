import math

def getOre(quantity, chemical): 
	ore = 0
	for item, amount in getRecipe(quantity, chemical).items():
		ore += amount if item == "ORE" else getOre(amount, item)
	return ore
	
def getRecipe(quantity, chemical):
	recipe = {}
	formula = cookbook.get(chemical).copy()
	
	factor = 0
	leftovers = 0 if chemical not in stash else stash[chemical]
	if leftovers < quantity:
		factor = math.ceil( (quantity-leftovers) / formula[0] )
	stash[chemical] = leftovers + factor*formula[0] - quantity
	formula.pop(0)
	
	while formula:
		chemical = formula.pop(0)
		recipe[chemical] = factor*formula.pop(0)
		
	return recipe

def approx(lower, upper, target):
	if lower == upper:
		return lower
	mid = (lower + upper) // 2
	ore = getOre(mid, "FUEL")
	if ore > target:
		return approx(lower, mid-1, target)
	return approx(mid, upper, target)


cookbook = {}
stash = {}

with open("input.txt") as input_file:
	for line in input_file:
		line = line.split("=>")
		inp, out = line[0], line[1]
		
		out = out.strip().split(" ")
		cookbook[out[1]] = [int(out[0])]
		
		for e in inp.split(","):
			e = e.strip().split(" ")
			cookbook[out[1]] += [e[1]] + [int(e[0])] 

part1 = getOre(1, "FUEL")			
print("Part 1: " + str(part1))

target = 1000000000000
i =  target // part1
part2 = approx(i, 2*i, target) - 1
print("Part 2: " + str(part2))