import re
import numpy as np
from collections import defaultdict

with open ("input6.txt", "r") as file:
	rows = file.read().strip().split('\n')

pattern = re.compile(r'(\d+),\s(\d+)')
data = map(lambda row: map(int ,pattern.match(row).groups()), rows)
temp = np.transpose(data)
maxx = max(temp[0])
maxy = max(temp[1])

def getClosest(x,y):
	distances = [abs(data[j][0]-x) + abs(data[j][1]-y) for j in range(len(data))]
	minimum = min(distances)
	if(len(np.where(distances == minimum))>1):
		return "."
	return np.argmin(distances);

def part1():
	grid = [[getClosest(i, j) for j in range(maxy)] for i in range(maxx)]
	areas = defaultdict(int)
	excluded = {}
	for i in range(maxx):
		for j in range(maxy):
			areas[grid[i][j]] +=1
			if(i==0 or i==maxx-1 or j==0 or j==maxy-1):
				excluded[grid[i][j]] = True

	for key in excluded.keys():
		del areas[key]

	return max(areas.values())

def part2():
	result = 0
	for x in range(maxx):
		for y in range(maxy):
			if np.sum(map(lambda row: abs(row[0]-x) + abs(row[1]-y) ,data)) < 10000:
				result += 1
	return result

print part1()
print part2()
