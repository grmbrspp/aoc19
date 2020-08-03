modules=[];
with open('input.txt') as input_file:
		for line in input_file:
			modules.append(int(line));

result = sum([mass//3 - 2 for mass in modules])
print ("Part 1: " + str(result))


result = 0
for mass in modules:
	fuelWeight = mass//3 - 2
	result += fuelWeight
	while True:
		fuelWeight = fuelWeight//3 - 2
		if fuelWeight < 1: break
		result += fuelWeight
		
print ("Part 2: " + str(result))