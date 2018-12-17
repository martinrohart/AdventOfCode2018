import numpy as np
from operator import itemgetter
from collections import deque

with open ("input15.txt", "r") as file:
	lines = file.read().strip().split('\n')

def printGrid(grid):
	for line in grid:
		print ''.join(line)

def possible_paths(coor):
    # This function checks the 4 available routes around the current point.

	paths = [
    (coor[0]- 1, coor[1]),
    (coor[0],coor[1]-1),
    (coor[0], coor[1] + 1),
    (coor[0] + 1, coor[1])
        ]
	possible_paths = []

	for path in paths:
		if grid[path[1]][path[0]]=='.':             
			possible_paths.append(path)
	return possible_paths

def find_closest_target(coords, tofind):
    previous_move = {}
    distance = {}

    to_visit = deque()
    for incr in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        coords_ = (coords[0] + incr[0], coords[1] + incr[1])
        to_visit.append(coords_)
        previous_move[coords_] = tuple(coords)
        distance[coords_] = 1

    closest = None
    while len(to_visit) > 0:

        new_coords = to_visit.popleft()

        if grid[new_coords[1]][new_coords[0]] == tofind:
            closest = new_coords
            break

        if grid[new_coords[1]][new_coords[0]]!='.':
            continue

        for incr in [(0, -1), (-1, 0), (1, 0), (0, 1)]:

            coords_ = (new_coords[0] + incr[0], new_coords[1] + incr[1])
            if coords_ not in previous_move:
                previous_move[coords_] = new_coords
                distance[coords_] = distance[new_coords] + 1

                to_visit.append(coords_)

    if closest is None:
        return None, None, None

    position = closest
    next_move = previous_move[closest]
    while next_move != tuple(coords):
        position = next_move
        next_move = previous_move[position]

    return closest, position, distance[closest]


def isAttackable(unit, target):
	if target[3]>0 and unit[2]!=target[2]:
		if (unit[0]==target[0] and unit[1]==target[1]-1) or \
		(unit[0]==target[0] and unit[1]==target[1]+1) or \
		(unit[0]==target[0]-1 and unit[1]==target[1]) or \
		(unit[0]==target[0]+1 and unit[1]==target[1]):
			return True
	return False


def getEnemy(unit):
	enemies = filter(lambda t: isAttackable(unit, t), targets)
	if enemies:
		enemies = sorted(enemies, key=itemgetter(3,1,0))
		return enemies[0]
	else:
		return False

def endOfGame(targets):
	nbElf = len(filter(lambda t: t[2]=='E' and t[3]>0,targets))
	nbGobelins= len(filter(lambda t: t[2]=='G' and t[3]>0,targets))
	return (nbElf==0 or nbGobelins==0)

def sumPointsUnits(targets):
	targets = filter(lambda t: t[3]>0,targets)
	return sum([t[3] for t in targets])

def init(attackPower):
	grid = map(lambda line: [str(c) for c in line] , lines)
	targets = []
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x]=='G':
				targets.append((x,y,grid[y][x],200,3))
			elif grid[y][x]=='E':
				targets.append((x,y,grid[y][x],200,attackPower))
	targets = sorted(targets, key=itemgetter(1,0))
	return grid, targets

def play(absoluteWin):
	global grid
	global targets
	turn=1
	while True:
		#print "Turn %s:" % str(turn)
		for t in range(len(targets)):
			target = targets[t]
			if target[3]<=0:
				continue
			if endOfGame(targets):
				points = sumPointsUnits(targets)
				print "END %s, %s: result %s" % (turn-1, points, points*(turn-1) )
				return True

			enemy = getEnemy(target)
			if not enemy:
				if target[2] == 'E':
					tofind = 'G'
				else:
					tofind = 'E'
				closest, step, distance = find_closest_target( (target[0], target[1]), tofind)
				if step:
					#print "Move %s to %s" % (str(target), str(step))
					grid[target[1]][target[0]] = '.'
					target = (step[0], step[1], target[2], target[3], target[4])
					grid[step[1]][step[0]] = target[2]
					targets[t] = target
					enemy = getEnemy(target)
			if enemy:
				enemy = (enemy[0], enemy[1], enemy[2], enemy[3] - target[4], enemy[4])
				#print "Enemy attacked %s" % str(enemy)
				for e in range(len(targets)):
					if targets[e][0]==enemy[0] and targets[e][1]==enemy[1]:
						targets[e] = enemy
						break
				if enemy[3]<=0:
					#print "Enemy died"
					grid[enemy[1]][enemy[0]] = '.'
					if absoluteWin and enemy[2]=='E':
						return False
		targets = filter(lambda t: t[3]>0,targets)
		targets = sorted(targets, key=itemgetter(1,0))
		turn+=1
		#printGrid(grid)

#Part 1
attackPower = 3
grid, targets = init(attackPower)
play(False)

#Part2
while True:
	attackPower+=1
	grid, targets = init(attackPower)
	if play(True):
		print "Attack power needed: %s" % str(attackPower)
		break
