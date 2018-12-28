from heapq import heappush, heappop

depth = 7863
target = (14,760)
erosions = {}
risks = {}
#depth=510
#target = (10,10)

def getGeologicIndex(x,y):
	if x==0 and y==0:
		return 0
	if x==target[0] and y==target[1]:
		return 0
	if y==0:
		return x * 16807
	if x==0:
		return y * 48271
	return getErosionLevel(x-1, y) * getErosionLevel(x, y-1)


def getErosionLevel(x,y):
	if (x,y) in erosions:
		return erosions[(x,y)]
	erosion = (getGeologicIndex(x,y) + depth) % 20183
	erosions[(x,y)] = erosion
	return erosion


def getRisk(x,y):
	if (x,y) in risks:
		return risks[(x,y)]
	risk = getErosionLevel(x,y) % 3
	risks[(x,y)] = risk
	return risk

print sum([sum([getRisk(x,y) for x in range(target[0]+1)]) for y in range(target[1]+1)])

def getTime(coords, currentEq):
	risk = getRisk(coords[0],coords[1])
	if risk==0 and (coords[2]=='' or currentEq==''):
		return None
	elif risk==1 and (coords[2]=='T' or currentEq=='T'):
		return None
	elif risk==2 and (coords[2]=='C' or currentEq=='C'):
		return None
	return 1 if coords[2]==currentEq else 8

def getPossiblePaths(x,y,currentEq):
	possible = []
	for incr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		for eq in ['','T','C']:
			coords_ = (x + incr[0], y + incr[1], eq)
			if coords_[0]<0 or coords_[1]<0:
				continue
			time_ = getTime(coords_, currentEq)
			if time_:
				possible.append((coords_, time_))
	return possible

def find_quickest_target(coords, target):
	previous_move = {}
	visited = {}

	to_visit = [(0, coords[0], coords[1], coords[2])]
	visited[str(coords)] = 0
	while len(to_visit) > 0:

		t, x ,y,eq = heappop(to_visit)

		if x==target[0] and y==target[1] and eq==target[2]:
			print "Goal in %s min" % visited[str(target)]
			break
		else:
			for coords_,t_ in getPossiblePaths(x,y,eq):
				ntime = t + t_
				if str(coords_) not in visited or ntime < visited[str(coords_)]:
					visited[str(coords_)] = ntime
					#previous_move[str(coords_)] = new_coords
					heappush(to_visit, (ntime, coords_[0], coords_[1], coords_[2]))

	print visited[str(target)]
	#next_move = previous_move[str(target)]
	#while next_move != tuple(coords):
	#	print next_move
	#	print visited[str(next_move)]
	#	next_move = previous_move[str(next_move)]

find_quickest_target( (0,0,'T'), (target[0], target[1], 'T'))