import re

with open ("input3.txt", "r") as file:
	strings=file.read().strip().split('\n')

pattern = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')


rectangles = list(map(lambda s: pattern.match(s),strings))

fabric = [[0 for j in range(1000)] for i in range(1000)]
shared=0

for rectangle in rectangles:
	for i in range(int(rectangle.group(2)), int(rectangle.group(2))+int(rectangle.group(4))):
		for j in range(int(rectangle.group(3)), int(rectangle.group(3))+int(rectangle.group(5))):
			if(fabric[i][j]!=0 and fabric[i][j]!='x'):
				fabric[i][j]='x'
				shared+=1
			elif fabric[i][j]=='x':
				#nothing
				fabric[i][j]='x'
			else:
				fabric[i][j]=rectangle.group(1)
print shared

#Part 2
def checkUnique(rectangle):
	for i in range(int(rectangle.group(2)), int(rectangle.group(2))+int(rectangle.group(4))):
		for j in range(int(rectangle.group(3)), int(rectangle.group(3))+int(rectangle.group(5))):
			if fabric[i][j]!=rectangle.group(1):
				return False
	return True

print filter(checkUnique, rectangles)[0].group(1)