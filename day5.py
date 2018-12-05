import string
import numpy as np

with open ("input5.txt", "r") as file:
	input=list(file.read().strip())

#input = list("dabAcCaCBAcCcaDA")

def react(input):
	index = 0
	while index < (len(input)-1):
		if (input[index].upper() == input[index+1].upper()) and (input[index] != input[index+1]):
			del input[index:index+2]
			index = index -1
		else:
			index+=1	
	return len(input)

#Part 1
print react(input)

#Part 2
results = []
for char in string.ascii_lowercase:
	filtered = list(filter(lambda x : x != char and x != char.upper() , input))
	results.append(react(filtered))
print np.min(results)