import re
from collections import defaultdict

pattern = re.compile(r'(.)=(\d+),\s(.)=(\d+)\.\.(\d+)')

with open ("input17.txt", "r") as file:
	lines = map(lambda l: pattern.match(l).groups(), file.read().split('\n'))

coords = defaultdict(lambda:'.')
coordsx = []
coordsy = []
for line in lines:
	for n in range(int(line[3]), int(line[4])+1):
		if line[0]=='x':
			coords[int(line[1]),n] = '#'
			coordsx.append(int(line[1]))
			coordsy.append(n)	
		else:
			coords[n,int(line[1])] = '#'
			coordsy.append(int(line[1]))
			coordsx.append(n)	

grid = [[coords[i,j] for i in range(max(coordsx)+2)] for j in range(max(coordsy)+1)]

def printGrid(grid):
	for line in range(len(grid)):
		print str(line) + ''.join(grid[line][400:])

def getHorizontalRange(x,y):
	#print "checking range at y=%s" % int(y)
	current = x-1
	left = None
	leftFall = None
	while left==None and current>=0:
		if grid[y][current]=='#':
			left = current
		elif grid[y+1][current]=='.':
			leftFall = current
			break
		elif grid[y+1][current]=='|':
			grid[y][x]='|'
			return None,None,None,None
		else:
			current-=1

	current = x+1
	right = None
	rightFall = None
	while right==None and current<= (max(coordsx)+1):
		if grid[y][current]=='#':
			right = current
		elif grid[y+1][current]=='.':
			rightFall = current
			break
		elif grid[y+1][current]=='|':
			grid[y][x]='|'
			return None,None,None,None
		else:
			current+=1
	return left, right, leftFall, rightFall

sources = [(500,0)]

def nextSource():
	global sources
	success = False
	if sources:
		found = False
		while sources and not found:
			x,y = sources[0]
			sources = sources[1:]
			found = grid[y][x] != '~'
			if found:
				return x,y,success
	return None, None, True

x,y,success = nextSource()
while not success:
	y+=1
	if y==max(coordsy):
		grid[y][x] = '|'
		x,y,success = nextSource()
	elif grid[y+1][x]!='.':
		left, right, leftFall, rightFall = getHorizontalRange(x,y)
		if left and right:
			for i in range(left+1, right):
				grid[y][i] = '~'
			y-=2
		elif left and rightFall:
			for i in range(left+1, rightFall+1):
				grid[y][i] = '|'
			x = rightFall
		elif right and leftFall:
			for i in range(leftFall, right):
				grid[y][i] = '|'
			x = leftFall
		elif rightFall and leftFall:
			for i in range(leftFall, rightFall+1):
				grid[y][i] = '|'
			x = leftFall
			sources.append((rightFall,y))
		else:
			x,y,success = nextSource()
	else:
		grid[y][x] = '|'

#printGrid(grid)
print sum(map(lambda row: len(filter(lambda x: x=='|' or x=='~', row)),grid[min(coordsy):]))
print sum(map(lambda row: len(filter(lambda x: x=='~', row)),grid[min(coordsy):]))
