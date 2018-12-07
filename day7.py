import re
import string
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
	found = []
	for letter in remaining.keys():
		if not(letter in precedents):
			found.append(letter)

	found.sort()
	steps.append(found[0])
	del remaining[found[0]]
	for key in precedents.keys():
		if found[0] in precedents[key]:
			precedents[key].remove(found[0])
			if len(precedents[key])==0:
				del precedents[key]

print ''.join(steps)

#Part 2
def getNextStep():
	if steps:
		for step in steps:
			ok = True
			for precedent in precedents[step]:
				if not precedent in completed:
					ok = False
					break
			if ok:
				steps.remove(step)
				return step

times = {}
for letter in string.ascii_uppercase:
	times[letter] = ord(letter)-64+60

time = 0
workers = 5
working = []
workingOn = []
completed = []

precedents = defaultdict(list)
for pair in data:
	precedents[pair[1]].append(pair[0])

while steps:
	while len(working)>0 and min(working)==time:
		step = workingOn[np.argmin(working)]
		completed.append(step)
		print "Step %s completed at %s" % (step,str(time))
		workingOn.remove(step)
		working.remove(min(working))
		workers+=1

	for worker in range(workers):
		step = getNextStep()
		if step:
			print "Worker starts %s at %s" % (step, str(time))
			stepTime = times[step]
			working.append( time + stepTime)
			workingOn.append(step)
			print "... busy until "+ str(time + stepTime)
			workers-=1

	time += 1