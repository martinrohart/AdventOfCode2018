import re
import numpy as np
from collections import deque
from collections import defaultdict

pattern = re.compile(r'initial state: ([\.#]+)')
patternRule = re.compile(r'([\.#]{5})\s=>\s([\.#])')

with open ("input12.txt", "r") as file:
	lines = file.read().strip().split('\n')

initial = pattern.match(lines[0]).group(1)

rules = defaultdict(lambda:'.')
for rule in map(lambda row: patternRule.match(row).groups() ,filter(lambda line: line, lines[1:])):
	rules[rule[0]] = rule[1]

def init():
	state = defaultdict(lambda:'.')
	for i in range(len(initial)):
		state[i] = initial[i]
	return state

def nextState(start):
	nextstate = defaultdict(lambda:'.')
	plants = state.keys()
	for plant in range(min(plants)-2, max(plants)+2):
		rule = state[plant-2] + state[plant-1] + state[plant] + state[plant+1] + state[plant+2]
		nextstate[plant] = rules[rule]

	#Clean starting '.'s
	plants = state.keys()
	for plant in range(min(plants), max(plants)):
		if nextstate[plant]=='#':
			start = plant
			break
		del nextstate[plant]
	return (nextstate, start)

# Part 1

state = init()
start = 0
for generation in range(1,21):
	state, start = nextState(start)
print sum(filter(lambda k: state[k]=='#', state.keys()))


# Part 2 Too many iteration, find a pattern that repeats itself

def getStateString():
	result = ''
	for plant in range(min(state.keys()), max(state.keys())+1):
		result += state[plant]
	return result

def printState(generation):
	print "Iteration %s from %s: %s" % (generation, start, getStateString())

allstates = []
start = 0
previousStart = 0
offset = 0
state = init()
for generation in range(1,1001):# Enough to see the repetition
	state,start = nextState(start)

	# Displaying the state, we can spot the repeting pattern after a while
	#printState(generation)

	pattern = getStateString()
	if pattern in allstates:
		#Pattern already seen
		offset = start-previousStart
	else: 
		allstates.append(pattern)
	previousStart = start

totalOffset = (50000000000-1000)*offset
plantKeys = filter(lambda p: state[p]=='#', state.keys())
print sum(plantKeys) + len(plantKeys)*totalOffset