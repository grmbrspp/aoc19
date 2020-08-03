import re

a, b = 108457, 562041
part1, part2 = 0, 0

for num in range(a, b+1):
 	lst = list(str(num))
 	if len(set(lst)) == 6 or lst != sorted(lst):
 		continue
 	part1 += 1
 	
 	for obj in re.finditer(r"(\d)\1+",str(num)): 		
 		if len(obj.group(0)) == 2:
 			part2 += 1
 			break


print("Part 1: " + str(part1))
print("Part 2: " + str(part2))