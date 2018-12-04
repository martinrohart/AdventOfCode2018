import re
import numpy as np
from collections import defaultdict

with open ("input4.txt", "r") as file:
	rows=file.read().strip().split('\n')

dict = {}
pattern = re.compile(r'\[(.+)\]\s(.+)')

for row in rows:
	parsed = pattern.match(row)
	dict[parsed.group(1)] = parsed.group(2)

keylist = dict.keys()
keylist.sort()

patternGuard = re.compile(r'Guard.#(\d+)')
patternTime = re.compile(r'.+\s00:(\d\d)')
currentGuard = 0
currentStartSleep = 0
guards =defaultdict(lambda: np.zeros(60))

for i in range(len(keylist)):
	instr = dict[keylist[i]]
	guard = patternGuard.match(instr)
	if guard:
		currentGuard = guard.group(1)
	elif instr.startswith('falls'):
		currentStartSleep = int(patternTime.match(keylist[i]).group(1))
	elif instr.startswith('wakes'):
		currentStopSleep = int(patternTime.match(keylist[i]).group(1))
		guards[currentGuard][currentStartSleep:currentStopSleep] += 1

maxPerGuard = map(lambda guard:np.sum(guard) , guards.values())
guard = guards.keys()[np.argmax(maxPerGuard)]
minute = np.argmax(guards[guard])
print "Most asleep guard is %s, with most asleep minute %s. Result is %s" % (guard, minute, int(guard) * minute)

#part 2
argmax = np.argmax(guards.values())
index = np.unravel_index(argmax, np.array(guards.values()).shape)
guardId = guards.keys()[index[0]]
print "Most asleep minute on minute %s, from guard %s. Result is %s" % (index[1], guardId, int(guardId)*index[1])