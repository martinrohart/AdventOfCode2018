import re
import numpy as np
from collections import defaultdict

pattern = re.compile(r'Step\s([A-Z]).*step\s([A-Z])')

with open ("input7.txt", "r") as file:
	data = map(lambda row: pattern.match(row).groups() , file.read().strip().split('\n'))

precedents = defaultdict(list)
remaining = defaultdict()
for pair in data:
	precedents[pair[1]].append(pair[0])
	remaining[pair[0]] = True
	remaining[pair[1]] = True

steps = []
while len(remaining.keys())>0:
	found = [l for l in remaining.keys() if not(precedents[l]) ]
	found.sort()

	steps.append(found[0])
	del remaining[found[0]]

	for key in precedents.keys():
		precedents[key] = [l for l in (precedents[key]) if l!=found[0] ]

print ''.join(steps)

#Part 2

times = {}
for step in steps:
	times[step] = ord(step)-64+60

time = 0
workers = 5
working = []
workingOn = []
completed = []

def getNextStep():
	for step in steps:
		blocking = [l for l in precedents[step] if not l in completed]
		if not blocking:
			steps.remove(step)
			return step
			
precedents = defaultdict(list)
for pair in data:
	precedents[pair[1]].append(pair[0])

while steps:
	while working and min(working)==time:
		step = workingOn[np.argmin(working)]
		completed.append(step)
		#print "Step %s completed at %s" % (step,str(time))
		workingOn.remove(step)
		working.remove(min(working))
		workers+=1

	for worker in range(workers):
		step = getNextStep()
		if step:
			#print "Worker starts %s at %s" % (step, str(time))
			stepTime = times[step]
			working.append( time + stepTime)
			workingOn.append(step)
			print "... busy until "+ str(time + stepTime)
			workers-=1

	time += 1