with open ("input2.txt", "r") as file:
	ids=file.read().strip().split('\n')

#ids=['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']
twos = 0
threes = 0

for id in ids:
	keys = {}
	for letter in list(id):
		if letter in keys:
			keys[letter] = keys[letter] + 1
		else:
			keys[letter] = 1

	if(2 in keys.values()):
		twos+=1
	if(3 in keys.values()):
		threes+=1

print "checksum: "+str(twos*threes)

#Part2
from itertools import combinations
for pair in list(combinations(ids,2)):
	letters1 = list(pair[0])
	letters2 = list(pair[1])
	same=""
	for i in range(len(letters1)):
		if(letters1[i]==letters2[i]):
			same=same+letters1[i]
	if len(same)==len(letters1)-1:
		print "common letters in most similar IDs: "+same

