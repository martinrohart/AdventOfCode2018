import re

pattern = re.compile(r'(\d+)')

with open ("input8.txt", "r") as file:
	data = map(int,re.findall(pattern, file.read().strip()))

def parse(index):
	#print "parse from %s : %s" % (index, data[index:])
	children = data[index]
	nbMetadata = data[index+1]
	index = index +2
	for i in range(children):
		index = parse(index)

	for m in range(nbMetadata):
		metadata.append(data[index+m])

	return index+nbMetadata


metadata = []
parse(0)
print sum(metadata)

def computeValue():
	global g
	children = data[g]
	nbMetadata = data[g+1]
	g = g +2
	value = 0
	values = []

	for i in range(children):
		values.append(computeValue())

	for m in range(nbMetadata):
		metadata = data[g+m]
		if children==0:
			value += metadata
		else:
			if(metadata <= len(values)):
				value += values[metadata-1]

	g = g+nbMetadata
	return value

g = 0
print computeValue()