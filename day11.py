import numpy as np

gridSerialNumber = 1133

def getPower(x,y):
	rackID = x+1+10
	powerLevel = (rackID * (y+1) + gridSerialNumber) * rackID
	hundredDigit = int(str(powerLevel)[-3])
	return hundredDigit-5

def getFuel(x,y,size):
	if x<=(300-size) and y<=(300-size):
		return sum([ sum([power[i][j] for i in range(x, x+size)]) for j in range(y, y+size)])
	else:
		return 0

power = [[getPower(i,j) for i in range(300)] for j in range(300)]

fuel = [[getFuel(i,j,3) for i in range(300)] for j in range(300)]
argmax = np.argmax(fuel)
index = np.unravel_index(argmax, np.array(fuel).shape)
print "Max size 3 is %s,%s" % (index[0]+1,index[1]+1)


#Part 2, need more speed, use https://en.wikipedia.org/wiki/Summed-area_table

s = np.zeros([300,300], dtype = int)

def ss(x,y):
	if x<0 or y<0:
		return 0
	return s[x][y]

for y in range(300):
	for x in range(300):
		s[x][y] = power[x][y] + ss(x,y-1) + ss(x-1,y) - ss(x-1,y-1)

def getFuelGridValue(x,y,size):
	return ss(x-1,y-1) + ss(x+size-1,y+size-1) - ss(x-1,y+size-1) - ss(x+size-1,y-1)

def getFuelGrid(size):
	return [[ getFuelGridValue(i,j, size) for i in range(300-size)] for j in range(300-size)]

sizes = [np.max(getFuelGrid(size)) for size in range(1,300)]
maxSize = np.argmax(sizes)+1
maxGrid = getFuelGrid(maxSize)
argmax = np.argmax(maxGrid)
index = np.unravel_index(argmax, np.array(maxGrid).shape)
print "Max is %s,%s,%s" % (index[0]+1, index[1]+1, maxSize)