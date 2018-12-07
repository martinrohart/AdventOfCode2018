import re

with open ("input3.txt", "r") as file:
	strings=file.read().strip().split('\n')

pattern = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')


rectangles = map(lambda s: pattern.match(s).groups(),strings)

fabric = [[0 for j in range(1000)] for i in range(1000)]
shared = 0

for rectangle in rectangles:
	for i in range(int(rectangle[1]), int(rectangle[1])+int(rectangle[3])):
		for j in range(int(rectangle[2]), int(rectangle[2])+int(rectangle[4])):
			if(fabric[i][j]!=0 and fabric[i][j]!='x'):
				fabric[i][j]='x'
				shared+=1
			elif fabric[i][j]!='x':
				fabric[i][j]=rectangle[0]
print shared

#Part 2
def checkUnique(rectangle):
	for i in range(int(rectangle[1]), int(rectangle[1])+int(rectangle[3])):
		for j in range(int(rectangle[2]), int(rectangle[2])+int(rectangle[4])):
			if fabric[i][j]!=rectangle[0]:
				return False
	return True

print filter(checkUnique, rectangles)[0][0]
