frequencies = open ("input1.txt", "r").read().split('\n')
print sum([int(f) for f in frequencies]);

#Part 2
final = 0;
keys = {}
i = 0
while True:
	final = final + int(frequencies[i % len(frequencies)])
	i+=1
	if str(final) in keys:
		print "Frequency reached again: "+str(final)
		break
	else:
		keys[str(final)] = final;

