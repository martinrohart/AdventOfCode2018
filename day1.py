with open ("input1.txt", "r") as myfile:
	input=myfile.read()
frequencies = input.split('\n');

final = 0;
for frequency in frequencies:
	final = final + int(frequency)

print "Final frequency: "+ str(final)

#Part 2

final = 0;
keys = {}
i = 0
while i<len(frequencies):
	final = final + int(frequencies[i])
	i+=1
	if i==len(frequencies):
		i = 0
	if str(final) in keys:
		print "Frequency reached again: "+str(final)
		break
	else:
		keys[str(final)] = final;

