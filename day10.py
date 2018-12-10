import re
import numpy as np
from collections import defaultdict

pattern = re.compile(r'(-?\d+)')

with open ("input10.txt", "r") as file:
	data = map(lambda row: map(int, re.findall(pattern, row)), file.read().strip().split('\n'))

def getArea(temp):
	area = np.transpose(temp)
	xmin = min(area[0])
	xmax = max(area[0])
	ymin = min(area[1])
	ymax = max(area[1])
	return (xmin,xmax,ymin,ymax)


def printSky():
	xmin,xmax,ymin,ymax = getArea(data)
	sky = [['.' for i in range(xmin,xmax+1)] for j in range(ymin, ymax+1)]
	for i in range(len(data)):
		sky[data[i][1]-ymin][data[i][0]-xmin] = '#'
	
	for j in range(len(sky)):
		print ''.join(sky[j])

xmin,xmax,ymin,ymax = getArea(data)
lastDX=xmax-xmin
lastDY=ymax-ymin
time = 0
while True:
	time+=1
	data2 = map(lambda row: [row[0]+row[2], row[1]+row[3], row[2], row[3]],data)
	xmin,xmax,ymin,ymax = getArea(data2)
	print "Area %s x %s" % (str(xmax-xmin), str(ymax-ymin))

	#if the area increases again, the previous iteration was the local minimum
	if (lastDX<= (xmax-xmin) and lastDY<=(ymax-ymin)):
		printSky()
		print "Time is %s seconds" % str(time-1)
		quit()

	lastDX=xmax-xmin
	lastDY=ymax-ymin
	data = data2


