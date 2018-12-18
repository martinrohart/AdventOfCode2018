import re

pattern = re.compile(r'(\d+)')

with open ("input18.txt", "r") as file:
	grid = map(lambda l: list(l), file.read().split('\n'))

def printGrid(grid):
	for line in grid:
		print ''.join(line)

def getCell(y,x):
	if y<0 or x<0 or y>=len(grid) or x>=len(grid[0]):
		return None
	return grid[y][x]

def getAdjacents(x,y):
	return [getCell(y-1,x-1), getCell(y-1,x), getCell(y-1,x+1), getCell(y,x-1), getCell(y,x+1), getCell(y+1,x-1), getCell(y+1,x), getCell(y+1,x+1) ]

def iteration():
	newgrid = [[grid[j][i] for i in range(len(grid[0]))] for j in range(len(grid))]
	#printGrid(newgrid)
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			neighbors = getAdjacents(x,y)
			trees = len(filter(lambda n: n=='|', neighbors))
			lumbers = len(filter(lambda n: n=='#', neighbors))
			if grid[y][x]=='.' and trees>=3:
				newgrid[y][x] = '|'
			elif grid[y][x]=='|' and lumbers>=3:
					newgrid[y][x] = '#'
			elif grid[y][x]=='#':
				if lumbers>=1 and trees>=1:
					newgrid[y][x] = '#'
				else:
					newgrid[y][x] = '.'
	return newgrid

#Part 1
for minute in range(1,11):
	grid = iteration()

lumbers = sum(map(lambda row: len(filter(lambda c: c=='#',row)), grid))
trees = sum(map(lambda row: len(filter(lambda c: c=='|',row)), grid))
print lumbers*trees

#Part 2
seen = {}
start = 0
while True:
	minute+=1
	grid = iteration()
	for g in seen.values():
		if g==grid:	
			if start>0:
				interval = minute-start
				check = start + (1000000000-start) % interval
				print "Repetition interval: %s -> Grid at 1000000000 is the same than grid at %s" % (interval, check)
				lumbers = sum(map(lambda row: len(filter(lambda c: c=='#',row)), seen[check]))
				trees = sum(map(lambda row: len(filter(lambda c: c=='|',row)), seen[check]))
				print lumbers*trees
				quit()
			else:
				print "Pattern repeats at %s" % str(minute)
				start = minute
				seen = {}
	seen[minute] = grid